"""
Fichier contenant la classe Metier.
Classe utilitaire du projet de simulation du programme de simulation de fonctionnement de magasin.

Contient les méthodes suivantes :
    1) Méthodes renvoyant le montant total par rayons et par secteurs d'activité.
    2) Méthode renvoyant le montant total d'un vendeur
    3) Méthode renvoyant le montant moyen d'achat par client

Pour toutes idées, remarques et signalements, veuillez contacter Victorien Guyon (M2 MMAA Univ-SMB) :
    -> Par mail : victorien.guyon@etu.univ-smb.fr
    -> Par discord : Victorien, sur le serveur Master MMAA USMB
"""

# Importation des classes :
from Client import Client
from Vendeur import Vendeur
from Produit import Produit
# from Rayon import Rayon
from SecteurActivite import SecteurActivite


# Classe Rayon (Provisoire) :
class Rayon:
    pass


# Classe Métier :
class Metier:
    """
    Classe utilitaire.
    Contient des méthodes de calculs de montant totaux ou moyens liés aux différentes entités du magasin.
    """

    @staticmethod
    def montant_total_Rayon(rayon: Rayon):
        """
        Renvoie le montant to total des produits dans un rayon.
        :param rayon: Rayon concerné.
        :return: Somme totale en euros des produits du rayon.
        """
        pass

    @staticmethod
    def montant_total_secteur(secteurActivite: SecteurActivite):
        """
        Donne le montant total des produits contenus dans tout un secteur.
        :param secteurActivite: Secteur en question.
        :return: Montant total en euros des produits du secteur.
        """
        pass

    @staticmethod
    def montant_total_vendeur(vendeur: Vendeur):
        """
        Renvoie le montant total vendu par un vendeur.
        :param vendeur: Le vendeur concerné.
        :return: Montant total de produit vendu par le vendeur, en euros.
        """
        pass

    @staticmethod
    def montant_moyen_achat_client(client: Client):
        """
        Renvoie le montant moyen d'achat par un client.
        :param client: Le client en question.
        :return: Le montant moyen d'achat du client en euros.
        """
        pass
