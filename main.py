# Extraction des éléments depuis index.html avec BeautifulSoup
from bs4 import BeautifulSoup

with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# 1. Titre de la page
titre = soup.title.string
print(titre)

# 2. Titre principal (h1)
h1 = soup.find(id="titre").string
print(h1)

# 3. Extraction des informations sur les produits
produits = []
products = soup.find_all('li', class_="product")
for product in products:
    nom = product.find('h2').string
    prix_produit = product.find('p', class_='price').string
    paragraphes = product.find_all('p')
    description = paragraphes[1].string

    # Stockage dans une liste de dictionnaires
    infos_produits = {
        'nom': nom,
        'prix': prix_produit,
        'description': description
    }
    produits.append(infos_produits)

# 4. Nettoyage du prix — on garde que les chiffres (ex: "Prix: 10€" → 10)
for product in produits:
    prix = product['prix']
    prix_nettoye = ''.join(filter(str.isdigit, prix))
    product['prix'] = float(prix_nettoye)

# 5. Conversion en dollars (taux : 1€ = 1.2$)
for product in produits:
    prix_dollars = product['prix'] * 1.2
    product['prix'] = f"{prix_dollars:.2f} $"

# 6. Affichage des produits
for product in produits:
    print(f"Nom: {product['nom']}")
    print(f"Prix: {product['prix']}")
    print(f"Description: {product['description']}")
    print("-" * 20)
