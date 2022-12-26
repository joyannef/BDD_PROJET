#Exercice n° 6:
#Droits d'utilisateurs des managers: afficher le nombre de ventes du mois et le montant

#Importer les modules 
import sqlite3
import csv 

#Connexion à la base de données
connect = sqlite3.connect('/Users/Laetitia/Documents/M1/BDD/Projet/bars.db')
cursor = connect.cursor()

#Créer la variable "droits d'utilisateurs" pour les matricules
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

#Créer la variable pour les dates présentent dans notre base de données
dates_bdd = cursor.execute("""SELECT date
                                FROM ventes
                                GROUP BY date """)
c = []
d = []
for item in dates_bdd:
    c.append(item)
    for i in c:
        d.append(i[0])

#Renseigner la date souhaitée
in_d = True
while in_d:
    find_date = input("Saisisez une date au format 'jj/mm/aaaa': ")
    if find_date in d:
        print ()
        break
    else:
        print("Veuillez renseigner une date valide")

    
#Renseigner les matricules des managers pour permettre l'accès aux ventes effectuées et les bénéfices du bar
in_b = True
while in_b:
    find_matricule = input("Entrer votre matricule: ")
    if find_matricule in b:
        print ("Vous avez l'accès aux informations suivantes...\n('Nom_du_Bar', 'Date', 'Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
        break 
    else:
        print ("ERREUR. Vous n'avez pas d'accès à ces informations...")
        break

#Conditions
if find_matricule == "T80612" :
            vente_emp = cursor.execute("""SELECT nom_bar, date, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Saphir" 
                                        GROUP BY nom_bar, nom""")

            res = cursor.fetchall()
            for item in res:
                print(item)
            vente_effectuees = (input("\nVoudriez-vous l'accès au bénéfice généré par vos employés (répondez: O/N)? :  "))
            print (vente_effectuees)
            if vente_effectuees == "O":
                montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Le Saphir"
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
                print ("Voici le bénéfice de chaque employé en ordre descendant :\n")
                res = cursor.fetchall()
                for item in res:
                    print(item)
                    

                

if find_matricule == "R25976":
            vente_emp = cursor.execute("""SELECT nom_bar, date, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "L'Envers Bodega"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            vente_effectuees = (input("\nVoudriez-vous l'accès au bénéfice généré par vos employés (répondez: O/N)? :  "))
            print (vente_effectuees)
            if vente_effectuees == "O":
                montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "L'Envers Bodega"
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
                print ("Voici le bénéfice de chaque employé en ordre descendant :\n")
                res = cursor.fetchall()
                for item in res:
                    print(item)
                    
    
if find_matricule == "R81326":
            vente_emp = cursor.execute("""SELECT nom_bar, date, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "By Coss Bar"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            vente_effectuees = (input("\nVoudriez-vous l'accès au bénéfice généré par vos employés (répondez: O/N)? :  "))
            print (vente_effectuees)
            if vente_effectuees == "O":
                montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "By Coss Bar"
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
                print ("Voici le bénéfice de chaque employé en ordre descendant :\n")
                res = cursor.fetchall()
                for item in res:
                    print(item)
                
if find_matricule == "Q66872":
            vente_emp = cursor.execute("""SELECT nom_bar, date, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Nu-Bahia"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            vente_effectuees = (input("\nVoudriez-vous l'accès au bénéfice généré par vos employés (répondez: O/N)? :  "))
            print (vente_effectuees)
            if vente_effectuees == "O":
                montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Nu-Bahia"
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
                print ("Voici le bénéfice de chaque employé en ordre descendant :\n")
                res = cursor.fetchall()
                for item in res:
                    print(item)
        
if find_matricule == "Q09012":
            vente_emp = cursor.execute("""SELECT nom_bar, date, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Antirouille"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            vente_effectuees = (input("\nVoudriez-vous l'accès au bénéfice généré par vos employés (répondez: O/N)? :  "))
            print (vente_effectuees)
            if vente_effectuees == "O":
                montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Antirouille"
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
                print ("Voici le bénéfice de chaque employé en ordre descendant :\n")
                res = cursor.fetchall()
                for item in res:
                    print(item)
              
if find_matricule == "O42298":
            vente_emp = cursor.execute("""SELECT nom_bar, date, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir de l'Arc"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            vente_effectuees = (input("\nVoudriez-vous l'accès au bénéfice généré par vos employés (répondez: O/N)? :  "))
            print (vente_effectuees)
            if vente_effectuees == "O":
                montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Comptoir de l'Arc"
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
                print ("Voici le bénéfice de chaque employé en ordre descendant :\n")
                res = cursor.fetchall()
                for item in res:
                    print(item)
        
if find_matricule == "A08113":
            vente_emp = cursor.execute("""SELECT nom_bar, date, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir Saint-Paul"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            vente_effectuees = (input("\nVoudriez-vous l'accès au bénéfice généré par vos employés (répondez: O/N)? :  "))
            print (vente_effectuees)
            if vente_effectuees == "O":
                 montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Comptoir Saint-Paul"
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
                 print ("Voici le bénéfice de chaque employé en ordre descendant :\n")
                 res = cursor.fetchall()
                 for item in res:
                    print(item)

if find_matricule == "Q42796":
            vente_emp = cursor.execute("""SELECT nom_bar, date, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "La Barbote"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            vente_effectuees = (input("\nVoudriez-vous l'accès au bénéfice généré par vos employés (répondez: O/N)? :  "))
            print (vente_effectuees)
            if vente_effectuees == "O":
                 montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "La Barbote"
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
                 print ("Voici le bénéfice de chaque employé en ordre descendant :\n")
                 res = cursor.fetchall()
                 for item in res:
                     print(item)
       
if find_matricule == "R66525":
            vente_emp = cursor.execute("""SELECT nom_bar, date, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Chez Félix"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            vente_effectuees = (input("\nVoudriez-vous l'accès au bénéfice généré par vos employés (répondez: O/N)? :  "))
            print (vente_effectuees)
            if vente_effectuees == "O":
                 montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Chez Félix"
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
                 print ("Voici le bénéfice de chaque employé en ordre descendant :\n")
                 res = cursor.fetchall()
                 for item in res:
                     print(item)
      
if find_matricule == "W04397":
            vente_emp = cursor.execute("""SELECT nom_bar, date, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Sens Six"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            vente_effectuees = (input("\nVoudriez-vous l'accès au bénéfice généré par vos employés (répondez: O/N)? :  "))
            print (vente_effectuees)
            if vente_effectuees == "O":
                 montant_total_emp = cursor.execute(""" SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Le Sens Six"
                                              GROUP BY employe_id)
                                              ORDER BY S DESC
                                             """)
                 print ("Voici le bénéfice de chaque employé en ordre descendant :\n")
                 res = cursor.fetchall()
                 for item in res:
                     print(item)


#Sauvegarde et déconnexion de la base
connect.commit()
connect.close()
