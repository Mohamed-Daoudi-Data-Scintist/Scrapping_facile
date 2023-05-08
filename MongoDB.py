import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Se connecter à la base de données MongoDB
client = MongoClient('localhost', 27017)
db = client.scraper_projet
collection = db.Quote

# URL de la première page à scraper
url = 'http://quotes.toscrape.com/page/1/'

# Boucler à travers toutes les pages du site
nb_pages = int(input("Combien de page voulez-vous parcourir ? : "))
for i in range(1, nb_pages + 1):
    # Obtenir le contenu de la page
    response = requests.get(f'http://quotes.toscrape.com/page/{i}/')
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trouver toutes les citations sur la page
    quotes = soup.find_all('div', {'class': 'quote'})

    # Boucler à travers toutes les citations et insérer les données dans la collection
    for quote in quotes:
        text = quote.find('span', {'class': 'text'}).text
        author = quote.find('small', {'class': 'author'}).text
        tags = [tag.text for tag in quote.find_all('a', {'class': 'tag'})]

        # Créer un document avec les données de la citation
        quote_doc = {
            'text': text,
            'author': author,
            'tags': tags
        }

        # Insérer le document dans la collection
        collection.insert_one(quote_doc)