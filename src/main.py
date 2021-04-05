
import time # performance Messung
#module importieren
from src.modules.csv_processor.logproc import LogfileProcessor
from src.modules.csv_processor.csvproc import CsvProcessor
from src.modules.csv_processor.csv_writer import CsvWriter
from src.modules.pdf_processor.pdfproc import PdfProcessor
from src.modules.helpers.dir_maker import DirMaker
import sys
sys.path.insert(0, "../")

t0= time.process_time() # Messung der Zeit von Start


class Main():
    def __init__(self): #Setup
        self.setup_dir = DirMaker("../data/output/csv/", "../data/output/pdf/")
        self.lp = LogfileProcessor("../data/input/logfiles/production.small.log", "r")
        self.csv_structure = [["Row"], ["Date"], ["Time"], ["Timezone"], ["Room_name"],
                                  ["user_name"],
                                  ["status"], ["full_log \n"]]
        self.csv = CsvProcessor(self.lp.sorted_data_array, self.csv_structure)
        self.csv_writer = CsvWriter(self.csv.dictionary.items(), self.setup_dir.aktuellesDatum)
        self.pdf = PdfProcessor(self.csv.dictionary.items())

    def dir_setup(self):
        self.setup_dir.create_dir()

    def process_logfile(self): #Logfiles verarbeiten und sortieren und in array-list speichern
        self.lp.start()

    def process_csv(self): # aus array-list dictionary erstellen mit key: room_id und value: [logfiles][...][...]
        self.csv.start()

    def csv_creator(self): #erstellt csv Dateien - sortiert nach Raumnamen
        self.csv_writer.start()

    def pdf_creator(self):
        self.pdf.start()

    def start(self): # Hauptprogramm starten
        self.dir_setup()
        self.process_logfile()
        self.process_csv()
        self.csv_creator()
        self.pdf_creator()

x = Main()
x.start()
t1 = time.process_time() - t0
print("Time elapsed from program-start to end:PDF creation: ", t1 , "sec") # Messung der Zeit bis Ende mit Ausgabe



