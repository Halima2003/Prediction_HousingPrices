import streamlit as st
from formulaire import get_forms
import model_helper as models
import pandas as pd

from dataclasses import asdict

st.set_page_config(
    page_title="Prédiction du prix d'un logement",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Prédicteur de prix immobilier à Londres")

st.markdown("""
Cette application utilise plusieurs modèles de Machine Learning
pour estimer le prix d'un bien immobilier à Londres en fonction
de ses caractéristiques.
""")

# ==========================
# Modèles disponibles
# ==========================

RIDGE = "Ridge"
RANDOM_FOREST = "Random Forest"
GRADIENT_BOOSTING = "Gradient Boosting"
XGBOOST = "XGBoost"

MODEL_MAPPING = {
    RIDGE: models.get_ridge_model,
    RANDOM_FOREST: models.get_random_forest_model,
    GRADIENT_BOOSTING: models.get_gradient_boosting_model,
    XGBOOST: models.get_xgboost_model
}

st.subheader("🤖 Choisissez un modèle")

selected_model = st.selectbox(
    "Modèle",
    [
        "--",
        RIDGE,
        RANDOM_FOREST,
        GRADIENT_BOOSTING,
        XGBOOST
    ]
)

user_input = get_forms()

# Conversion en format ML
ml_data = asdict(user_input.convert_to_mlinput())

mlinput = pd.DataFrame([ml_data])

# Renommage des colonnes
column_mapping = models.get_column_mapping()
mlinput = mlinput.rename(columns=column_mapping)

# Réorganisation des colonnes
feature_names = models.get_feature_names()

mlinput = mlinput.reindex(
    columns=feature_names,
    fill_value=0
)


if selected_model != "--":

    model = MODEL_MAPPING[selected_model]()

    prediction_value = model.predict(mlinput)[0]

    st.success(
        f"### 💰 Prix estimé : {prediction_value:,.0f} £"
    )

    st.info(f"""
    **Modèle utilisé :** {selected_model}

    Prix prédit du logement :
    **{prediction_value:,.0f} £**
    """)


st.markdown("---")

if st.checkbox("📊 Comparer tous les modèles"):

    st.subheader("Comparaison des prédictions")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        value = models.get_ridge_model().predict(mlinput)[0]

        st.metric(
            label="Ridge",
            value=f"{value:,.0f} £"
        )

    with col2:
        value = models.get_random_forest_model().predict(mlinput)[0]

        st.metric(
            label="Random Forest",
            value=f"{value:,.0f} £"
        )

    with col3:
        value = models.get_gradient_boosting_model().predict(mlinput)[0]

        st.metric(
            label="Gradient Boosting",
            value=f"{value:,.0f} £"
        )

    with col4:
        value = models.get_xgboost_model().predict(mlinput)[0]

        st.metric(
            label="XGBoost",
            value=f"{value:,.0f} £"
        )

    st.info("""
    💡 **Interprétation**

    Si les quatre modèles donnent des résultats proches,
    la prédiction est généralement plus fiable.

    Si les écarts sont importants, cela peut indiquer
    un logement atypique ou une plus grande incertitude
    dans l'estimation.
    """)

