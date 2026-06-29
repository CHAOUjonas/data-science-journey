# Jour 5 - Manipulation JSON

import json

data = {
    "nom": "Jonas",
    "parcours": "Data Science",
    "semaine": 1
}

with open("exemple.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Fichier JSON créé.")
