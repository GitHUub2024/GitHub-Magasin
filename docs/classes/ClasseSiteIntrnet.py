class SiteInternet:
    def __init__(self, url, logo):
        self.url = url
        self.logo = logo  
        self.liste_produits = []
        self.clients_connectes = []
    
    def afficher_produits(self):
        for produit in self.liste_produits:
            print(f"Produit: {produit.nom}, Prix: {produit.prix}")
    
    def ajouter_produit(self, produit):
        self.liste_produits.append(produit)
    
    def ajouter_client(self, client):
        self.clients_connectes.append(client)

    def supprimer_produit(self, produit):
        self.liste_produits.remove(produit)
    
    def valider_commande(self, client):
        total = sum(produit.prix for produit in client.historique_achats)
        print(f"Commande validée pour {client.nom} {client.prenom}, Total: {total}€")
        return total
    
    def afficher_logo(self):
        print(f"Affichage du logo : {self.logo}")  
