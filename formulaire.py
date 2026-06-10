import streamlit as st
from objets import UserInput


def get_forms() -> UserInput:
    """
    Affiche le formulaire et retourne un UserInput.
    """

    with st.sidebar:

        st.header("🏠 Informations du logement")

        Square_Meters = st.number_input(
            "Surface (m²)",
            min_value=20,
            max_value=500
        )

        Bedrooms = st.number_input(
            "Nombre de chambres",
            min_value=1,
            max_value=5
        )

        Bathrooms = st.number_input(
            "Nombre de salles de bain",
            min_value=1,
            max_value=3
        )

        Floors = st.number_input(
            "Nombre d'étages",
            min_value=1,
            max_value=4
        )

        Building_Age = st.number_input(
            "Âge du logement (années)",
            min_value=1,
            max_value=100
        )

        Garage = st.radio(
            "Garage",
            ["Oui", "Non"]
        )

        Garden = st.radio(
            "Jardin",
            ["Oui", "Non"]
        )

        Neighborhood = st.selectbox(
            "Quartier",
            [
                "Camden",
                "Chelsea",
                "Greenwich",
                "Islington",
                "Kensington",
                "Marylebone",
                "Notting Hill",
                "Shoreditch",
                "Soho",
                "Westminster"
            ]
        )

        Property_Type = st.selectbox(
            "Type de logement",
            [
                "Appartement",
                "Maison individuelle",
                "Maison jumelée"
            ]
        )

        Heating_Type = st.selectbox(
            "Type de chauffage",
            [
                "Chauffage central",
                "Chauffage électrique",
                "Chauffage au gaz",
                "Chauffage au sol"
            ]
        )

        Balcony = st.selectbox(
            "Balcon",
            [
                "Balcon haut",
                "Balcon bas",
                "Sans balcon"
            ]
        )

        Interior_Style = st.selectbox(
            "Style intérieur",
            [
                "Classique",
                "Industriel",
                "Minimaliste",
                "Moderne"
            ]
        )

        View = st.selectbox(
            "Vue",
            [
                "Skyline urbain",
                "Jardin",
                "Parc",
                "Mer",
                "Rue"
            ]
        )

        Materials = st.selectbox(
            "Matériau principal",
            [
                "Granit",
                "Marbre",
                "Bois",
                "Sol stratifié"
            ]
        )

        Building_Status = st.selectbox(
            "État du logement",
            [
                "Neuf",
                "Ancien",
                "Rénové"
            ]
        )

        user_input = UserInput(
            Square_Meters,
            Bedrooms,
            Bathrooms,
            Floors,
            Building_Age,
            Garage,
            Garden,
            Neighborhood,
            Property_Type,
            Heating_Type,
            Balcony,
            Interior_Style,
            View,
            Materials,
            Building_Status
        )

    return user_input