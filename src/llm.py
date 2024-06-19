import locale
# Définition de la fonction de préférence d'encodage de la locale pour toujours retourner "UTF-8"
locale.getpreferredencoding = lambda: "UTF-8"

# Importation de la classe HuggingFaceHub depuis le module langchain
from langchain import HuggingFaceHub

# Définition de la fonction llm qui crée et retourne un modèle de langage mixte
def llm(system_prompt):
    # Création d'une instance de la classe HuggingFaceHub avec les paramètres spécifiés
    llm_model = HuggingFaceHub(
        repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',  # Identifiant du dépôt du modèle
        model_kwargs={'max_length': 900, 'temperature': 0.1, 'return_full_text':False},  # Arguments du modèle (longueur maximale et température)
        system_prompt=system_prompt
    )
    # Retour de l'instance du modèle de langage mixte créée
    return llm_model
