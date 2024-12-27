class Vente:
    def __init__(
        self,
        id_vente=None,
        produit=None,
        prix=None,
        vendeur=None,
        date=None,
        client=None
    ):
        self.id_vente = id_vente
        self.produit = produit
        self.prix = prix
        self.vendeur = vendeur
        self.date = date
        self.client = client
    