import random

class Eleve:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.liste_evitement = []
        self.liste_favorise = []
        self.devant = False
        self.derriere = False
        self.seul = False
    def mettre_devant(self):
        self.devant = True
    def ne_plus_mettre_devant(self):
        self.devant = False
    def mettre_derriere(self):
        self.derriere = True
    def ne_plus_mettre_derriere(self):
        self.derriere = False
    def mettre_seul(self):
        self.seul = True
    def ne_plus_mettre_seul(self):
        self.seul = False
    def eviter(self, eleve):
        self.liste_evitement.append(eleve)
    def favoriser(self, eleve):
        self.liste_favorises.append(eleve)

class Classe:
    def __init__(self, nom, eleves):
        self.nom = nom
        self.eleves = eleves
    def ajouter(self, eleve):
        self.eleves.append(eleve)
    def eleve(self, nom, prenom):
        trouve = False
        n = 0
        while not trouve and n < len(self.eleves):
            if self.eleves[n].prenom == prenom:
                if self.eleves[n].nom == nom:
                    trouve = True
                else:
                    n = n + 1
            else:
                n = n + 1
        return(self.eleves[n])
    def separer(self, nom1, prenom1, nom2, prenom2):
        self.eleve(nom1, prenom1).liste_evitement.append(self.eleve(nom2, prenom2))
        self.eleve(nom2, prenom2).liste_evitement.append(self.eleve(nom1, prenom1))
    def rassembler(self, nom1, prenom1, nom2, prenom2):
        self.eleve(nom1, prenom1).liste_favorise.append(self.eleve(nom2, prenom2))
        self.eleve(nom2, prenom2).liste_favorise.append(self.eleve(nom1, prenom1))
    def mettre_seul(self, nom, prenom):
        self.eleve(nom, prenom).mettre_seul()
    def ne_plus_mettre_seul(self, nom, prenom):
        self.eleve(nom, prenom).ne_plus_mettre_seul()
    def mettre_devant(self, nom, prenom):
        self.eleve(nom, prenom).mettre_devant()
    def ne_plus_mettre_devant(self, nom, prenom):
        self.eleve(nom, prenom).ne_plus_mettre_devant()
    def mettre_derriere(self, nom, prenom):
        self.eleve(nom, prenom).mettre_derriere()
    def ne_plus_mettre_derriere(self, nom, prenom):
        self.eleve(nom, prenom).ne_plus_mettre_derriere()

class Salle():
    def __init__(self, nom, nb_lignes, nb_colonnes):
        self.nom = nom
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes

class Plan():
    # Le plan est vu du fond de la classe, du point de vue élève
    def __init__(self, classe, salle):
        self.classe = classe
        self.salle = salle
        self.plan = []
        for i in range(self.salle.nb_lignes):
            self.plan.append([])
            for j in range(self.salle.nb_colonnes):
                self.plan[i].append(Eleve('X', 'X'))
        self.aleatoire()
    def montrer(self):
        for i in range(self.salle.nb_lignes):
            ligne_a_afficher = ''
            for j in range(self.salle.nb_colonnes):
                ligne_a_afficher = ligne_a_afficher + self.plan[i][j].prenom + ' '
            print(ligne_a_afficher)
    def reinitialiser(self):
        for i in range(self.salle.nb_lignes):
            self.plan.append([])
            for j in range(self.salle.nb_colonnes):
                self.plan[i].append(Eleve('X', 'X'))
    def aleatoire(self):
        eleves_non_places = random.sample(self.classe.eleves, len(self.classe.eleves))
        i = 0
        j = 0
        while len(eleves_non_places) != 0:
            self.plan[i][j] = eleves_non_places[0]
            del(eleves_non_places[0])
            j = j + 1
            if j >= self.salle.nb_colonnes:
                i = i + 1
                j = 0
    def position(self, eleve):
        i = 0
        j = 0
        while self.plan[i][j] != eleve and i < self.salle.nb_lignes:
            while self.plan[i][j % self.salle.nb_colonnes] != eleve and j < self.salle.nb_colonnes:
                j = j + 1
            if j >= self.salle.nb_colonnes:
                j = 0
                i = i + 1
        return(i,j)
    def evaluation(self):
        note = 0
        note_maximale = 0
        for eleve in self.classe.eleves:
            if eleve.devant:
                note_maximale = note_maximale + 1
                if self.position(eleve)[0] == 0:
                    note = note + 1
                else:
                    print(eleve.prenom + eleve.nom + ' n est pas devant.')
            if eleve.derriere:
                note_maximale = note_maximale + 1
                if self.position(eleve)[0] == (self.salle.nb_lignes - 1):
                    note = note + 1
                else:
                    print(eleve.prenom + eleve.nom + ' n est pas derriere.')
            for autre_eleve in eleve.liste_evitement:
                note_maximale = note_maximale + 1
                oups = False
                i_eleve, j_eleve = self.position(eleve)
                for i in range(i_eleve - 1, i_eleve + 2):
                    for j in range(j_eleve - 1, j_eleve + 2):
                        if not (i < 0 or j < 0 or i >= self.salle.nb_lignes or j >= self.salle.nb_colonnes):
                            if self.plan[i][j] == autre_eleve:
                                print(eleve.nom + eleve.prenom + ' et ' + autre_eleve.nom + autre_eleve.prenom + ' ne sont pas separe.e.s.')
                                oups = True
                if not oups:
                    note = note + 1
            for autre_eleve in eleve.liste_favorise:
                note_maximale = note_maximale + 1
                c_bon = False
                i_eleve, j_eleve = self.position(eleve)
                for i in range(i_eleve - 1, i_eleve + 2):
                    for j in range(j_eleve - 1, j_eleve + 2):
                        if not (i < 0 or j < 0 or i >= self.salle.nb_lignes or j >= self.salle.nb_colonnes):
                            if self.plan[i][j] == autre_eleve:
                                c_bon = True
                if c_bon:
                    note = note + 1
                else:
                    print(eleve.nom + eleve.prenom + ' et ' + autre_eleve.nom + autre_eleve.prenom + ' ne sont pas reuni.e.s.')
        return(note / note_maximale)
    def permutation_benef(self):
        evaluation_initiale = self.evaluation()
        eleve1 = random.choice(self.classe.eleves)
        eleve2 = random.choice(self.classe.eleves)
        while eleve1 == eleve2:
            eleve2 = random.choice(self.classe.eleves)
        i1, j1 = self.position(eleve1)
        i2, j2 = self.position(eleve2)
        self.plan[i1][j1] = eleve2
        self.plan[i2][j2] = eleve1
        if self.evaluation() < evaluation_initiale:
            self.plan[i1][j1] = eleve1
            self.plan[i2][j2] = eleve2


