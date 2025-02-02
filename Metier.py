"""
Fichier contenant la classe Metier.
Classe utilitaire du projet de simulation du programme de simulation de fonctionnement de magasin.

Contient les méthodes suivantes :
    1) Méthodes renvoyant le montant total et moyen par rayons et par secteurs d'activité.
    2) Méthode renvoyant le montant moyen d'une vente d'un vendeur
    3) Méthode renvoyant le montant moyen d'achat par client

Pour toutes idées, remarques et signalements, veuillez contacter Victorien Guyon (M2 MMAA Univ-SMB) :
    -> Par mail : victorien.guyon@etu.univ-smb.fr
    -> Par discord : Victorien, sur le serveur Master MMAA USMB
"""

# Importation des classes :
from Client import Client
from Vendeur import Vendeur
from Rayon import Rayon
from SecteurActivite import SecteurActivite


# Classe Métier :
class Metier:
    """
    Classe utilitaire.
    Contient des méthodes de calculs de montant totaux ou moyens liés aux différentes entités du magasin.
    """

    @staticmethod
    def montant_total_rayon(rayon: Rayon, ttc: bool = True) -> float:
        """
        Renvoie le montant total des produits dans un rayon. Calcul avec les prix TTC par défault, HT
        si ttc = False.
        :param rayon: Rayon concerné.
        :param ttc: Indique le type de prix utilisé dans le calcul du montant. True pour TTC et False pour HT.
        :return: Somme totale en euros des produits du rayon.
        """
        if ttc:
            total = sum(prod.prix_ttc() * rayon.produit[prod] for prod in rayon.produit)
        else:
            total = sum(prod.prix_ht * rayon.produit[prod] for prod in rayon.produit)
        return total

    @staticmethod
    def montant_moyen_rayon(rayon: Rayon, ttc: bool = True) -> float:
        """
        Renvoie le montant moyen d'un produit dans un rayon. Calcul avec les prix TTC par défault, HT
        si ttc = False.
        :param rayon: Rayon en question.
        :param ttc: Indique le type de prix utilisé dans le calcul du montant. True pour TTC et False pour HT.
        :return: Montant moyen sur le rayon.
        """
        if ttc:
            total = sum(prod.prix_ttc() * rayon.produit[prod] for prod in rayon.produit)
        else:
            total = sum(prod.prix_ht * rayon.produit[prod] for prod in rayon.produit)
        return total / sum(rayon.produit[prod] for prod in rayon.produit)

    @staticmethod
    def montant_total_secteur_ht(secteurActivite: SecteurActivite) -> float:
        """
        Donne le montant total hors-taxes des produits contenus dans tout un secteur.
        :param secteurActivite: Secteur en question.
        :return: Montant total en euros des produits hors_taxes du secteur.
        """
        return sum(prod.prix_ht * prod.stock for prod in secteurActivite.liste_produits)

    @staticmethod
    def montant_moyen_secteur(secteurActivite: SecteurActivite, ttc: bool = True) -> float:
        """
        Renvoie le montant moyen d'un produit d'un secteur d'activité. Calcul avec les prix TTC par défault, HT
        si ttc = False.
        :param secteurActivite: Secteur en question.
        :param ttc: Indique le type de prix utilisé dans le calcul du montant. True pour TTC et False pour HT.
        :return: Montant moyen sur le secteur.
        """
        # Montant total secteur :
        if ttc:
            total = sum(prod.prix_ttc() * prod.stock for prod in secteurActivite.liste_produits)
        else:
            total = sum(prod.prix_ht * prod.stock for prod in secteurActivite.liste_produits)

        return total / sum(prod.stock for prod in secteurActivite.liste_produits)

    @staticmethod
    def montant_moyen_vendeur(vendeur: Vendeur) -> float:
        """
        Renvoie le montant moyen vendu par un vendeur.
        :param vendeur: Le vendeur concerné.
        :return: Montant moyen de produit vendu par le vendeur, en euros.
        """
        return sum(vente.prix_total for vente in vendeur.ventes) / len(vendeur.ventes)

    @staticmethod
    def montant_moyen_achat_client(client: Client) -> float:
        """
        Renvoie le montant moyen d'achat par un client.
        :param client: Le client en question.
        :return: Le montant moyen d'achat du client en euros.
        """
        return sum(vente.prix_total for vente in client.historique_achats) / len(client.historique_achats)
