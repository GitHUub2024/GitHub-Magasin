class Magasin:
    def __init__(self, number, secteurs):
        self.id = number
        self.secteurs = secteurs

    def __str__(self):
        chaine = "Magasin "+str(self.id)+" : {"
        for i in range(len(self.secteurs) -1):
            chaine += str(self.secteurs[i])+", "
        chaine += str(self.secteurs[-1]) + "}"
        return chaine

if __name__ == "__main__":
    m1 = Magasin(220802, ['natation', 'danse', 'foot'])
    print(m1)