### SALLES

salle_B22 = Salle('B22', 4, 6)
salle_les_pins = Salle('Les Pins', 5, 6)
salle_23 = Salle('23', 4, 8)

### 6F
sixiemeF = Classe(
    '6F', [
        Eleve('A', 'Adam'),
        Eleve('B', 'Amina'),
        Eleve('B', 'Helycia'),
        Eleve('B', 'Lyna'),
        Eleve('B', 'Ilyes'),

    ]
)

### 6BCD4
sixiemeBCD = Classe('6BCD', [
    Eleve('A','Sebyl'),
    Eleve('A', 'Merwan'),
    Eleve('A', 'Hafsa'),
    Eleve('A', 'Elton'),
    Eleve('B', 'Amena'),
    Eleve('B', 'Christenvie'),
    Eleve('E', 'Inaya'),
    Eleve('K', 'Adam'),
    Eleve('L', 'Omar'),
    Eleve('M', 'Ilane'),
    Eleve('M', 'Nour'),
    Eleve('S', 'Infi'),
    Eleve('T', 'Alseny'),
    Eleve('W', 'Lea'),
    Eleve('Z', 'Adam')
]
)

sixiemeBCD.separer('A', 'Sebyl', 'W', 'Lea')
sixiemeBCD.separer('A', 'Sebyl', 'A', 'Hafsa')
sixiemeBCD.separer('A', 'Hafsa', 'W', 'Lea')
sixiemeBCD.separer('A', 'Sebyl', 'B', 'Christenvie')
sixiemeBCD.separer('A', 'Hafsa', 'B', 'Christenvie')
sixiemeBCD.separer('A', 'Elton', 'A', 'Merwan')
sixiemeBCD.mettre_devant('B', 'Christenvie')
sixiemeBCD.mettre_devant('Z', 'Adam')
sixiemeBCD.mettre_devant('T', 'Alseny')
sixiemeBCD.mettre_devant('E', 'Inaya')
sixiemeBCD.rassembler('S', 'Infi', 'B', 'Amena')

plan_6BCD = Plan(sixiemeBCD, salle_B22)

plan_6BCD.montrer()

print(plan_6BCD.evaluation())

while(plan_6BCD.evaluation() != 1.0):
    plan_6BCD.permutation_benef()

plan_6BCD.montrer()

### 2023/2024 5E

cinqE = Classe('5E', [
    Eleve('A', 'Sohann'),
    Eleve('A', 'Lilian'),
    Eleve('A', 'Malak'),
    Eleve('B', 'Assia'),
    Eleve('B', 'Nolan'),
    Eleve('B', 'Milena'),
    Eleve('B', 'Mathys'),
    Eleve('C', 'Floriana'),
    Eleve('C', 'Lola'),
    Eleve('D', 'Meyson'),
    Eleve('F', 'Leo'),
    Eleve('G', 'Kylian'),
    Eleve('G', 'Ilhan'),
    Eleve('G', 'Lisa'),
    Eleve('H', 'Leo'),
    Eleve('K', 'Tiago'),
    Eleve('L', 'Victoria'),
    Eleve('M', 'Jihene'),
    Eleve('M', 'Maelys'),
    Eleve('M', 'Ana'),
    Eleve('O', 'Luca'),
    Eleve('P', 'Priscilia'),
    Eleve('P', 'Camille'),
    Eleve('R', 'Charlie'),
    Eleve('R', 'Linh'),
    Eleve('S', 'Louka'),
    Eleve('Y', 'Gaia')
])

cinqE.separer('G', 'Lisa', 'M', 'Jihene')
cinqE.separer('K', 'Tiago', 'A', 'Lilian')
cinqE.separer('C', 'Floriana', 'B', 'Assia')
cinqE.separer('B', 'Mathys', 'A', 'Sohann')
cinqE.rassembler('M', 'Ana', 'L', 'Victoria')
cinqE.rassembler('R', 'Charlie', 'P', 'Priscilia')
cinqE.mettre_derriere('G', 'Kylian')
cinqE.mettre_derriere('B', 'Milena')
cinqE.mettre_devant('K', 'Tiago')

'''plan = Plan(cinqE, salle_les_pins)

plan.montrer()

print(plan.evaluation())

while(plan.evaluation() != 1.0):
    plan.permutation_benef()

plan.montrer()'''