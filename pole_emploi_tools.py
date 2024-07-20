from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field
import requests
from utils import obtenir_token
from config import POLE_EMPLOI_API_URL

class JobSearchInput(BaseModel):
    mot_cle: str = Field(..., description="Mot-clé pour la recherche d'emploi")
    lieu: Optional[str] = Field(None, description="Lieu de l'emploi")
    publiee_depuis: Optional[int] = Field(None, description="Nombre de jours depuis la publication")
    salaire_min: Optional[int] = Field(None, description="Salaire minimum annuel")
    type_contrat: Optional[str] = Field(None, description="Type de contrat")

class PoleEmploiJobSearchTool(BaseTool):
    name = "recherche_emploi_pole_emploi"
    description = "Recherche des offres d'emploi sur Pôle Emploi en fonction de divers critères"
    args_schema: Type[BaseModel] = JobSearchInput

    def _run(self, mot_cle: str, lieu: Optional[str] = None, publiee_depuis: Optional[int] = None, 
             salaire_min: Optional[int] = None, type_contrat: Optional[str] = None) -> str:
        try:
            token = obtenir_token()
            headers = {"Authorization": f"Bearer {token}"}
            params = {"motsCles": mot_cle}
            if lieu:
                params["commune"] = lieu
            if publiee_depuis:
                params["publieeDepuis"] = publiee_depuis
            if salaire_min:
                params["salaireMin"] = salaire_min
            if type_contrat:
                params["typeContrat"] = type_contrat

            response = requests.get(POLE_EMPLOI_API_URL, headers=headers, params=params)
            response.raise_for_status()
            offres = response.json().get('resultats', [])
            return self._format_offres(offres[:10])
        except Exception as e:
            return f"Une erreur s'est produite lors de la recherche d'emploi : {str(e)}"

    def _format_offres(self, offres):
        formatted_offres = []
        for offre in offres:
            formatted_offre = {
                "titre": offre.get("intitule"),
                "entreprise": offre.get("entreprise", {}).get("nom"),
                "lieu": offre.get("lieuTravail", {}).get("libelle"),
                "type_contrat": offre.get("typeContrat", {}).get("libelle"),
                "description": offre.get("description")[:200] + "..." if offre.get("description") else "Pas de description disponible",
                "url": offre.get("origineOffre", {}).get("urlOrigine")
            }
            formatted_offres.append(formatted_offre)
        return str(formatted_offres)  # Convert to string to ensure compatibility
