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
        prix_ht=15.0,
        tva=20,
    )
    produit2 = Produit(
        identifiant="id_prod2",
        rayon="rando",
        nom="Chaussures",
        stock=80,
        prix_ht=97.22,
        tva=20,
    )

    produit3 = Produit(
        identifiant="id_prod3",
        rayon="maillot",
        nom="Jammer",
        stock=50,
        prix_ht=84.95,
        tva=20,
    )

    produit4 = Produit(
        identifiant="id_prod4",
        rayon="bonnet",
        nom="Bonnet de bain",
        stock=300,
        prix_ht=10.50,
        tva=20,
    )

    # Création d'un secteur d'activité auxquel lier les produits
    secteur_foot = SecteurActivite(
        nom="Secteur Foot",
        liste_rayons=["ballons", "chaussures"],
        liste_produits=[produit1, produit2],
    )

    secteur_natation = SecteurActivite(
        nom="Secteur Natation",
        liste_rayons=["bonnets", "maillots"],
        liste_produits=[produit3, produit4],
    )
    # Création d'un magasin et ajout des secteurs d'activité
    magasin = Magasin(nom="Décathlon", secteurs_act=[secteur_foot, secteur_natation])

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

    vendeur2 = Vendeur(
        prenom="Tatiana",
        nom="Malibou",
        telephone="0104070809",
        mail="tatiana.malibou@email.com",
        secteur=secteur_natation,
    )

    # On simule une vente
    vente1 = Vente(
        id_vente=1,
        produits=[produit1, produit2],
        prix_total=float(produit1.prix_ttc()) * 2 + float(produit2.prix_ttc()) * 1,
        vendeur=vendeur1,
        date="01-03-2024",
        client=client1,
    )

    vente2 = Vente(
        id_vente=2,
        produits=[produit3, produit4],
        prix_total=float(produit3.prix_ttc()) * 3 + float(produit4.prix_ttc()) * 3,
        vendeur=vendeur1,
        date="05-07-2024",
        client=client1,
    )

    vendeur1.ajoute_vente(vente1)
    vendeur2.ajoute_vente(vente2)

    # On affiche les informations du magasin
    print(f"====== Informations du magasin ======\n{magasin}")

    # On affiche les informations des vendeurs
    print(f"====== Fiche vendeur1 ======\n{vendeur1.fiche_vendeur()}")
    print(f"====== Fiche vendeur2 ======\n{vendeur2.fiche_vendeur()}")

    # On affiche le stock après vente
    print("====== Affichage des stocks après vente ======")
    print(f"Stock du produit '{produit1.nom}': {produit1.stock} unités")
    print(f"Stock du produit '{produit2.nom}': {produit2.stock} unités")
    print(f"Stock du produit '{produit3.nom}': {produit3.stock} unités")
    print(f"Stock du produit '{produit4.nom}': {produit4.stock} unités")

    # Marge du magasin
    print(
        f"====== Marge brut du magasin ======\n{sum(vendeur.get_montant_ventes() for vendeur in [vendeur1,vendeur2])}€"
    )


if __name__ == "__main__":
    main()
