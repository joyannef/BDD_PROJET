import sqlite3
import csv

#connect to the database
connect = sqlite3.connect('/Users/jfoster/Documents/PluriTAL/BDD/test/bars.db')
cursor = connect.cursor()

#Afficher les employés qui ont vendus le plus de cocktail du moment et blonde pression

# TOTAL vendu de Cocktail du moment
cocktail_biere = cursor.execute("""SELECT nom_Boisson, boisson_id, COUNT(id_vente) AS F
                                        FROM ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND nom_Boisson = "Cocktail du moment"
                                        GROUP BY nom_Boisson
                                        ORDER BY F DESC
                                        LIMIT 3
                                        """)
res = cursor.fetchall()
for item in res:
    print(item)
# TOTAL vendu de Blonde Pression
cocktail_biere2 = cursor.execute("""SELECT nom_Boisson, boisson_id, COUNT(id_vente) AS F
                                        FROM ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND nom_Boisson = "Blonde pression"
                                        GROUP BY nom_Boisson
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
for item in res:
    print(item)

# Total par employé
cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
for item in res:
    print(item)
biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
for item in res:
    print(item)

connect.commit()

connect.close()

