import requests
from bs4 import BeautifulSoup

# URL de la première page à scraper
url = 'http://quotes.toscrape.com/page/1/'

# Créer une liste vide pour stocker les données
data = []

nb=int(input("Combien de page voulez-vous parcourir ? : "))
i=0
# Boucler à travers toutes les pages du site
while i<nb :
    i = i + 1
    # Obtenir le contenu de la page
    response = requests.get(http://quotes.toscrape.com/page/str(i)/)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trouver toutes les citations sur la page
    quotes = soup.find_all('div', {'class': 'quote'})

    # Boucler à travers toutes les citations et extraire les données souhaitées
    for quote in quotes:
        text = quote.find('span', {'class': 'text'}).text
        author = quote.find('small', {'class': 'author'}).text
        tags = [tag.text for tag in quote.find_all('a', {'class': 'tag'})]
        data.append([text, author, tags])

# Afficher les données sous forme de tableau
for row in data:
    print(row)
