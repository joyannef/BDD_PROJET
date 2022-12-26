#Exercice n° 2:
#Rédiger un script permettant d'afficher les statistiques globales à l'échelle du groupe

#Importer les modules
import sqlite3
import csv

#Connexion à la base de données
connect = sqlite3.connect('/Users/Laetitia/Documents/M1/BDD/Projet/bars.db')
cursor = connect.cursor()

#Trouver le nombre total de bars
#Compter simplement le nombre de lignes pour la colonne où il y a les noms de la table établissements
nombre_bars = cursor.execute("SELECT COUNT (name) FROM etablissements")
res1 = cursor.fetchall()
for item in res1:
    print(f"Nombre de Bars = {item}")

#Trouver le nombre d'employés 
#Compter simplement le nombre de lignes pour la colone matricule de la table employés
nombre_employes = cursor.execute("SELECT COUNT (matricule) FROM employes")
res2 = cursor.fetchall()
for item in res2:
    print(f"Nombre d'Employés = {item}")

#Trouver le nombre total de managers
#Compter le nombre de ligne où la profession est "manager"  
managers = cursor.execute("SELECT COUNT (matricule) FROM employes WHERE profession = 'Manager' ")
res3 = cursor.fetchall()
for item in res3:
    print(f"Nombre de Managers = {item}")

#Trouver le nombre d'employés par profession
#Compter le nombre de lignes pour chaque type de profession en utilisant "GROUP BY"
emp_par_profession = cursor.execute("SELECT profession, COUNT (matricule) FROM employes GROUP BY profession")
res4= cursor.fetchall()
for item in res4:
    print(item)

#Trouver le revenu total 
#Additionnant le prix de toutes les boissons vendues 
revenu_groupe = cursor.execute (""" SELECT SUM(S) FROM
                                              (SELECT COUNT(boisson_id) * prix AS S
                                              FROM ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson
                                              GROUP BY boisson_id)
                                             """)

res5 = cursor.fetchall()
for item in res5:
    print(f"Revenu du Groupe = {item}")

#Sauvegarde et déconnexion de la base 
connect.commit()
connect.close()
