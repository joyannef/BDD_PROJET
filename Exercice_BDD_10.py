import sqlite3
import csv

#connect to the database
connect = sqlite3.connect('/Users/jfoster/Documents/PluriTAL/BDD/test/bars.db')
cursor = connect.cursor()

#  l’identifiant du manager accédant aux informations.
droits_utilisateurs = cursor.execute("""SELECT matricule
                                        FROM employes
                                        WHERE profession = 'Manager'
                                        GROUP BY nom""")
a = []
b = []
for item in droits_utilisateurs:
    a.append(item)
for i in a:
    b.append(i[0])

#Pour verifier si les matricules dans b sont des matricules des managers
# print (b)

# Accès aux ventes effectuées dans son bar étant donné que la matricule est celle d'un manager et afficher les employés qui ont vendus le plus de cocktail du moment et blonde pression
in_b = True
while in_b:
    find_matricule = input("Entrer votre matricule: ")
    if find_matricule in b:
        print ("Vous avez l'accès aux informations suivantes...\n('Nom_du_Bar', 'Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
        if find_matricule == "T80612":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Saphir"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
            cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Le Saphir"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nVoici une liste des employés qui ont vendus le plus de Cocktail du Moment:\n('Nom', 'Prenom', 'id_Boisson', 'Total_Vendu')\n")
            for item in res:
                print(item)
            biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Le Saphir"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nVoici une liste des employés qui ont vendus le plus de Blonde pression:\n('Nom', 'Prenom', 'id_Boisson', 'Total_Vendu')\n")
            for item in res:
                print(item)
            break
        if find_matricule == "R25976":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "L'Envers Bodega"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "L'Envers Bodega"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "L'Envers Bodega"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
        if find_matricule == "R81326":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "By Coss Bar"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "By Coss Bar"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "By Coss Bar"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
        if find_matricule == "Q66872":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Nu-Bahia"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Nu-Bahia"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Nu-Bahia"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
        if find_matricule == "Q09012":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Antirouille"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Antirouille"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Antirouille"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
        if find_matricule == "O42298":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir de l'Arc"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Comptoir de l'Arc"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Comptoir de l'Arc"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
        if find_matricule == "A08113":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir Saint-Paul"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Comptoir Saint-Paul"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Comptoir Saint-Paul"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
        if find_matricule == "Q42796":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "La Barbote"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "La Barbote"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "La Barbote"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
        if find_matricule == "R66525":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Chez Félix"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Chez Félix"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Chez Félix"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
        if find_matricule == "W04397":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Sens Six"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Le Sens Six"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Le Sens Six"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
    else:
        print ("ERREUR. Vous n'avez pas d'accès à ces informations...")
        break

connect.commit()

connect.close()
