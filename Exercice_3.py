import sqlite3
import csv

#connect to the database
connect = sqlite3.connect('/Users/jfoster/Documents/PluriTAL/BDD/test/bars.db')
cursor = connect.cursor()

#no. total de boissons vendues par chaque employé
vente_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule
                                        GROUP BY nom""")

#manque montant total!!

res = cursor.fetchall()
for item in res:
    print(item)
