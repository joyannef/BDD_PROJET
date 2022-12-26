#Exercice n° 4:
#Rédiger un script pour trouver la date à laquelle il y a eu le moins de ventes et de bénéfices

#Importer les modules
import sqlite3
import csv

#Connexion à la base de données
connect = sqlite3.connect('/Users/Laetitia/Documents/M1/BDD/Projet/bars.db')
cursor = connect.cursor()

#Trouver la date avec le moins de ventes
moins_vente = cursor.execute ("""SELECT date, COUNT(date)
                                             FROM ventes
                                             GROUP BY date
                                             ORDER BY (SELECT COUNT(no_vente)) LIMIT 1""")
res = cursor.fetchall()
for item in res:
    print(item)

#Trouver la date où les benefices ont été moins importants
#Sélectionner la somme des prix des boissons vendues et regrouper par date
montant_total_emp = cursor.execute(""" SELECT date, ROUND(S, 6) FROM (SELECT date, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson
                                              GROUP BY date
                                              ORDER BY S ASC
                                              LIMIT 1)
                                             """)

res2 = cursor.fetchall()
for item in res2:
    print(item)

#final commit of all commands and print
connect.commit()
connect.close()

#Nous obtenons les mêmes dates pour les deux requêtes différentes
#Ce qui est logique étant donné que moins de boissons seront vendues, moins les bénéfices seront élevés
