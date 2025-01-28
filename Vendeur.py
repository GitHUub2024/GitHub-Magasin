class Vendeur:
    def __init__(
        self,
        nom=None,
        prenom=None,
        telephone=None,
        mail=None,
        date_prise_de_fonction=None,
        indice_grille_salaire=None,
        secteur=None,
        rayon_associe=None,
    ):

        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.mail = mail
        self.date_prise_de_fonction = date_prise_de_fonction
        self.indice_grille_salaire = indice_grille_salaire
        self.secteur = secteur
        self.rayon_associe = rayon_associe
        self.ventes = []

    def ajoute_vente(self, vente):
        self.ventes += [vente]

    def __repr__(self):
        details = (
            f"Prénom NOM : {self.prenom} {self.nom.upper()}\n"
            f"Téléphone : {self.telephone}\n"
            f"Mail : {self.mail}\n"
            f"Montant des ventes : {self.get_montant_ventes()}"
        )
        return details

    def __str__(self):
        return self.__repr__()

    def fiche_vendeur(self):
        return self.__repr__()

    def get_montant_ventes(self):
        return (
            sum(vente.prix_montant for vente in self.ventes) if len(self.ventes) != 0 else 0
        )


if __name__ == "__main__":
    michel = Vendeur(prenom="Michel", nom="Dumont")
    print(michel.fiche_vendeur())
