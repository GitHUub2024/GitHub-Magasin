class SecteurActivite: 
    def __init__(self,nom,liste_rayons,liste_produits):
        self.nom = nom
        self.liste_rayons = liste_rayons
        self.liste_produits = liste_produits
    
    def __repr__(self):
        nom = self.nom
        liste_rayons = self.liste_rayons
        liste_produits = self.liste_produits
        noms_rayons = []
        noms_produits = []
        for ray in liste_rayons:
            noms_rayons.append(ray.nom)
        for prod in liste_produits:
            noms_produits.append(prod.nom)
        return "Il s'agit du secteur {}. Les rayons qui le composent sont {}. Les produits de ce secteur sont {}.".format(nom,noms_rayons,noms_produits)
    
    def ajouter_rayon(self,rayon):
        # Ajoute un rayon au secteur d'activité
        self.liste_rayons.append(rayon)

    def supprimer_rayon(self,nom_rayon):
        # Supprime un rayon du secteur
        for ray in self.liste_rayons:
            if ray.nomRayon == nom_rayon:
                self.liste_rayons.remove(ray)

        
    def ajouter_produit(self,produit):
        # Ajoute un produit au secteur
        self.liste_produis.append(produit)

    def supprimer_produit(self,nom_produit):
        # Supprime un produit du secteur
        for prod in self.liste_produit:
            if prod.nom == nom_produit:
                self.liste_produits.remove(prod)
        
    def prix_ttc_secteur(self):
        # Renvoie le prix toutes taxes comprises du secteur dans son intégralité
        res = 0
        for prod in self.liste_produits:
            res += prod.prix_ttc() * prod.stock
        return res
        
if __name__ == "__main__":
    secteur_foot = SecteurActivite(
        nom="Secteur Foot",
        liste_rayons=["ballons", "chaussures"],
        liste_produits=[produit1, produit2])
    secteur_foot.ajouter_produit(produit3)
    secteur_foot.supprimer_produit(produit1)
