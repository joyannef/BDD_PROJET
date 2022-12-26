#Exercice n° 3: 
#Rédiger un script permettant de consulter le nombre total de boissons vendues pour chaque employé
#ainsi que le montant total associé à ces ventes

#Importer les modules 
import sqlite3
import csv

#Connexion à la base de données
connect = sqlite3.connect('/Users/Laetitia/Documents/M1/BDD/Projet/bars.db')
cursor = connect.cursor()


#Requête permettant d'avoir le montant total des boissons vendues par employé 
Total_montant = cursor.execute("""SELECT prenom, nom, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule
                                              GROUP BY employe_id
                                              ORDER BY S DESC)
                                             """)

results = cursor.fetchall()
for item in results:
    print(item)

#Requête permettant d'avoir le nombre total de boissons vendues par employé
Total_boisson = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule
                                        GROUP BY nom
                                        ORDER BY F DESC""")
resultats = cursor.fetchall()
for item in resultats:
    print(item)
    
#Sauvegarde et deconnexion de la base
connect.commit()
connect.close()
