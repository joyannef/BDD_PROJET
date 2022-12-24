import sqlite3
import csv

#connect to the database
connect = sqlite3.connect('/Users/jfoster/Documents/PluriTAL/BDD/test/bars.db')
cursor = connect.cursor()

# Les statistiques globale du groupe
nombre_bars = cursor.execute("SELECT COUNT (name) FROM etablissements")
res1 = cursor.fetchall()
for item in res1:
    print(item)

nombre_employes = cursor.execute("SELECT COUNT (matricule) FROM employes WHERE profession != 'Manager' ")
res2 = cursor.fetchall()
for item in res2:
    print(item)

managers = cursor.execute("SELECT COUNT (matricule) FROM employes WHERE profession = 'Manager' ")
res3 = cursor.fetchall()
for item in res3:
    print(item)

emp_par_profession = cursor.execute("SELECT profession, COUNT (matricule) FROM employes GROUP BY profession")
res4= cursor.fetchall()
for item in res4:
    print(item)
# revenu_groupe = cursor.execute ("SELECT boisson_id FROM ventes JOIN ON id_Boisson FROM carte WHERE boisson_id * prix")

connect.commit()

connect.close()
