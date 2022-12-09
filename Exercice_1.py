import sqlite3
import csv
from csv import DictReader

#connect to the database
connect = sqlite3.connect('BARStesting.db')
cursor = connect.cursor()

#creating the tables for the data
cursor.execute("""CREATE TABLE carte (id_Boisson INTEGER PRIMARY KEY,
                                    nom TEXT NON NULL,
                                    type TEXT NON NULL,
                                    prix REAL NON NULL,
                                    degre REAL,
                                    quantite REAL)""")

cursor.execute("""CREATE TABLE employes (matricule TEXT PRIMARY KEY,
                                    nom TEXT NON NULL,
                                    prenom TEXT NON NULL,
                                    profession TEXT NON NULL,
                                    nom_bar TEXT NON NULL)""")

cursor.execute("""CREATE TABLE etablissements (manager_id TEXT PRIMARY KEY,
                                    name TEXT NON NULL,
                                    adresse TEXT NON NULL,
                                    num_Tel INTEGER NON NULL)""")

cursor.execute("""CREATE TABLE ventes (no_vente INTEGER PRIMARY KEY AUTOINCREMENT,
                                    employe_id TEXT,
                                    boisson_id INTEGER, 
                                    date TEXT)""")

#paths
with open('/Users/jfoster/Documents/PluriTAL/BDD/Projet/data/carte.csv', 'rt') as carte_path:
    carte_csv= csv.reader(carte_path, delimiter="\t")
    for row in carte_csv:
        print (row)
        Id_Boisson = row[0]
        Nom = row[1]
        Type = row[2]
        Prix = row[3]
        Degre = row[4]
        Quantite = row [5]
        cursor.execute("INSERT INTO carte (id_Boisson, nom, type, prix, degre, quantite) VALUES (?, ?, ?, ?, ?, ?)", (Id_Boisson, Nom, Type, Prix, Degre, Quantite))

with open('/Users/jfoster/Documents/PluriTAL/BDD/Projet/data/employes.csv', 'rt') as employes_path:
    emp_csv = csv.reader(employes_path, delimiter="\t")
    for row in emp_csv:
        print (row)
        Prenom = row[0]
        Nom = row[1]
        Matricule = row[2]
        Profession = row[3]
        Nom_Bar = row[4]
        cursor.execute ("INSERT INTO employes (prenom, nom, matricule, profession, nom_bar) VALUES (?, ?, ?, ?, ?)", (Prenom, Nom, Matricule, Profession, Nom_Bar))

with open('/Users/jfoster/Documents/PluriTAL/BDD/Projet/data/etablissements.csv', 'rt') as etab_path:
    etab_csv = csv.reader(etab_path, delimiter="\t")
    for row in etab_csv:
        print (row)
        Manager_id = row[0]
        Name = row[1]
        Adresse = row [2]
        Num_Tel = row[3]
        cursor.execute("INSERT INTO etablissements (manager_id, name, adresse, num_Tel) VALUES (?,?,?,?)", (Manager_id, Name, Adresse, Num_Tel))

with open('/Users/jfoster/Documents/PluriTAL/BDD/Projet/data/ventes.csv', 'rt') as vente_path:
    vente_csv = csv.reader(vente_path, delimiter="\t")
    for row in vente_csv:
        print (row)
        # no_vente = row [0]
        Employe_Id = row[0]
        Boisson_Id = row[1]
        Date = row[2]
        # cursor.execute("INSERT INTO ventes (no_vente) VALUES (0)")
        cursor.execute ("INSERT INTO ventes (employe_id, boisson_id, date) VALUES (?, ?, ?)", (Employe_Id, Boisson_Id, Date))

connect.commit()

all = cursor.fetchall()
for item in all:
    print (item)

#final commit of all commands and print
connect.commit()

connect.close()
