class AssistantEducationDirection:
    def __init__(self, prenom, lun_deb, lun_fin, mar_deb, mar_fin, mer_deb, mer_fin, jeu_deb, jeu_fin, ven_deb, ven_fin):
        self.prenom = prenom 
        self.lun_deb = lun_deb
        self.lun_fin = lun_fin
        self.mar_deb = mar_deb
        self.mar_fin = mar_fin
        self.mer_deb = mer_deb
        self.mer_fin = mer_fin
        self.jeu_deb = jeu_deb
        self.jeu_fin = jeu_fin
        self.ven_deb = ven_deb
        self.ven_fin = ven_fin

class Periode:
    def __init__(self, nom, deb, fin, priorites1, priorites2, priorites3):
        self.nom = nom
        self.deb = deb
        self.fin = fin
        self.priorites1 = priorites1
        self.priorites2 = priorites2
        self.priorites3 = priorites3

class Jour:
    def __init__(self,name):
        self.name = name
        if self.name == 'mercredi':
            self.accueil = Periode('Accueil', 8, 8.25, ['Hall', 'cour B toilettes', 'cour A toilettes', 'cour B centre'], ['cour B préau ou cour B panier de basket'], ['passerelle'])
            self.montee_des_eleves_matin = Periode('Montée des élèves matin', 8.25, 8.3333333333, ['couloirs BAT A', 'cour b + prépa étude', 'hall+prépa étude', 'couloirs BAT B'], ['passerelle'], [])
            self.m1 = Periode('M1', 8.3333333333, 9.25, [' AED référent.e Renfort étude Aide bureau Couloirs', 'étude 1', 'étude 2', 'salle de réflexion', 'Prépa devoirs heures de retenue de la journée + répartition fin de journée'],[],[])
            self.intercours1 = Periode('Intercours 1', 9.25, 9.3333333333, ['couloirs BAT A', 'couloirs BAT B, cour B + prépa étude', 'hall + prépa étude'], ['dedoublement couloirs BAT A', 'dedoublement couloirs BAT B', 'passerelle'], [])
            self.m2 = Periode('M2', 9.3333333333, 10.25, ['AED référent.e Renfort étude Aide bureau Couloirs', 'étude 1', 'étude 2', 'salle de réflexion', 'Prépa devoirs heures de retenue de la journée + répartition fin de journée'])
            self.recreationMatin = Periode('Récréation matin', 10.25, 10.5, ['Cour A toilettes', 'cour B centre', 'cour B Toilettes', 'cour B panier de basket'], ['cour B préau'], ['Hall'])
            self.montee_des_eleves_recreation = Periode('Montée des élèves récréation', 10.5, 10.5833333333, ['couloirs BAT A', 'couloirs BAT B', 'COUR B + prépa étude', 'Hall + prépa étude'], ['doubler couloir bat A', 'doubler couloirs bat B', 'passerelle'], [])
            self.m3 = Periode('M3', 10.5833333333, 11.5, ['étude 1', 'étude 2', 'salle de réflexion'], ['repas de 11h-11h30', 'repas de 11h-11h30', 'repas de 11h-11h30', 'repas de 11h-11h30'], [])
            self.intercours2 = Periode('Intercours 2', 11.5, 11.5833333333, ['couloirs BAT A', 'couloirs BAT B', 'cartablerie', 'hall', 'portail (mise en rang)'], ['doubler couloir bat A', 'doubler couloirs bat B', 'passerelle'], [])
            self.m4 = Periode('M4', 11.5833333333, 12.5, ['salle de réflexion', 'étude 1', 'étude 2', 'repas 12h'], [], [])
            self.intercours3 = Periode('Intercours 3', 12.5, 12.8333333333, ['portail porte jaune', 'portail (portail vert)', 'portail (porte jaune)', 'portail (porte jaune)'], [], [])
            self.pause_meridienne = Periode('Pause méridienne', 12.8333333333, 13.9166666666, ['file self', 'self', 'self renfort', 'toilettes cour B', 'cour B centre'], ['cour B préau '], [])
        else:
            self.accueil = Periode('Accueil', 8, 8.25, ['Hall', 'cour B toilettes', 'cour A toilettes', 'cour B centre'], ['cour B préau ou cour B panier de basket'], ['passerelle'])
            self.montee_des_eleves_matin = Periode('Montée des élèves matin', 8.25, 8.3333333333, ['couloirs BAT A', 'cour b + prépa étude', 'hall+prépa étude', 'couloirs BAT B'], ['passerelle'], [])
            self.m1 = Periode('M1', 8.3333333333, 9.25, [' AED référent.e Renfort étude Aide bureau Couloirs', 'étude 1', 'étude 2', 'salle de réflexion', 'Prépa devoirs heures de retenue de la journée + répartition fin de journée'],[],[])
            self.intercours1 = Periode('Intercours 1', 9.25, 9.3333333333, ['couloirs BAT A', 'couloirs BAT B, cour B + prépa étude', 'hall + prépa étude'], ['dedoublement couloirs BAT A', 'dedoublement couloirs BAT B', 'passerelle'], [])
            self.m2 = Periode('M2', 9.3333333333, 10.25, ['AED référent.e Renfort étude Aide bureau Couloirs', 'étude 1', 'étude 2', 'salle de réflexion', 'Prépa devoirs heures de retenue de la journée + répartition fin de journée'])
            self.recreationMatin = Periode('Récréation matin', 10.25, 10.5, ['Cour A toilettes', 'cour B centre', 'cour B Toilettes', 'cour B panier de basket'], ['cour B préau'], ['Hall'])
            self.montee_des_eleves_recreation = Periode('Montée des élèves récréation', 10.5, 10.5833333333, ['couloirs BAT A', 'couloirs BAT B', 'COUR B + prépa étude', 'Hall + prépa étude'], ['doubler couloir bat A', 'doubler couloirs bat B', 'passerelle'], [])
            self.m3 = Periode('M3', 10.5833333333, 11.5, ['étude 1', 'étude 2', 'salle de réflexion'], ['repas de 11h-11h30', 'repas de 11h-11h30', 'repas de 11h-11h30', 'repas de 11h-11h30'], [])
            self.intercours2 = Periode('Intercours 2', 11.5, 11.5833333333, ['couloirs BAT A', 'couloirs BAT B', 'cartablerie', 'hall', 'portail (mise en rang)'], ['doubler couloir bat A', 'doubler couloirs bat B', 'passerelle'], [])
            self.m4 = Periode('M4', 11.5833333333, 12.5, ['Aide Bureau = salle de réflexion', 'toilettes cour B', 'self', 'file self'], ['repas 11h45'], [])
            self.intercours3 = Periode('Intercours 3', 12.5, 12.8333333333, ['portail porte jaune', 'portail (mise en rang + cour A)', 'self', 'file self', 'cartablerie'], ['Cour B centre'], [])
            self.pause_meridienne = Periode('Pause méridienne', 12.8333333333, 13.9166666666, ['file self', 'self', 'self renfort', 'toilettes cour B', 'cour B centre'], ['cour B préau '], [])
            self.montee_des_eleves_midi = Periode('Montée des élèves midi', 13.9166666666, 14, ['ouloirs BAT A', 'couloirs BAT B', 'COUR B + prépa étude', 'Hall + prépa étude', 'cartablerie'], ['doubler couloir bat A', 'doubler couloirs bat B', 'passerelle'], [])
            self.s1 = Periode('S1', 14, 14.9166666666, ['étude 1', 'étude 2', 'salle de réflexion', 'cartablerie'], ['AED référent.e Renfort étude Aide bureau Couloirs', 'AED référent.e Renfort étude Aide bureau Couloirs', 'AED référent.e Renfort étude Aide bureau Couloirs'], [])
            self.intercours4 = Periode('Intercours 4', 14.9166666666, 15, ['couloirs BAT A', 'couloirs BAT B', 'cour B + prépa étude', 'hall + prépa étude'], ['dedoublement couloirs BAT A', 'dedoublement couloirs BAT B', 'passerelle'], [])
            self.s2 = Periode('S2', 15, 15.9166666666, ['étude 1', 'étude 2', 'salle de réflexion'], ['AED référent.e Renfort étude Aide bureau Couloirs', 'AED référent.e Renfort étude Aide bureau Couloirs', 'AED référent.e Renfort étude Aide bureau Couloirs'], [])
            self.recreationAprem = Periode('Récréation après-midi', 15.9166666666, 16.1666666666, ['Cour A toilettes', 'cour B centre', 'cour B Toilettes', 'portail (portail vert)', 'portail (porte jaune)', 'portail (mise en rang + cour A)'], [], [])
            self.intercours5 = Periode('Intercours 5', 16.1666666666, 16.25, ['couloirs BAT A', 'couloirs BAT B', 'hall + prépa heures de retenues'], ['dedoublement couloirs BAT A', 'dedoublement couloirs BAT B', 'passerelle'], [])
            self.s3 = Periode('S3', 16.25, 17.1666666666, ['heures de retenues', 'heures de retenues', 'salle de réflexion '], [], [])
            self.intercours6 = Periode('Intercours 6', 17.1666666666, 17.25, ['Couloirs', 'portail '], [], [])
            self.s4 = Periode('S4', 17.25, 18.1666666666, ['heures de retenue'], [], [])
            self.intercours7 = Periode('Intercours 7', 18.1666666666, 18.25, ['portail'], [''], [''])

