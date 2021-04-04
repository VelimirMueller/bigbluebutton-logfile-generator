class CsvWriter(): #CsvWriter Klasse -> erstelle CSVs
    def __init__(self, data_input, aktuellesDatum):
        self.aktuellesDatum = aktuellesDatum
        self.data_input = data_input # dictionary aus csvproc.py
        self.csv_writer_cache = [] #Kontrollstruktur
        self.csv_path = "../data/output/csv/" + str(self.aktuellesDatum) #Pfad des Outputs
        self.csv_mode = "w" #w=write, a=append, x=if doesnt exist ->, r=read
        self.name = "CsvWriter"

    def create_csv(self): #erstellt csv dateien - je key im dictionary wird eine Datei erstellt
        try:
            for key, value in self.data_input: #dictionary iterieren
                with open(self.csv_path + "/" + str(key) + ".csv", self.csv_mode, encoding="utf-8") as csvfile:
                    for element in self.data_input:
                        for counter in range(0, len(element[1])): # für alle Logfileeinträge eines keys
                            if key in element[1][counter][0]: #nur logfileeinträge die zur room_id gehören
                                csvfile.write(str(element[1][counter][0])) #schreibvorgang
                csvfile.close()
        except:
            print("Error in class: " + self.name + " - create_csv() error. Please fix Code")
        else:
            print("class: " + self.name + " function: - create_csv() executed succesfully")

    def start(self): #Startfunktion von CSV-writer
        self.create_csv()
