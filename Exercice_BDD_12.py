import sqlite3
import csv

#connect to the database
connect = sqlite3.connect('/Users/jfoster/Documents/PluriTAL/BDD/test/bars.db')
cursor = connect.cursor()

#Afficher les boissons les moins vendues
boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)

resultat = cursor.fetchall()
for item in resultat:
    print(item)
#Afficher les boissons qui ont rapporté le moins d'argent
boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3)
                                             """)

resultat = cursor.fetchall()
for item in resultat:
    print(item)


connect.commit()

connect.close()


#Faut copier coller tout de Q 5 et mettre ces resultats en dessous "Vente_emp" dans le boucle pour chaque manager et ajouter le nom du bar dans la ligne WHERE
#Faut ajouter une ligne pour supprimer boissons 



