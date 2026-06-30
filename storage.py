import json
import os

#----------------------------------------------------------------
# Funções

# - carregar pesos
pesos_file = "data/pesos.json"
def load_pesos():
    if os.path.exists(pesos_file):
        try:
            with open(pesos_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Erro ao carregar os pesos. Iniciando com uma lista vazia.")
            return []
    return []

# - salvar pesos
def save_pesos(pesos):
    os.makedirs("data", exist_ok=True)
    with open(pesos_file, "w", encoding="utf-8") as f:
        json.dump(pesos, f, indent=4, ensure_ascii=False)

# - carregar profile
profile_file = "data/profile.json"
def load_profile():
    if os.path.exists(profile_file):
        try:
            with open(profile_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except(json.JSONDecodeError, FileNotFoundError):
            print("Erro ao carregar o perfil. Iniciando com um perfil vazio.")
            return {}
    return {}

def save_profile(profile):
    os.makedirs("data", exist_ok=True)
    with open(profile_file, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4, ensure_ascii=False)