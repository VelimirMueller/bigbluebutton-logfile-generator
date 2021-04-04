class LogfileProcessor(): # LogfileProcessor Klasse -> bereitet Daten für CsvProcessor Klasse auf
    def __init__(self, path, mode): # Konstrutor
        self.path = path
        self.mode = mode
        self.data_array = []
        self.sorted_data_array = []
        self.name = "LogfileProcessor"

    def reader(self): # Logfile auslesen
        try:
            with open(self.path, self.mode, encoding="utf-8") as logfile:  # encoding für Umlaute
                for log in logfile:
                    self.data_array.append(log)
            logfile.close()
        except:
            print("Error in class: " + self.name + " - reader() error. Please fix Code")
        else:
            print("class: " + self.name + " function: reader()-executed succesfully")

    def sort(self): # Logfile nach relevanten Daten sortieren
        try:
            for entry in self.data_array:
                if entry.find("is joining") > -1 or entry.find("has left") > -1 or entry.find("is starting") > -1:
                    self.sorted_data_array.append(entry)
        except:
            print("Error in class: " + self.name + " - sort() error. Please fix Code")
        else:
            print("class: " + self.name + " function: sort() executed succesfully")

    def return_data(self): # Kontrollfunktion
        try:
            for entry in self.sorted_data_array:
                print(entry)
        except:
            print("Error in class: " + self.name + " - return_data() error. Please fix Code")
        else:
            print("class: " + self.name + " function: - return_data() executed succesfully")

    def start(self): # Startfunktion logfile data processing -> wird dann an csvproc.py übergeben
        self.reader()
        self.sort()
