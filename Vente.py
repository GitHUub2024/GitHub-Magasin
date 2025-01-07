class Vente:
    def __init__(
        self,
        id_vente=None,
        produits,
        prix_total=None,
        vendeur=None,
        date=None,
        client=None
    ):
        self.id_vente = id_vente
        self.produits = []
        self.prix_total = prix_total
        self.vendeur = vendeur
        self.date = date
        self.client = client
    
