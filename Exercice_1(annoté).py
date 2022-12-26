#Exercice n° 1:
#Créer la base de données "bars.db"

#Importer les modules
import sqlite3
import csv

#Connexion à la base de données
connect = sqlite3.connect('bars.db')
cursor = connect.cursor()

#Création des différentes tables
cursor.execute("""CREATE TABLE carte (id_Boisson PRIMARY KEY,
                                    nom_Boisson TEXT NOT NULL,
                                    type TEXT NOT NULL,
                                    prix REAL NOT NULL,
                                    degre REAL,
                                    quantite REAL NOT NULL);""")

cursor.execute("""CREATE TABLE employes (
                                    prenom TEXT NOT NULL,
                                    nom TEXT NOT NULL,
                                    matricule TEXT PRIMARY KEY,
                                    profession TEXT NOT NULL,
                                    nom_bar TEXT NOT NULL)""")

cursor.execute("""CREATE TABLE etablissements (
                                    id_etablissement INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    adresse TEXT NOT NULL,
                                    num_Tel INTEGER NOT NULL,
                                    manager_id TEXT NOT NULL,
                                    FOREIGN KEY (manager_id) REFERENCES employes (matricule));""")

cursor.execute("""CREATE TABLE ventes (id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
                                    employe_id TEXT,
                                    boisson_id INTEGER, 
                                    date TEXT,
                                    FOREIGN KEY (boisson_id) REFERENCES carte (id_boisson),
                                    FOREIGN KEY (employe_id) REFERENCES employes (matricule));""")

#Ouvrir les fichiers CSV et insérer leurs données dans les tables
with open('/Users/Laetitia/Documents/M1/BDD/Projet/data/carte.csv', 'rt') as carte_path:
    carte_csv= csv.reader(carte_path, delimiter = "\t" )
    for row in carte_csv:
        print (row)
        Id_Boisson = row[0]
        Nom = row[1]
        Type = row[2]
        Prix = row[3]
        Degre = row[4]
        Quantite = row [5]
        cursor.execute("INSERT INTO carte (id_Boisson, nom_Boisson, type, prix, degre, quantite) VALUES (?, ?, ?, ?, ?, ?)", (Id_Boisson, Nom, Type, Prix, Degre, Quantite))

del_c = "DELETE FROM carte WHERE id_Boisson = 'Id_Boisson' "
cursor.execute(del_c)

with open('/Users/Laetitia/Documents/M1/BDD/Projet/data/employes.csv', 'rt') as employes_path:
    emp_csv = csv.reader(employes_path, delimiter="\t")
    for row in emp_csv:
        print(row)
        Prenom = row[0]
        Nom = row[1]
        Matricule = row[2]
        Profession = row[3]
        Nom_Bar = row[4]
        cursor.execute ("INSERT INTO employes (prenom, nom, matricule, profession, nom_bar) VALUES (?, ?, ?, ?, ?)", (Prenom, Nom, Matricule, Profession, Nom_Bar))

delete = "DELETE FROM employes WHERE prenom = 'Prenom' "
cursor.execute(delete)

with open('/Users/Laetitia/Documents/M1/BDD/Projet/data/etablissements.csv', 'rt') as etab_path:
    etab_csv = csv.reader(etab_path, delimiter="\t")
    for row in etab_csv:
        print (row)
        Name = row[0]
        Adresse = row[1]
        Num_Tel = row[2]
        Manager_id = row[3]
        cursor.execute("INSERT INTO etablissements (name, adresse, num_Tel, manager_id) VALUES (?,?,?,?)", (Name, Adresse, Num_Tel, Manager_id ))

del_etab = "DELETE FROM etablissements WHERE rowid IN (SELECT rowid FROM etablissements LIMIT 1);"
cursor.execute(del_etab)

with open('/Users/Laetitia/Documents/M1/BDD/Projet/data/ventes.csv', 'rt') as vente_path:
    vente_csv = csv.reader(vente_path, delimiter="\t")
    for row in vente_csv:
        print (row)
        Employe_Id = row[0]
        Boisson_Id = row[1]
        Date = row[2]
        cursor.execute ("INSERT INTO ventes (employe_id, boisson_id, date) VALUES (?, ?, ?)", (Employe_Id, Boisson_Id, Date))

del_vente = "DELETE FROM ventes WHERE rowid IN (SELECT rowid FROM ventes LIMIT 1);"
cursor.execute(del_vente)

select_all = "SELECT *"

connect.commit()

all = cursor.fetchall()
for item in all:
    print (item)

#Sauvegarde et déconnexion de la base
connect.commit()
connect.close()
