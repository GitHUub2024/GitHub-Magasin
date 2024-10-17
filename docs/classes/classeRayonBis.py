class Rayon:
    
    def __init__(self,id_rayon,nomRayon,nomSecteurActivite):
        self.id_rayon = id_rayon
        self.nomRayon = nomRayon
        self.nomSecteurActivite = nomSecteurActivite
        self.produit = {}
        
    def get_id_rayon(self):
        return self.id_rayon
    
    def set_id_rayon(self,new_id_rayon):
        self.id_rayon = new_id_rayon
        
    def get_nomRayon(self):
        return self.nomRayon
    
    def set_nomRayon(self,new_nomRayon):
        self.nomRayon = new_nomRayon
    
    def get_secteurActivite(self):
        return self.nomSecteurActivite
    
    def set_secteurActivite(self,new_nomSecteurActivite):
        self.nomSecteurActivite = new_nomSecteurActivite
        
    def get_produit(self):
        for i in self.produit.items():
            print(i)
            
    def get_liste_nomProduit(self):
        liste_produit = list(self.produit)
        return sorted(liste_produit)
    
    def get_nombre_nomProduit(self):
        liste_produit = list(self.produit)
        return len(liste_produit)
    
    def get_quantite_produit(self):
        somme = 0
        for val in self.produit.values():
            somme = somme + val
        return somme
    
    def get_appartientProduit(self,nomProduit):
        listeProduit = sorted( list(self.produit))
        return (nomProduit in listeProduit)
        
    def get_no_appartientProduit(self,nomProduit):
        listeProduit = sorted( list(self.produit))
        return (nomProduit not in listeProduit)
        
    def set_ajouterProduit(self,nomProduit, quantite = 1):
        self.produit[nomProduit] = quantite
        
    def set_supprimerProduit(self,nomProduit):
        self.produit.pop(nomProduit, None)
        return 1
    
    def get_disponible_produit(self,nomProduit):
        return self.produit[nomProduit]
