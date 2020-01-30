import datetime
class bloc:
    def __init__(self,employe,avantmidi = False):
        self.employe = employe
        if avantmidi:
            self.hr_debut = datetime.time(hour=9,minute=00,second=00)
            self.hr_fin = datetime.time(hour=15,minute=30,second=00)
        else:
            self.hr_debut = datetime.time(hour=15, minute=30, second=00)
            self.hr_fin = datetime.time(hour=23, minute=00, second=00)

    def set_bloc(self,new_hr_debut,new_hr_fin):
        if new_hr_debut < new_hr_fin:
            self.hr_debut = new_hr_debut
            self.hr_fin = new_hr_fin

    def set_hr_debut(self,new_hr):
        self.hr_debut = new_hr

    def set_hr_fin(self,new_hr):
        self.hr_fin = new_hr

class employe:
    def __init__(self, nom, dispos):
        self.nom = nom
        self.dispos = dispos

class lieux:
    def __init__(self,nom,nb_blocs = 2):
        self.nom_lieu = nom
        self.horaire = []
        for i in range(nb_blocs):
            if i == 0:
                self.horaire[i] = bloc(avantmidi=True)
            else:
                self.horaire[i] = bloc()
