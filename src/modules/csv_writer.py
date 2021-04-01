import csv

class CsvWriter():
    def __init__(self, data_input):
        self.data_input = data_input # dictionary aus csvproc.py
        self.csv_writer_cache = [] #Kontrollstruktur
        self.csv_path = "../csv/" #Pfad des Outputs
        self.csv_mode = "w" #w=write, a=append, x=if doesnt exist ->, r=read

    def create_csv(self): #erstellt csv dateien - je key im dictionary wird eine Datei erstellt
        for key, value in self.data_input: #dictionary iterieren
            with open(self.csv_path + str(key) + ".csv", self.csv_mode, encoding="utf-8") as csvfile:
                for element in self.data_input:
                    for counter in range(0, len(element[1])): # für alle Logfileeinträge eines keys
                        if key in element[1][counter][0]: #nur logfileeinträge die zur room_id gehören
                            csvfile.write(str(element[1][counter][0])) #schreibvorgang
            csvfile.close()

    def start(self): #Startfunktion von CSV-writer
        self.create_csv()
