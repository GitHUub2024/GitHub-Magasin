from Vente import Vente
from Client import Client
from Produit import Produit
from Vendeur import Vendeur
from SecteurActivite import SecteurActivite
from Magasin import Magasin


def main():
    # Création de produits
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

    # Création d'un secteur d'activité
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

    # Ajouter l'achat au client et à l'historique des ventes du vendeur
    client1.ajouter_achat(vente1)
    vendeur1.ajoute_vente(vente1)

    # Affichage de l'historique des achats du client
    print(client1.afficher_historique_achats())

    # Affichage des informations du vendeur
    print(vendeur1.fiche_vendeur())

    # Affichage des informations du magasin
    print(magasin)

    # Affichage du stock après vente
    print(f"Stock du produit '{produit1.nom}': {produit1.stock} unités")
    print(f"Stock du produit '{produit2.nom}': {produit2.stock} unités")


if __name__ == "__main__":
    main()
