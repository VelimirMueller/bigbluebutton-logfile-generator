class CsvProcessor(): #CsvProcessor Klasse -> bereitet Daten für CsvWriter Klasse auf
    def __init__(self, data, structure):
        self.data = data #input
        self.structure = structure # in main.py wird die Struktur festgelegt (columns Bezeichner)
        self.data_array = [[],[],[],[],[],[],[],[]] # Anzal der Arrays hängt von der Anzahl der Spalten ab
        self.iterator = 1 # Zählvariable
        self.dictionary = {} # cache
        self.name = "CsvProcessor"

    def sort_data(self): # Diese Funktion sorgt dafür, dass die Logfile Abschnitte korrekt in die Arrays eingetragen werden
        try:
            for data in self.data: #string slicing zum Logfile unterteilen
                self.data_array[0].append(str(self.iterator)) # Zeilennummer
                self.data_array[1].append(data.split(" - ")[0].split(" ")[0]) #Datum
                self.data_array[2].append(data.split(" - ")[0].split(" ")[1]) #Uhrzeit
                self.data_array[3].append(data.split(" - ")[0].split(" ")[2]) #Zeitzone
                self.data_array[4].append(data.split("room")[1].split("\n")[0]) #Raumid
                if data.find("is joining") > -1:
                    self.data_array[5].append(data.split("Support: ")[1].split("room")[0].split("is joining")[0]) #username
                    self.data_array[6].append("login") #status
                elif data.find("has left") > -1:
                    self.data_array[5].append(data.split("Support: ")[1].split("room")[0].split("has left")[0]) #username
                    self.data_array[6].append("logout") #status
                else:
                    self.data_array[5].append(data.split("Support: ")[1].split("room")[0].split("is starting")[0])  # Raumstart
                    self.data_array[6].append("start room")  # status
                self.data_array[7].append(data.replace(";", " / ")) #komplettes Logfile
                self.iterator = self.iterator + 1 #Zählvariable ++
        except OSError as error:
            print("Error in class: " + self.name + " - sort_data() error. Please fix Code")
            print("error code: " + str(error))
        else:
            print("class: " + self.name + " function: - sort_data() executed succesfully")

    def room_dict(self): # erstellt ein dictionary - pro key (room_id) können beliebig viele [Logfileeinträge] zugeordnet sein
        try:
            for row in range(0, len(self.data_array[7])):
                if self.data_array[4][row] not in self.dictionary:
                    self.dictionary[self.data_array[4][row]] = [self.data_array[0][row] + ";" + self.data_array[1][row] + ";" +
                                    self.data_array[2][row] + ";" + self.data_array[3][row] + ";" +
                                    str(self.data_array[4][row]) + ";" + self.data_array[5][row] + ";" +
                                    self.data_array[6][row] + ";" + self.data_array[7][row]]
                else:
                    self.dictionary[self.data_array[4][row]].append([self.data_array[0][row] + ";" + self.data_array[1][row] + ";" +
                                    self.data_array[2][row] + ";" + self.data_array[3][row] + ";" +
                                    str(self.data_array[4][row]) + ";" + self.data_array[5][row] + ";" +
                                    self.data_array[6][row] + ";" + self.data_array[7][row]])
        except OSError as error:
            print("Error in class: " + self.name + " - room_dict() error. Please fix Code")
            print("error code: " + str(error))
        else:
            print("class: " + self.name + " function: - room_dict() executed succesfully")

    def start(self): #startet csv data processing - wird dann an csv_writer.py übergeben
        self.sort_data()
        self.room_dict()



