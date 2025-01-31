class Rayon:
    
    def __init__(self,id_rayon,nomRayon,nomSecteurActivite):
        """_Cette fonction permet la contruction du rayon_

        Args:
            id_rayon (_int_): _l'id est un entier sans signe permettant d'identifier de manière unique le rayon_
            nomRayon (_string_): _le parametre nomRayon permet de recevoir le nom du rayon_
            nomSecteurActivite (_string_): _le parametre nomSecteurActive permet de recevoir le nom du secteur d'activite de ce rayon_
        """
        self.id_rayon = id_rayon
        self.nomRayon = nomRayon
        self.nomSecteurActivite = nomSecteurActivite
        self.produit = {}
        
    def get_id_rayon(self):
        
        """_Cette fonction permet d'obtenir l'id du rayon_

        Returns:
            _int_: _la clé permettant l'identification du rayon_
        """
        return self.id_rayon
    
    def set_id_rayon(self,new_id_rayon):
        """_Cette fonction permet de changer ou modifier le nom du rayon_

        Args:
            new_id_rayon (_string_): _le parametre new_id_rayon permet de recevoir le nouveau nom du rayon_
        """
        self.id_rayon = new_id_rayon
        
    def get_nomRayon(self):
        """_Cette fonction permet d'obtenir le nom du rayon_

        Returns:
            _string_: _le nom du rayon_
        """
        return self.nomRayon
    
    def set_nomRayon(self,new_nomRayon):
        """_Cette fonction permet de changer ou de modifier le nom du rayon_

        Args:
            new_nomRayon (_string_): _le parametre new_nomRayon permet de recevoir le nouveau nom du rayon_
        """
        self.nomRayon = new_nomRayon
    
    def get_secteurActivite(self):
        """_Cette fonction permet d'obtenir le nom du secteur d'activite_

        Returns:
            _string_: _le nom du secteur d'activite du rayon_
        """
        return self.nomSecteurActivite
    
    def set_secteurActivite(self,new_nomSecteurActivite):
        """_Cette fonction fonction permet de changer ou de modifier le nom du secteur d'activite du rayon_

        Args:
            new_nomSecteurActivite (_string_): _le parametre new_nomSecteurActivite permet de recevoir le nouveau nom du secteur d'activite_
        """
        self.nomSecteurActivite = new_nomSecteurActivite
        
    def get_produit(self):
        """_Cette fonction permet de voir de maniere tres rapide les produits que contient ce rayon et leurs quantites.
            Elle les affiche sous forme de couple: (produit,quantite)_
        """
        for i in self.produit.items():
            print(i)
            
    def get_liste_nomProduit(self):
        """_Cette fonction permet de voir les produits du rayon_

        Returns:
            _list_: _liste ordonnee des produits du rayon_
        """
        liste_produit = list(self.produit)
        return sorted(liste_produit)
    
    def get_nombre_nomProduit(self):
        """_Cette fonction permet d'obtenir le nombre de nombre different de produit qui est different de la quantite de produit du rayon_

        Returns:
            _int_: _le nombre de nombre different de produit_
        """
        liste_produit = list(self.produit)
        return len(liste_produit)
    
    def get_quantite_produit(self):
        """_Cette fonction permet d'obtenir le nombre de produits ie la quantite totale de produits du rayon. Rappel: um produit peut avoir
        la valeur 15 comme sa quantite_

        Returns:
            _int_: _la quantite totale de produits_
        """
        somme = 0
        for val in self.produit.values():
            somme = somme + val
        return somme
    
    def get_appartientProduit(self,nomProduit):
        """_Cette fonction permet de savoir si un produit appartient au rayon ou non_

        Args:
            nomProduit (_string_): _le nom du produit à tester_

        Returns:
            _booleen_: _vrai ou faux_
        """
        listeProduit = sorted( list(self.produit))
        return (nomProduit in listeProduit)
        
    def get_no_appartientProduit(self,nomProduit):
        """_Cette fontion aussi permet de tester l'appartenance d'un produit au rayon en faisant le contraire de la fonction
        get_appartientProduit qui est non appartient_

        Args:
            nomProduit (_string_): _le nom du produit _ tester_

        Returns:
            _booleen_: _faux ou vrai_
        """
        listeProduit = sorted( list(self.produit))
        return (nomProduit not in listeProduit)
        
    def set_ajouterProduit(self,nomProduit, quantite = 1):
        """_Cette fonction permet d'ajouter un produit et sa quantite au rayon. A defaut de na pas donner la quantité, la fonction prend
        la valeur 1 comme sa quantite_

        Args:
            nomProduit (_string_): _le nom du produit à ajouter_
            quantite (int, optional): _la quantite du produit à ajouter_. Defaults to 1.
        """
        self.produit[nomProduit] = quantite
        
    def set_supprimerProduit(self,nomProduit):
        """_Cette fonction permet de supprimer un produit au rayon_

        Args:
            nomProduit (_sstring_): _le nom du produit à supprimer au rayon_

        Returns:
            _int_: _la valeur 1 pour confirmer la supprission du produit au rayon_
        """
        self.produit.pop(nomProduit, None)
        return 1
    
    def get_disponible_produit(self,nomProduit):
        """_Cette fonction permet d'obtenir la quantite restant pour un produit donne_

        Args:
            nomProduit (_string_): _le nom du produit_

        Returns:
            _int_: _la quantite du produit_
        """
        return self.produit[nomProduit]