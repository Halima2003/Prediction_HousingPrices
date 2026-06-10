from pathlib import Path
import pickle
import json

from sklearn.pipeline import Pipeline
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
)
from sklearn.linear_model import Ridge
import xgboost as xgb


# dossier contenant les modèles
MODEL_DIR = Path("models")


def get_feature_names() -> list:
    """
    Charge les colonnes attendues par les modèles.
    """
    with open(MODEL_DIR / "feature_names.json", "r") as f:
        return json.load(f)


def get_column_mapping() -> dict:
    """
    Mapping entre les attributs Python (MLInput)
    et les colonnes utilisées pendant l'entraînement.
    """
    return {

        # numériques
        "Square_meters": "Square_Meters",
        "Bedrooms": "Bedrooms",
        "Bathrooms": "Bathrooms",
        "Floors": "Floors",
        "Building_age": "Building_Age",

        # binaires
        "Garage_Yes": "Garage_Yes",
        "Garden_Yes": "Garden_Yes",

        # Neighborhood
        "Neighborhood_Chelsea": "Neighborhood_Chelsea",
        "Neighborhood_Greenwich": "Neighborhood_Greenwich",
        "Neighborhood_Islington": "Neighborhood_Islington",
        "Neighborhood_Kensington": "Neighborhood_Kensington",
        "Neighborhood_Marylebone": "Neighborhood_Marylebone",
        "Neighborhood_Notting_Hill": "Neighborhood_Notting Hill",
        "Neighborhood_Shoreditch": "Neighborhood_Shoreditch",
        "Neighborhood_Soho": "Neighborhood_Soho",
        "Neighborhood_Westminster": "Neighborhood_Westminster",

        # Property Type
        "Property_Type_Detached_House":
            "Property_Type_Detached House",

        "Property_Type_Semi_Detached":
            "Property_Type_Semi-Detached",

        # Heating Type
        "Heating_Type_Electric_Heating":
            "Heating_Type_Electric Heating",

        "Heating_Type_Gas_Heating":
            "Heating_Type_Gas Heating",

        "Heating_Type_Underfloor_Heating":
            "Heating_Type_Underfloor Heating",

        # Balcony
        "Balcony_Low_Level_Balcony":
            "Balcony_Low-level Balcony",

        "Balcony_No_Balcony":
            "Balcony_No Balcony",

        # Interior Style
        "Interior_Style_Industrial":
            "Interior_Style_Industrial",

        "Interior_Style_Minimalist":
            "Interior_Style_Minimalist",

        "Interior_Style_Modern":
            "Interior_Style_Modern",

        # View
        "View_Garden": "View_Garden",
        "View_Park": "View_Park",
        "View_Sea": "View_Sea",
        "View_Street": "View_Street",

        # Materials
        "Materials_Laminate_Flooring":
            "Materials_Laminate Flooring",

        "Materials_Marble":
            "Materials_Marble",

        "Materials_Wood":
            "Materials_Wood",

        # Building Status
        "Building_Status_Old":
            "Building_Status_Old",

        "Building_Status_Renovated":
            "Building_Status_Renovated",
    }


def load_model(name: str):
    """
    Charge un modèle sauvegardé.
    """
    with open(MODEL_DIR / f"{name}_Model.pkl", "rb") as f:
        return pickle.load(f)


def get_ridge_model() -> Pipeline:
    return load_model("Ridge")


def get_random_forest_model() -> RandomForestRegressor:
    return load_model("RandomForest")


def get_gradient_boosting_model() -> GradientBoostingRegressor:
    return load_model("GradientBoosting")


def get_xgboost_model() -> xgb.XGBRegressor:
    return load_model("XGBoost")