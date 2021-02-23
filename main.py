class Vehicule:

    def __init__(self, nom, q_essence):
        self.nom = nom
        self.essence = q_essence

    def se_deplacer(self):
        print("Le vehicule {} se déplace...".format(self.nom))


class Voiture(Vehicule):
    def __init__(self, nom_voiture, essence, puissance):
        Vehicule.__init__(self, nom_voiture, essence)
        self.puissance = puissance


voiture1 = Voiture("toyota supra", 90, 420)
voiture1.se_deplacer()
print(voiture1.puissance, "CH")
