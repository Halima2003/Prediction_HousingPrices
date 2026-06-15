# 🏠 London House Price Predictor

Application de Machine Learning permettant d'estimer le prix d'un bien immobilier à Londres à partir de ses caractéristiques.
Le projet comprend :

- Préparation et nettoyage des données
- Entraînement de plusieurs modèles de régression
- Sauvegarde des modèles entraînés
- Interface utilisateur Streamlit pour réaliser des prédictions

---

# 📂 Structure du projet

```text
.
│
├── london_houses.csv
├── training.py
├── model_helper.py
├── objets.py
├── formulaire.py
├── app.py
│
├── models/
│   ├── feature_names.json
│   ├── Ridge_Model.pkl
│   ├── RandomForest_Model.pkl
│   ├── GradientBoosting_Model.pkl
│   └── XGBoost_Model.pkl
│
└── README.md
```

---

# 📊 Jeu de données

Le dataset contient des informations sur des logements londoniens :

| Variable | Description |
|-----------|-------------|
| Bedrooms | Nombre de chambres |
| Bathrooms | Nombre de salles de bain |
| Square_Meters | Surface du logement |
| Building_Age | Âge du bâtiment |
| Floors | Nombre d'étages |
| Neighborhood | Quartier |
| Property_Type | Type de logement |
| Garage | Présence d'un garage |
| Garden | Présence d'un jardin |
| Heating_Type | Type de chauffage |
| Balcony | Type de balcon |
| Interior_Style | Style intérieur |
| View | Vue du logement |
| Materials | Matériaux principaux |
| Building_Status | État du bâtiment |
| Price | Prix du logement (variable cible) |

---

# 🧹 Prétraitement des données

Le script `training.py` effectue :

### Nettoyage

- Suppression des doublons
- Gestion des valeurs manquantes
- Filtrage des valeurs aberrantes sur le prix

### Contraintes métier

- Surface minimale : 20 m²
- Au moins 1 chambre
- Au moins 1 salle de bain
- Âge du bâtiment compris entre 1 et 99 ans

### Encodage

Variables binaires :

- Garage
- Garden

Variables catégorielles :

- Neighborhood
- Property_Type
- Heating_Type
- Balcony
- Interior_Style
- View
- Materials
- Building_Status

Encodage réalisé avec :

```python
pd.get_dummies(drop_first=True)
```

---

# 🤖 Modèles entraînés

Quatre modèles de régression sont utilisés :

## 1. Ridge Regression

Régression linéaire régularisée.

Avantages :

- Rapide
- Interprétable
- Bonne baseline

---

## 2. Random Forest Regressor

Forêt d'arbres de décision.

Avantages :

- Robuste
- Capture les non-linéarités
- Peu sensible aux outliers

---

## 3. Gradient Boosting Regressor

Méthode d'ensemble basée sur le boosting.

Avantages :

- Très bonne précision
- Souvent performante sur les données tabulaires

---

## 4. XGBoost Regressor

Version optimisée du Gradient Boosting.

Avantages :

- Très performant
- Gestion avancée des interactions entre variables

---

# 📈 Résultats obtenus

| Modèle | MAE | R² |
|----------|----------|----------|
| Ridge | 158 661 £ | 0.942 |
| Random Forest | 139 999 £ | 0.959 |
| Gradient Boosting | 50 466 £ | 0.993 |
| XGBoost | 96 641 £ | 0.968 |

Le modèle **Gradient Boosting** est celui qui obtient les meilleures performances sur l'ensemble de test.

---
# Installation

## Cloner le projet

git clone https://github.com/ton-compte/Prediction_HousingPrices.git

## Accéder au dossier

cd Prediction_HousingPrices

## Installer les dépendances

uv sync

# 🚀 Lancer l'entraînement

```bash
uv run training.py
```

Les modèles entraînés sont automatiquement sauvegardés dans le dossier :

```text
models/
```

---

# 💻 Lancer l'application Streamlit


```bash
uv run streamlit run app.py 
```
---

# 🏠 Fonctionnement de l'application

L'utilisateur renseigne :

- Surface du logement
- Nombre de chambres
- Nombre de salles de bain
- Nombre d'étages
- Âge du bâtiment
- Quartier
- Type de propriété
- Présence d'un garage
- Présence d'un jardin
- Type de chauffage
- Type de balcon
- Style intérieur
- Vue
- Matériaux
- État du bâtiment

L'application :

1. Encode automatiquement les informations saisies
2. Recharge le modèle sélectionné
3. Génère une estimation du prix du bien
4. Permet de comparer les résultats des quatre modèles

---

# 🛠️ Technologies utilisées

- Python
- Uv
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Streamlit

---

# 👩‍💻 Auteur
- Halima KADDAR 
- Sara KHALLOUD 
- Ikram ELFAHLI
- Etudiantes en M2 Ingénierie des Données et Evaluations Econométriques à L'Université d'Angers.
