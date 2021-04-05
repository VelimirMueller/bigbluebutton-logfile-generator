from datetime import date
import os

class DirMaker():
    def __init__(self, csv_path, pfd_path):
        self.aktuellesDatum = date.today()
        self.csv_path = csv_path + str(self.aktuellesDatum)
        self.pdf_path = pfd_path + str(self.aktuellesDatum)
        self.paths =[self.csv_path, self.pdf_path]
        self.name = "DirMaker"

    def get_today(self): #Tagesdatum als string ausgeben
        return str(self.aktuellesDatum)

    def create_dir(self): #neues Verzeichnis erstellen - akt Datum: yyyy-mm-dd
        for path in self.paths:
            try:
                os.mkdir(path)
            except OSError as error:
                print("Creation of the directory %s failed" % path)
                print("error code: " + str(error))
            else:
                print("class: " + self.name + " function: - create_dir() executed succesfully. Created the directory %s " % path)