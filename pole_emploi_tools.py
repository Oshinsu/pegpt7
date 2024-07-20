import requests
from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field

class JobSearchInput(BaseModel):
    keyword: str = Field(..., description="Mot-clé pour la recherche d'emploi")
    location: Optional[str] = Field(None, description="Lieu de l'emploi")

class TrainingSearchInput(BaseModel):
    keyword: str = Field(..., description="Mot-clé pour la recherche de formation")
    location: Optional[str] = Field(None, description="Lieu de la formation")

class PoleEmploiJobSearchTool(BaseTool):
    name = "pole_emploi_job_search"
    description = "Recherche des offres d'emploi sur Pôle Emploi"
    args_schema: Type[BaseModel] = JobSearchInput

    def _run(self, keyword: str, location: Optional[str] = None):
        access_token = self._get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        params = {
            "motsCles": keyword,
            "commune": location if location else None
        }
        response = requests.get("https://api.emploi-store.fr/partenaire/offresdemploi/v2/offres/search", 
                                headers=headers, params=params)
        return response.json()

    def _get_access_token(self):
        # Implémentez la logique pour obtenir le token d'accès ici
        pass

class PoleEmploiTrainingSearchTool(BaseTool):
    name = "pole_emploi_training_search"
    description = "Recherche des offres de formation sur Pôle Emploi"
    args_schema: Type[BaseModel] = TrainingSearchInput

    def _run(self, keyword: str, location: Optional[str] = None):
        access_token = self._get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        params = {
            "q": keyword,
            "region": location if location else None
        }
        response = requests.get("https://api.emploi-store.fr/partenaire/offresdemploi/v2/formations", 
                                headers=headers, params=params)
        return response.json()

    def _get_access_token(self):
        # Implémentez la logique pour obtenir le token d'accès ici
        pass
