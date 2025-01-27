from Vente import Vente
from Client import Client
from Produit import Produit
from Vendeur import Vendeur
from SecteurActivite import SecteurActivite
from Magasin import Magasin


# ====================
# ALGORITHME PRINCIPAL
# ====================


# 1) On initialise un magasin avec différents secteur d'activité et plusieurs produits par secteurs
# 2) On initialise des clients, des vendeurs et un responsable par secteur d'activité
# 3) On effectue des ventes et on met à jour les statistiques des vendeurs ainsi que le stock des produits vendus
# 4) On effectue des commandes sur le site internet
# 5) On met à jour le catalogue internet après que les commandes aient été effectuées
# 6) On calcul le prix moyen des articles du magasin
# 7) On calcul le bénéfice du magasin (marge brute)


def main():
    # Création de divers produits
    produit1 = Produit(
        identifiant="id_prod1",
        rayon="foot",
        nom="Ballon",
        stock=100,
        prix_ht=15,
        tva=20,
    )
    produit2 = Produit(
        identifiant="id_prod2",
        rayon="rando",
        nom="Chaussures",
        stock=45,
        prix_ht=97.22,
        tva=20,
    )

    # Création d'un secteur d'activité auxquel lier les produits
    secteur_foot = SecteurActivite(
        nom="Secteur Foot",
        liste_rayons=["ballons", "chaussures"],
        liste_produits=[produit1, produit2],
    )

    # Création d'un magasin et ajout des secteurs d'activité
    magasin = Magasin(nom="Décathlon", secteurs_act=[secteur_foot])

    # Création de clients
    client1 = Client(
        id_client=1,
        nom="Dupont",
        prenom="Pierre",
        email="pierre.dupont@email.com",
        telephone=123456789,
    )
    client2 = Client(
        id_client=2,
        nom="Martin",
        prenom="Lucie",
        email="lucie.martin@email.com",
        telephone=987654321,
    )

    # Création de vendeurs
    vendeur1 = Vendeur(
        prenom="Michel",
        nom="Dumont",
        telephone="0102030405",
        mail="michel.dumont@email.com",
        secteur=secteur_foot,
    )

    # Simuler une vente
    vente1 = Vente(
        id_vente=1,
        produits=[produit1, produit2],
        prix_total=produit1.prix_ttc() * 2 + produit2.prix_ttc() * 1,
        vendeur=vendeur1,
        client=client1,
    )

    # Affichage des informations du magasin
    print(magasin)

    # Affichage des informations du vendeur
    print(vendeur1.fiche_vendeur())

    # Affichage du stock après vente
    print(f"Stock du produit '{produit1.nom}': {produit1.stock} unités")
    print(f"Stock du produit '{produit2.nom}': {produit2.stock} unités")


if __name__ == "__main__":
    main()
