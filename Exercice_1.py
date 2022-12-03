import sqlite3
import csv
from csv import DictReader

#connect to the database
connect = sqlite3.connect('BARS.db')
cursor = connect.cursor()

#creating the tables for the data
# cursor.execute("""CREATE TABLE carte (id_Boisson INTEGER PRIMARY KEY,
#                                     nom TEXT NON NULL,
#                                     type TEXT NON NULL,
#                                     prix INTEGER NON NULL,
#                                     degre TEXT NOT NULL,
#                                     quantite REAL NOT NULL)""")

# cursor.execute("""CREATE TABLE employes (matricule TEXT PRIMARY KEY,
#                                     nom TEXT NON NULL,
#                                     prenom TEXT NON NULL,
#                                     profession TEXT NON NULL,
#                                     nom_bar TEXT NON NULL)""")

# cursor.execute("""CREATE TABLE etablissements (manager_id INTEGER PRIMARY KEY,
#                                     name TEXT NON NULL,
#                                     adresse TEXT NON NULL,
#                                     num_Tel INTEGER NON NULL)""")

# cursor.execute("""CREATE TABLE ventes (employe_id TEXT PRIMARY KEY,
#                                     boisson_id INTEGER NON NULL,
#                                     date TEXT NON NULL)""")

# paths
#path = ("/Users/jfoster/Documents/PluriTAL/BDD/Projet/data/")
with open('/Users/jfoster/Documents/PluriTAL/BDD/Projet/data/employes.csv', 'r') as employes_path:
    emp_csv = csv.DictReader(employes_path, delimiter=" ")
    for line in emp_csv:
        cursor.executemany("INSERT INTO employes (prenom, nom, matricule, profession, nom_Bar) VALUES (:Prenom, :Nom, :Matricule, :Profession, :Nom_Bar)", (line,))
        
with open('/Users/jfoster/Documents/PluriTAL/BDD/Projet/data/carte.csv', 'r') as carte_path:
    carte_csv= csv.DictReader(carte_path, delimiter=" ")
    for line in carte_csv:
        cursor.executemany("INSERT INTO carte (id_Boisson, nom, type, prix, degre, quantite) VALUES (:Id_Boisson, :Nom, :Type, :Prix, :Degre, :Quantite)", (line,))

with open('/Users/jfoster/Documents/PluriTAL/BDD/Projet/data/ventes.csv', 'r') as vente_path:
    vente_csv = csv.DictReader(vente_path, delimiter=" ")
    for line in vente_path:
        cursor.executemany("INSERT INTO ventes (employe_Id, boisson_Id, date) VALUES (:Employe_Id, :Boisson_Id, :Date)", (line,))

with open('/Users/jfoster/Documents/PluriTAL/BDD/Projet/data/etablissements.csv', 'r') as etab_path:
    etab_csv = csv.DictReader(etab_path, delimiter=" ")
    for line in etab_csv:
        cursor.executemany("INSERT INTO etablissements (manager_id, name, adresse, num_Tel) VALUES (:Manager_id, :Name, :Adresse, :Num_Tel)", (line,))

connect.commit()


#final commit of all commands and print
all = cursor.fetchall()
for item in all:
    print (item)

connect.commit()

connect.close()
