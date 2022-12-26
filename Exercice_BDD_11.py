import sqlite3
import csv

#connect to the database
connect = sqlite3.connect('/Users/jfoster/Documents/PluriTAL/BDD/test/bars.db')
cursor = connect.cursor()

#Afficher les employés qui ont vendus le plus de cocktail du moment et blonde pression

# Moyen degré d'alcool consommé étant donné tous les boissons vendues
d_alcool = cursor.execute("""SELECT SUM (F) / 37200 FROM (SELECT quantite, nom_Boisson, boisson_id, COUNT(boisson_id) * degre AS F
                                        FROM ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson
                                        GROUP BY nom_Boisson)
                                        """)
res = cursor.fetchall()
for item in res:
    print(item)

# Moyen quantite d'alcool consommé
q_alcool = cursor.execute("""SELECT SUM (Q) / 37200 FROM (SELECT quantite, nom_Boisson, boisson_id, COUNT(boisson_id) * quantite AS Q
                                        FROM ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson
                                        GROUP BY nom_Boisson)
                                        """)
res = cursor.fetchall()
for item in res:
    print(item)

connect.commit()

connect.close()

#il faut changer le nombre en fonction de nombre des ventes pour chaque etablissement
#Faut copier coller tout de Q 5 et mettre ces resultats en dessous "Vente_emp" dans le boucle pour chaque manager et ajouter le nom du bar dans la ligne WHERE
