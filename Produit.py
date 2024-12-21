class Produit:
    def __init__(self, identifiant, 
                 rayon, 
                 nom,
                 stock,
                 prix_ht, 
                 tva,
                 prix_fournisseur = None,    # prix fournisseur pas forcément renseigné
                 fournisseur = None):       # fournisseur pas toujours connu
        self.id = identifiant
        self.rayon = rayon
        self.nom = nom
        self.prix_fournisseur = prix_fournisseur
        self.prix_ht = float(prix_ht)
        self.stock = stock
        self.fournisseur = fournisseur
        
        # TVA donnée comme x%
        if type(tva) == int: # 10 ou 20
            self.tva = float(tva)
        elif type(tva) == float: # 5.5 ou 0.2
            if tva > 1: # 5.5
                self.tva = tva
            else:  # 0.2
                self.tva = tva*100
    
    def __str__(self):
        """
        Décrit brièvement le produit avec les informations principales
        """
        str_out = f"Id : {self.id} \nNom : {self.nom}\nPrix HT : {self.prix_ht}€\nTaux TVA : {self.tva} %\nPrix TTC : {self.prix_ttc()}€"
        print(str_out)
    
    def set_prix_ht(self, nouveau_prix):
        self.prix_ht = nouveau_prix

    def set_prix_fournisseur(self, prix):
        self.prix_fournisseur = prix

    def set_nom_fournisseur(self, nom):
        self.fournisseur = nom

    def approvisionner(self, quantite):
        self.stock += quantite

    def prix_ttc(self):
        """
        Calcule le prix TTC du produit à partir du prix HT et de la TVA, avec deux décimales
        prix TTC = prix HT * (1 + TVA)
        """
        prix_ttc = '%0.2f'%(self.prix_ht*(1+self.tva/100))
        return prix_ttc
       
    def montant_marge_brut(self):
        """
        calcule le montant de la marge brute dégagée par le produit
        (différence entre prix HT et prix fournisseur)
        """
        if self.prix_fournisseur == None:
            marge_brute = "Calcul impossible : prix fournisseur inconnu"
        else:
            marge_brute = '%0.2f'%(self.prix_ht - self.prix_fournisseur)
        return marge_brute
    
    def pourcentage_marge_brute(self):
        """
        Donne le pourcentage de marge brute dégagée sur le prix HT du produit

        Returns
        -------
        marge_brute : % de marge brute sur prix HT

        """
        if self.prix_fournisseur == None:
            marge_brute = "Calcul impossible - prix fournisseur inconnu"
        else:
            # Calcul de l'écart entre prix HT et prix fournisseur
            diff = self.prix_ht - self.prix_fournisseur
            
            # calcul du % de marge brute au format x.xx
            marge_brute = '%0.2f'%(diff / self.prix_ht * 100)
            
        return marge_brute
    
    def pourcentage_entreprise(self):
        """
        donne le pourcentage ajouté sur le produit par l'entreprise par rapport au prix fournisseur
        """
        if self.prix_fournisseur == None:
            var_prix = "Calcul impossible : prix fournisseur inconnu"
        else:
            # calcul de la variation avec 2 décimales
            var_prix = '%0.2f'%((self.prix_ht - self.prix_fournisseur)/self.prix_fournisseur*100)
            
        return var_prix

    

if __name__ == "__main__":
    prod1 = Produit(identifiant='id_prod1',rayon='foot',nom='ballon',stock=100,prix_ht=15,tva=20)
    print("Taux TVA = ", prod1.tva, "%")
    print("Prix TTC = ", prod1.prix_ttc(), "€")
    print("Montant de marge dégagée = ",prod1.montant_marge_brut())

    prod1.set_prix_fournisseur(prix = 10)
    
    print("Montant de marge dégagée = ",prod1.montant_marge_brut(),"€")    
    print("% de marge dégagée = ",prod1.pourcentage_marge_brute(), "%")    
    print("% variation prix = ",prod1.pourcentage_entreprise(), "%")    

    prod2 = Produit(identifiant='id_prod2', rayon='montagne', nom='chaussures rando', stock=45, prix_ht=97.22, tva=20)
    prod2.__str__()