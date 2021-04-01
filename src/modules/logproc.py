class LogfileProcessor(): # Klasse für Logfile Processing
    def __init__(self, path, mode): # Konstrutor
        self.path = path
        self.mode = mode
        self.data_array = []
        self.sorted_data_array = []

    def reader(self): # Logfile auslesen
        with open(self.path, self.mode, encoding="utf-8") as logfile: #encoding für Umlaute
            for log in logfile:
                self.data_array.append(log)
        logfile.close()

    def sort(self): # Logfile nach relevanten Daten sortieren
        for entry in self.data_array:
            if entry.find("is joining") > -1 or entry.find("has left") > -1:
                self.sorted_data_array.append(entry)

    def return_data(self): # Kontrollfunktion
        for entry in self.sorted_data_array:
            print(entry)

    def start(self): # Startfunktion logfile data processing -> wird dann an csvproc.py übergeben
        self.reader()
        self.sort()
