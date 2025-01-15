from Vente import Vente

class Client:
    def __init__(self, id_client:int, nom:str, prenom:str, email:str, telephone:int):
        self.id_client = id_client  # Identifiant unique du client
        self.nom = nom              # Nom de famille
        self.prenom = prenom        # Prénom
        self.email = email          # Adresse email
        self.telephone = telephone  # Numéro de téléphone
        self.historique_achats = []  # Liste pour stocker l'historique des achats

    def ajouter_achat(self, vente:Vente):
        self.historique_achats+=[vente]

    def montant_moyen(self):
        nombre_achat=len(self.historique_achats)
        total=sum([self.historique_achats[k].prix for k in range(nombre_achat)])
        return total/nombre_achat

    def afficher_historique_achats(self):
        if not self.historique_achats:
            print(f"Aucun achat trouvé pour le client {self.nom} {self.prenom}.")
        else:
            print(f"Histoire des achats de {self.nom} {self.prenom}:")
            for achat in self.historique_achats:
                print(achat)

    def __str__(self):
        """Représentation en chaîne de caractères du client."""
        return f"{self.prenom} {self.nom} (Email: {self.email}, Téléphone: {self.telephone})"
