import os
from dotenv import load_dotenv

load_dotenv()

POLE_EMPLOI_CLIENT_ID = os.getenv("POLE_EMPLOI_CLIENT_ID")
POLE_EMPLOI_CLIENT_SECRET = os.getenv("POLE_EMPLOI_CLIENT_SECRET")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configuration de l'API Pôle Emploi
POLE_EMPLOI_TOKEN_URL = "https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=partenaire"
POLE_EMPLOI_API_URL = "https://api.pole-emploi.io/partenaire/offresdemploi/v2/offres/search"

# Configuration du modèle OpenAI
OPENAI_MODEL = "gpt-3.5-turbo-16k-0613"
