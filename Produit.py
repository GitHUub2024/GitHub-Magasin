class Produit:
    def __init__(self, identifiant, 
                 rayon, 
                 nom,
                 stockInit,
                 prixHT, 
                 TVA,
                 prixFournisseur = None,    # prix fournisseur pas forcément renseigné
                 fournisseur = None):       # fournisseur pas toujours connu
        self.id = identifiant
        self.rayon = rayon
        self.nom = nom
        self.prix_fournisseur = prixFournisseur
        self.prixHT = float(prixHT)
        self.stock_init = stockInit
        self.fournisseur = fournisseur
        
        # TVA donnée comme x%
        if type(TVA) == int: #10 ou 20
            self.TVA = float(TVA)
        elif type(TVA) == float: # 5.5 ou 0.2
            if TVA>1: # 5.5
                self.TVA = TVA
            else:  # 0.2
                self.TVA = TVA*100
    
    def __str__(self):
        """
        Décrit brièvement le produit avce les informations principales
        """
        strOut = "Nom : {}\nId : {} \nPrix HT : {}€\nPrix TTC : {}€".format(self.nom, self.id, self.prixHT, self.prixTTC())
        return strOut
    
    def prix_ttc(self):
        """
        Calcule le prix TTC du produit à partir du prix HT et de la TVA
        prix TTC = prix HT * (1 + TVA)
        """
        prixttc = self.prixHT*(1+self.TVA/100)
        return prixttc
    
    # def nombreVentes(self):
    #     return self.stock
    
    def montant_marge_brut(self):
        """
        calcule le montant de la marge brute dégagée par le produit
        (différence entre prix HT et prix fournisseur)
        """
        if self.prixFournisseur == None:
            margeBrute = "Calcul impossible - prix fournisseur inconnu"
        else:
            margeBrute = '%0.2f'%(self.prixHT - self.prixFournisseur)
        return margeBrute
    
    def variation_prix(self):
        """
        donne le pourcentage ajouté sur le produit par l'entreprise par rapport 
        au prix fournisseur
        """
        if self.prixFournisseur == None:
            varPrix = "Calcul impossible - prix fournisseur inconnu"
        else:
            # calcul de la variation avec 2 décimales
            varPrix = '%0.2f'%((self.prixHT - self.prixFournisseur)/self.prixFournisseur*100)
            
        return varPrix

    def marge_brute(self):
        """
        Donne le pourcentage de marge brute dégagée sur le prix HT du produit

        Returns
        -------
        marge_brute : % de marge brute sur prix HT

        """
        if self.prixFournisseur == None:
            marge_brute = "Calcul impossible - prix fournisseur inconnu"
        else:
            # Calcul de l'écart entre prix HT et prix fournisseur
            diff = self.prixHT - self.prixFournisseur
            
            # calcul du % de marge brute au format x.xx
            marge_brute = '%0.2f'%(diff / self.prixHT)
            
        return marge_brute


if __name__ == "__main__":
    prod1 = Produit('idProd','foot','ballon',100,15,20)

    print("Taux TVA = ", prod1.TVA, "%")
    print("Prix TTC = ", prod1.prix_ttc(), "€")
    print("Montant de marge dégagée = ",prod1.montant_marge_brut())
    prod1.prix_fournisseur = 10
    print("Montant de marge dégagée = ",prod1.montant_marge_brut(),"€")    
    print("% de marge dégagée = ",prod1.marge_brute(), "%")    
    print("% variation prix = ",prod1.variation_prix(), "%")    