from reportlab.lib.pagesizes import LETTER #Seitengröße importieren
from reportlab.lib.units import inch #inch importieren
from reportlab.pdfgen.canvas import Canvas #zeichenfläche erstellen
from reportlab.pdfbase import pdfmetrics #format pdf
from reportlab.pdfbase.cidfonts import UnicodeCIDFont #zeichensatz
from datetime import date

class PdfProcessor(): #PdfProcessor Klasse -> schreibt pdf Dateien
    def __init__(self, input_data):
        self.input_data = input_data
        self.pdf_path = "../data/output/pdf/"  # Pfad des Outputs
        self.pdf_mode = "w"
        self.counter = 0
        self.replab = pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3')) #alle Sonderzeichen drucken
        self.aktuellesDatum = date.today()
        self.name = "PdfProcessor"
        self.headline = "TEILNAHMELISTE"  # Überschrift
        self.start_time = "Startzeit:"  # Erste Zeile: Startzeit des Raums
        self.len_counter = 0

    def create_new_pdf(self):
        try:
            for key, value in self.input_data:
                with open(self.pdf_path + str(self.aktuellesDatum) + "/" + str(key) + ".pdf", self.pdf_mode, encoding="utf-8") as pdffile: #neues PDF erstellen mit RaumID als Dateinamen
                    self.replab
                    self.canvas = Canvas(self.pdf_path + "/" + str(self.aktuellesDatum) + "/" + str(key) + ".pdf", pagesize=LETTER) #in neues PDF
                    self.canvas.setFont("HeiseiMin-W3", 6)
                    self.headline
                    self.start_time
                    self.len_counter
                    self.cache = [[], [], []]
                    self.new_counter = self.counter  # neue Datei, neuer iterator
                    self.canvas.drawString(4 * inch, (10.5 - self.new_counter) * inch, self.headline) # in PDF schreiben/zeichnen
                    self.canvas.drawString(1 * inch, (10.25 - self.new_counter) * inch, self.start_time) # in PDF schreiben/zeichnenq

                    for val in value:
                        if self.len_counter > 0 and (self.len_counter % 33) == 0 > -1: # alle 35 Zeilen eine neue Seite anfangen
                            if val[0].find("start room") > -1:
                                self.canvas.setFont("HeiseiMin-W3", 6)  # utf-8 Schriftart festlegen
                                self.canvas.drawString(0.1 * inch, (10 - self.new_counter) * inch, str(val)) # in PDF schreiben/zeichnen
                                self.new_counter = 0 #neue Seite -> reset new_counter damit neue Zeilen in oberster Zeile Anfangen
                                self.canvas.showPage() # neue Seite Schreiben
                                self.new_counter += 0.25
                                self.len_counter += 1
                        elif val[0].find("start room") > -1:
                            self.canvas.setFont("HeiseiMin-W3", 6)
                            self.canvas.drawString(0.1 * inch, (10 - self.new_counter) * inch, str(val)) # in PDF schreiben/zeichnen

                            self.new_counter += 0.25
                            self.len_counter += 1
                    print("written pdf file start room: " + self.pdf_path + str(self.aktuellesDatum) + "/" + str(
                        key) + ".pdf")

                    for val in value:
                        if self.len_counter > 0 and (self.len_counter % 33) == 0 > -1: # alle 35 Zeilen eine neue Seite anfangen
                            if val[0].find("is joining") > -1:
                                self.canvas.setFont("HeiseiMin-W3", 6)  # utf-8 Schriftart festlegen
                                self.canvas.drawString(0.1 * inch, (10 - self.new_counter) * inch, str(val)) # in PDF schreiben/zeichnen
                                self.new_counter = 0 #neue Seite -> reset new_counter damit neue Zeilen in oberster Zeile Anfangen
                                self.canvas.showPage() # neue Seite Schreiben
                                self.new_counter += 0.25
                                self.len_counter += 1
                        elif val[0].find("is joining") > -1:
                            self.canvas.setFont("HeiseiMin-W3", 6)
                            self.canvas.drawString(0.1 * inch, (10 - self.new_counter) * inch, str(val)) # in PDF schreiben/zeichnen

                            self.new_counter += 0.25
                            self.len_counter += 1
                    print("written pdf file joining: " + self.pdf_path + str(self.aktuellesDatum) + "/" + str(
                        key) + ".pdf")

                    for val in value:
                        if self.len_counter > 0 and (self.len_counter % 33) == 0 > -1: # alle 35 Zeilen eine neue Seite anfangen
                            if val[0].find("has left") > -1:
                                self.canvas.setFont("HeiseiMin-W3", 6)  # utf-8 Schriftart festlegen
                                self.canvas.drawString(0.1 * inch, (10 - self.new_counter) * inch, str(val)) # in PDF schreiben/zeichnen
                                self.new_counter = 0 #neue Seite -> reset new_counter damit neue Zeilen in oberster Zeile Anfangen
                                self.canvas.showPage() # neue Seite Schreiben
                                self.new_counter += 0.25
                                self.len_counter += 1
                        elif val[0].find("has left") > -1:
                            self.canvas.setFont("HeiseiMin-W3", 6)
                            self.canvas.drawString(0.1 * inch, (10 - self.new_counter) * inch, str(val)) # in PDF schreiben/zeichnen

                            self.new_counter += 0.25
                            self.len_counter += 1
                    print("written pdf file has left: " + self.pdf_path + str(self.aktuellesDatum) + "/" + str(
                        key) + ".pdf")

                    self.canvas.save()# Seite erstellen
                pdffile.close() #PDF schließen
        except:
            print("Error in class: " + self.name + " - create_new_pdf() error. Please fix Code")
        else:
            print("class: " + self.name + " function: - create_new_pdf() executed succesfully")

    def start(self):
        self.create_new_pdf()
