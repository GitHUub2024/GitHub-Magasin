class Magasin:
    def __init__(self, nom, secteurs_act):
        self.nom = nom  # chaîne de caractères
        self.secteurs = secteurs_act  # liste de SecteurActivite

    def __str__(self):
        chaine = self.nom + " : {"
        for i in range(len(self.secteurs) - 1):
            chaine += str(self.secteurs[i]) + ", "
        chaine += str(self.secteurs[-1]) + "}"
        return chaine


if __name__ == "__main__":
    m1 = Magasin("Décathlon", ["natation", "danse", "foot"])
    print(m1)
