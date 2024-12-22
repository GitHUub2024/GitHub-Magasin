# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 08:15:14 2024

@author: gressema
"""



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
        self.liste_rayons.append(rayon)
        
    def ajouter_produit(self,produit):
        self.liste_produis.append(produit)
        
    def prix_ttc_secteur(self):
        res = 0
        for prod in self.liste_produits:
            res += prod.prix_ttc() * prod.stock
        return res
        
if __name__ == "__main__":
    pass