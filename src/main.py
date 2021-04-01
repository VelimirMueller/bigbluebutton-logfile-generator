
import time # performance Messung
from src.modules.logproc import LogfileProcessor
from src.modules.csvproc import CsvProcessor
from src.modules.csv_writer import CsvWriter

t0= time.process_time() # Messung der Zeit von Start


class Main():

    def __init__(self): #Setup
        self.lp = LogfileProcessor("../logfiles/production.log", "r")
        self.csv_structure = [["Zeilennummer"], ["Datum"], ["Uhrzeit"], ["Zeitzone"], ["Raumname"], ["Benutzername"],
                         ["Status"], ["Logfile_komplett \n"]]
        self.csv = CsvProcessor(self.lp.sorted_data_array, self.csv_structure)
        self.csv_writer = CsvWriter(self.csv.dictionary.items())

    def process_logfile(self): #Logfiles verarbeiten und sortieren und in array-list speichern
        self.lp.start()

    def process_csv(self): # aus array-list dictionary erstellen mit key: room_id und value: [logfiles][...][...]
        self.csv.start()

    def csv_creator(self): #erstellt csv Dateien - sortiert nach Raumnamen
        self.csv_writer.create_csv()

    def start(self): # Hauptprogramm starten
        self.process_logfile()
        self.process_csv()
        self.csv_creator()

x = Main() # neues Objekt initilisieren
x.start() # Hauptprogramm Startfunktion



t1 = time.process_time() - t0
print("Time elapsed: ", t1 , "sec") # Messung der Zeit bis Ende mit Ausgabe


