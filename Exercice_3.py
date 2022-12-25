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

resultat = cursor.fetchall()
for item in resultat:
    print(item)

#Montant total vendue par employé
montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
res = cursor.fetchall()
for item in res:
    print(item)

#     Liste de toutes les boissons vendues ainsi que le prix par employé
# """SELECT employe_id, boisson_id, prix, date
#                                               FROM ventes, carte
#                                               WHERE ventes.boisson_id = carte.id_Boisson
#                                      ORDER BY employe_id, boisson_id
#                                              """)

#ESSAYER FAIRE UN UNION DES RESULTATS

connect.commit()

connect.close()
