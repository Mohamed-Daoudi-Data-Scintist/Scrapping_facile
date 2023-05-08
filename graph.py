import pymongo
import matplotlib.pyplot as plt

# Connexion à la base de données
client = pymongo.MongoClient('localhost', 27017)
db = client['scraper_projet']
collection = db['Quote']

# Compter le nombre d'occurrences de chaque tag
tags_count = {}
for quote in collection.find():
    for tag in quote['tags']:
        if tag in tags_count:
            tags_count[tag] += 1
        else:
            tags_count[tag] = 1

# Créer le graphique
plt.bar(tags_count.keys(), tags_count.values())
plt.title("Tags les plus utilisés")
plt.xlabel("Tags")
plt.ylabel("Nombre d'occurrences")
plt.xticks(rotation=90)
plt.show()
