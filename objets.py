from dataclasses import dataclass

@dataclass
class MLInput:
    """
    Données encodées au format attendu par les modèles ML.
    """
    Square_Meters: float
    Bedrooms: int
    Bathrooms: int
    Floors: int
    Building_Age: int

    Garage_Yes: bool
    Garden_Yes: bool
    
    Neighborhood_Chelsea: bool
    Neighborhood_Islington: bool
    Neighborhood_Kensington: bool
    Neighborhood_Marylebone: bool
    Neighborhood_Notting_Hill: bool
    Neighborhood_Shoreditch: bool
    Neighborhood_Soho: bool
    Neighborhood_Westminster: bool
    Neighborhood_Greenwich: bool

    Property_Type_Semi_Detached: bool
    Property_Type_Detached_House: bool

    Heating_Type_Electric_Heating: bool
    Heating_Type_Gas_Heating: bool
    Heating_Type_Underfloor_Heating: bool

    Balcony_No_Balcony: bool
    Balcony_Low_Level_Balcony: bool

    Interior_Style_Industrial: bool
    Interior_Style_Minimalist: bool
    Interior_Style_Modern: bool

    View_Garden: bool
    View_Park: bool
    View_Sea: bool
    View_Street: bool

    Materials_Laminate_Flooring: bool
    Materials_Marble: bool
    Materials_Wood: bool

    Building_Status_Old: bool
    Building_Status_Renovated: bool
 
@dataclass
class UserInput:
    """
    Données brutes saisies par l'utilisateur.
    """
    Square_Meters: int           
    Bedrooms: int      
    Bathrooms: int      
    Floors: int         
    Building_Age: int     
    Neighborhood: str       
    Property_Type: str      
    Garage: str         
    Garden: str
    Heating_Type: str
    Balcony: str
    Interior_Style: str
    View: str
    Materials: str
    Building_Status: str
 
    def convert_to_mlinput(self) -> "MLInput":
        """
        Convertit les données utilisateur en format ML (one-hot encoding)
        """
        mlinput = MLInput(

        Square_Meters=self.Square_Meters,
        Bedrooms=self.Bedrooms,
        Bathrooms=self.Bathrooms,
        Floors=self.Floors,
        Building_Age=self.Building_Age,

        Garage_Yes=self.Garage == "Oui",
        Garden_Yes=self.Garden == "Oui",

        Neighborhood_Chelsea=self.Neighborhood == "Chelsea",
        Neighborhood_Islington=self.Neighborhood == "Islington",
        Neighborhood_Kensington=self.Neighborhood == "Kensington",
        Neighborhood_Marylebone=self.Neighborhood == "Marylebone",
        Neighborhood_Notting_Hill=self.Neighborhood == "Notting Hill",
        Neighborhood_Shoreditch=self.Neighborhood == "Shoreditch",
        Neighborhood_Soho=self.Neighborhood == "Soho",
        Neighborhood_Westminster=self.Neighborhood == "Westminster",
        Neighborhood_Greenwich=self.Neighborhood == "Greenwich",

        Property_Type_Detached_House=self.Property_Type == "Maison individuelle",
        Property_Type_Semi_Detached=self.Property_Type == "Maison jumelée",

        Heating_Type_Electric_Heating=self.Heating_Type == "Chauffage électrique",
        Heating_Type_Gas_Heating=self.Heating_Type == "Chauffage au gaz",
        Heating_Type_Underfloor_Heating=self.Heating_Type == "Chauffage au sol",

        Balcony_Low_Level_Balcony=self.Balcony == "Balcon bas",
        Balcony_No_Balcony=self.Balcony == "Sans balcon",

        Interior_Style_Industrial=self.Interior_Style == "Industriel",
        Interior_Style_Minimalist=self.Interior_Style == "Minimaliste",
        Interior_Style_Modern=self.Interior_Style == "Moderne",

        View_Garden=self.View == "Jardin",
        View_Park=self.View == "Parc",
        View_Sea=self.View == "Mer",
        View_Street=self.View == "Rue",

        Materials_Laminate_Flooring=self.Materials == "Sol stratifié",
        Materials_Marble=self.Materials == "Marbre",
        Materials_Wood=self.Materials == "Bois",

        Building_Status_Old=self.Building_Status == "Ancien",
        Building_Status_Renovated=self.Building_Status == "Rénové"
)
        return mlinput
 
 