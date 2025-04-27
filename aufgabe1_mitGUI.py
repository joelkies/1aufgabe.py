import mariadb
import sys
import tkinter as tk

#Bestandseingabefeld 
def bn_bestandseingabe():
    lieferant = "" 
    artikelname = ""
    anzahl = tf_eingabe.get() #ließt das eingabefeld aus
    stringabfrage = f"""SELECT artikel.Lagerbestand, artikel.Lieferant, artikel.Artikelname
    FROM artikel
    WHERE artikel.Lagerbestand < {anzahl}"""
    print(stringabfrage)
    abfrage = conn.cursor()  #conn.cursor() erzeugt das objekt welches die abfrage macht
    abfrage.execute(stringabfrage) #führt die abfrage aus
    stringausgabe = [["lagerbestand","lieferant","artikelname"]]
    
    for (lagerbestand, lieferant, artikelname) in abfrage:
        stringausgabe.append([lagerbestand,lieferant,artikelname]) #fügt liste hinzu
        
        
    lb_ausgabe.config(text=stringausgabe) #gilt für das fenster (fügt die liste ins fenster ein)


    
try:
    conn = mariadb.connect(
        user = "joelms13",
        password = "Sonnenblume@1",
        host = "localhost",
        port = 3306,
        database = "schlumpfshop3")
   
except mariadb.Error as e:
    print(f"Error connecting to MariaDB PLatform: {e}")
    sys.exit(1)



fenster = tk.Tk() #Fenster erstellen
fenster.geometry("500x500")

lb_mindeststueckzahl = tk.Label(fenster, text="Eingabe Mindeststückzahl") #erstellt ein label

tf_eingabe = tk.Entry(fenster,width=3) #width is die anzahl der zeichen für die eingabe

lb_ausgabe = tk.Label(fenster)

bn_bestand = tk.Button(fenster,text="Bestandeingabe",command=bn_bestandseingabe)

#Widgets hinzufügen
lb_mindeststueckzahl.pack() #setzt das label in das fenster
tf_eingabe.pack()
lb_ausgabe.pack()
bn_bestand.pack()
fenster.mainloop() #steht immer unter den anderen dingen

fenster.close()
conn.close()

