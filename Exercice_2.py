import sqlite3
import csv

#connect to the database
connect = sqlite3.connect('/Users/jfoster/Documents/PluriTAL/BDD/test/bars.db')
cursor = connect.cursor()

#Les statistiques globale du groupe
nombre_bars = cursor.execute("SELECT COUNT (name) FROM etablissements")
res1 = cursor.fetchall()
for item in res1:
    print(f"Nombre de Bars = {item}")

#Donc le nombre d'employés sans les managers inclus 
nombre_employes = cursor.execute("SELECT COUNT (matricule) FROM employes WHERE profession != 'Manager' ")
res2 = cursor.fetchall()
for item in res2:
    print(f"Nombre d'Employés = {item}")

managers = cursor.execute("SELECT COUNT (matricule) FROM employes WHERE profession = 'Manager' ")
res3 = cursor.fetchall()
for item in res3:
    print(f"Nombre de Managers = {item}")

emp_par_profession = cursor.execute("SELECT profession, COUNT (matricule) FROM employes GROUP BY profession")
res4= cursor.fetchall()
for item in res4:
    print(item)

revenu_groupe = cursor.execute (""" SELECT SUM(S) FROM
                                              (SELECT COUNT(boisson_id) * prix AS S
                                              FROM ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson
                                              GROUP BY boisson_id)
                                             """)

res5 = cursor.fetchall()
for item in res5:
    print(f"Revenu du Groupe = {item}")
    
connect.commit()

connect.close()
