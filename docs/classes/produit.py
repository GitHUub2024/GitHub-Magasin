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
        self.prixFournisseur = prixFournisseur
        self.prixHT = float(prixHT)
        self.stockInit = stockInit
        self.fournisseur = fournisseur
        
        # TVA donnée comme x%
        if type(TVA) == int: #10 ou 20
            self.TVA = float(TVA)
        elif type(TVA) == float: # 5.5 ou 0.2
            if TVA>1: # 5.5
                self.TVA = TVA
            else:  # 0.2
                self.TVA = TVA*100
        # Traiter le cas où le format n'est pas valide
        # else:
        #     print("nvjernv")
    
    def __str__(self):
        """
        Décrit brièvement le produit avce les informations principales

        Returns
        -------
        strOut : Description du nom, de l'id et des prix HT et TTC du produit

        """
        strOut = "Nom : {}\nId : {} \nPrix HT : {}€\nPrix TTC : {}€".format(self.nom, self.id, self.prixHT, self.prixTTC())
        return strOut
    
    def prixTTC(self):
        """
        Calcule le prix TTC du produit à partir du prix HT et de la TVA
        prix TTC = prix HT * (1 + TVA)

        Returns
        -------
        prixttc : prix TTC du produit

        """
        prixttc = self.prixHT*(1+self.TVA/100)
        return prixttc
    
    # def nombreVentes(self):
    #     return self.stock
    
    def montantMargeBrut(self):
        """
        calcule le montant de la marge brute dégagée par le produit
        (différence entre prix HT et prix fournisseur)

        Returns
        -------
        margeBrute : montant de la marge brute

        """
        if self.prixFournisseur == None:
            margeBrute = "Calcul impossible - prix fournisseur inconnu"
        else:
            margeBrute = str(self.prixHT - self.prixFournisseur)+"€"
        return margeBrute
    
    def variationPrix(self):
        """
        donne le pourcentage ajouté sur le produit par l'entreprise par rapport 
        au prix fournisseur

        Returns
        -------
        varPrix : % d'augmentation sur le produit après achat au fournisseur
        
        """
        if self.prixFournisseur == None:
            varPrix = "Calcul impossible - prix fournisseur inconnu"
        else:
            # calcul de la variation avec 2 décimales
            var = '%0.2f'%((self.prixHT - self.prixFournisseur)/self.prixFournisseur*100)
            
        return varPrix

    def margeBrute(self):
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
            marge = '%0.2f'%(diff / self.prixHT)
            
        return marge_brute


if __name__ == "__main__":
    prod1 = Produit('idProd','foot','ballon',100,15,20)

    print("Taux TVA = ", prod1.TVA, "%")
    print("Prix TTC = ", prod1.prixTTC(), "€")
    print("Montant de marge dégagée = ",prod1.montantMargeBrut())
    prod1.prixFournisseur = 10
    print("Montant de marge dégagée = ",prod1.montantMargeBrut())    
    print("% de marge dégagée = ",prod1.margeBrute())    
    print("variation prix = ",prod1.variationPrix())    