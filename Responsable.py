from Vendeur import Vendeur


class Responsable(Vendeur):
    def __init__(
        self,
        nom=None,
        prenom=None,
        telephone=None,
        mail=None,
        date_prise_de_fonction=None,
        indice_grille_dalaire=None,
        secteur=None,
    ):
        super().__init__(
            nom,
            prenom,
            telephone,
            mail,
            date_prise_de_fonction,
            indice_grille_dalaire,
            secteur,
            rayon_associe=None,
        )

        del self.rayon_associe  # Le responsable s'occupe de tout les rayons


if __name__ == "__main__":
    michel = Responsable(prenom="Michel", nom="Dumont")
    print(michel.fiche_vendeur())
