from SecteurActivite import SecteurActivite


class Magasin:
    def __init__(self, nom, secteurs_act):
        self.nom = nom  # chaîne de caractères
        self.secteurs = secteurs_act  # liste de SecteurActivite

    def __str__(self):
        chaine = self.nom + " : {"
        for i in range(len(self.secteurs) - 1):
            chaine += str(self.secteurs[i].nom) + ", "
        chaine += str(self.secteurs[-1].nom) + "}"
        return chaine


if __name__ == "__main__":
    secteur_natation = SecteurActivite(
        nom="natation", liste_rayons=[], liste_produits=[]
    )
    secteur_danse = SecteurActivite(nom="danse", liste_rayons=[], liste_produits=[])
    secteur_foot = SecteurActivite(nom="foot", liste_rayons=[], liste_produits=[])
    m1 = Magasin("Décathlon", [secteur_natation, secteur_danse, secteur_foot])
    print(m1)
