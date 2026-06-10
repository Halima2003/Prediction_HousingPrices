import pandas as pd
import numpy as np
from pathlib import Path
import json
import pickle


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
)
from sklearn.linear_model import Ridge
import xgboost as xgb


def load_and_clean(filepath: str) -> pd.DataFrame:
    """
    Charge et nettoie la base de données.

    Étapes :
    - Chargement CSV (séparateur point-virgule)
    - Suppression de la colonne Adress 
    - Vérification et suppression des doublons
    - Gestion des valeurs aberrantes
    - Encodage des variables catégorielles
    - Création de features dérivées
    """
    df = pd.read_csv(filepath, sep=";")
    print(f"dimensions : {df.shape}")
    print(df.head())

    #Suppression des doublons
    n_before = len(df)
    df = df.drop_duplicates()
    print(f"Doublons supprimés : {n_before - len(df)}")

    #valeurs manquantes
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    cat_cols = df.select_dtypes(include=["object", "str"]).columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    #Suppression des valeurs aberrantes
    Q1 = df["Price"].quantile(0.25)
    Q3 = df["Price"].quantile(0.75)
    IQR = Q3 - Q1
    df = df[
        (df["Price"] >= Q1 - 3 * IQR) &
        (df["Price"] <= Q3 + 3 * IQR)
    ]
    print(f"Lignes après filtrage outliers Price : {len(df)}")

    #Contraintes métier        
    df = df[df["Square_Meters"] >= 20]    
    df = df[df["Bedrooms"] >= 1]     
    df = df[df["Bathrooms"] >= 1]   
    df = df[df["Building_Age"] >= 1]    
    df = df[df["Building_Age"] <= 99]


    #Encodage binaire
    df["Garage_Yes"] = (df["Garage"] == "Yes").astype(int)
    df["Garden_Yes"] = (df["Garden"] == "Yes").astype(int)

    #Onehot encoding 
    df = pd.get_dummies(
        df,
        columns=["Neighborhood", "Property_Type", "Heating_Type", "Balcony", "Interior_Style", "View", "Materials", "Building_Status"],
        drop_first=True, 
        dtype=int
    )

    df = df.drop(columns=["Garage", "Garden"], errors="ignore")

    print(f"Shape final : {df.shape}")
    print(f"Colonnes : {list(df.columns)}")
    return df

# Entrainement des modèles

def train_models(df: pd.DataFrame, model_dir: str = "models") -> dict:
    """
    Entraîne 4 modèles adaptés à la régression immobilière :

    1. Ridge Regression      — baseline linéaire régularisé
    2. Random Forest         — robuste aux outliers, capture les non-linéarités
    3. Gradient Boosting     — haute précision, standard pour l'immobilier
    4. XGBoost               — performant sur données tabulaires, gère les interactions

    Retourne un dictionnaire {nom: (modèle, métriques)}.
    """
    Path(model_dir).mkdir(exist_ok=True)

    TARGET = "Price"
    FEATURES = [c for c in df.columns if c != TARGET]

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Sauvegarde des noms de features
    with open(f"{model_dir}/feature_names.json", "w") as f:
        json.dump(FEATURES, f)

    models_config = {
        "Ridge": Pipeline([
            ("scaler", StandardScaler()),
            ("model", Ridge(alpha=10.0)),
        ]),
        "RandomForest": RandomForestRegressor(
            n_estimators=200,
            max_depth=15,
            min_samples_split=5,
            random_state=42,
            n_jobs=-1,
        ),
        "GradientBoosting": GradientBoostingRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=5,
            subsample=0.8,
            random_state=42,
        ),
        "XGBoost": xgb.XGBRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            verbosity=0,
        ),
    }

    results = {}
    print("\nRésultats d'entraînement")
    for name, model in models_config.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        r2 = r2_score(y_test, preds)
        print(f"{name:20s} | MAE = {mae:10.2f} € | R² = {r2:.4f}")

        # Sauvegarde
        with open(f"{model_dir}/{name}_Model.pkl", "wb") as f:
            pickle.dump(model, f)

        results[name] = {"model": model, "mae": mae, "r2": r2}

    return results

if __name__ == "__main__":

    df_clean = load_and_clean("london_houses.csv")

    print("\nAperçu des données nettoyées :")
    print(df_clean.head())

    print("\nStatistiques descriptives :")
    print(df_clean.describe()) 
    results = train_models(df_clean) 

