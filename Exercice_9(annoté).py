#Exercice n° 9:
#Donner la possibilité aux managers de voir les employés qui ont rapporté le plus et les boissons qui se sont vendues le plus

#Importer les modules 
import sqlite3
import csv

#Connexion à la base de données 
connect = sqlite3.connect('/Users/Laetitia/Documents/M1/BDD/Projet/bars.db')
cursor = connect.cursor()

#Créer les droits d'utilisateur pour les managers uniquement 
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

#Pour verifier si les matricules de b sont bien celles des managers, on peut faire la commande qui suit en enlevant le "#"
# print (b)

#Si les droits d'utilisateurs sont bien compatibles avec les matricules des managers, alors ils auront accès à la base 
in_b = True
while in_b:
    find_matricule = input("Entrer votre matricule: ")
    if find_matricule in b:
        print ("Vous avez l'accès aux informations suivantes...\n('Nom_du_Bar', 'Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")


        if find_matricule == "T80612": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Saphir"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
#Chercher les 3 boissons qui ont rapporté le plus
            boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT name, nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM etablissements, ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Le Saphir"
                                              GROUP BY boisson_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)

            resultat = cursor.fetchall()
            print(f"\nListe des boissons qui ont rapportés le plus d'argent:\n('Nom_Boisson', 'Boisson_Id', 'Total')\n")
            for item in resultat:
                print(item)
#Chercher les 3 employés qui ont vendu le plus
            montant_total_emp = cursor.execute("""SELECT nom_bar, prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT nom_bar, prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Le Saphir"
                                              GROUP BY employe_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont rapportés le plus d'argent:\n('Nom_Bar', 'Prenom', 'Nom', 'Total')\n")
            for item in res:
                print(item)
            break
        if find_matricule == "R25976": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "L'Envers Bodega"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
#Chercher les 3 boissons qui ont rapporté le plus
            boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM etablissements, ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "L'Envers Bodega"
                                              GROUP BY boisson_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)

            resultat = cursor.fetchall()
            print(f"\nListe des boissons qui ont rapportés le plus d'argent:\n('Nom_Boisson', 'Boisson_Id', 'Total')\n")
            for item in resultat:
                print(item)
#Chercher les 3 employés qui ont vendu le plus
            montant_total_emp = cursor.execute("""SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "L'Envers Bodega"
                                              GROUP BY employe_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont rapportés le plus d'argent:\n('Nom_Bar', 'Prenom', 'Nom', 'Total')\n")
            for item in res:
                print(item)
            break
        if find_matricule == "R81326": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "By Coss Bar"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
#Chercher les 3 boissons qui ont rapporté le plus
            boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM etablissements, ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "By Coss Bar"
                                              GROUP BY boisson_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)

            resultat = cursor.fetchall()
            print(f"\nListe des boissons qui ont rapportés le plus d'argent:\n('Nom_Boisson', 'Boisson_Id', 'Total')\n")
            for item in resultat:
                print(item)
#Chercher les 3 employés qui ont vendu le plus
            montant_total_emp = cursor.execute("""SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "By Coss Bar"
                                              GROUP BY employe_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont rapportés le plus d'argent:\n('Nom_Bar', 'Prenom', 'Nom', 'Total')\n")
            for item in res:
                print(item)
            break
        if find_matricule == "Q66872": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Nu-Bahia"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
#Chercher les 3 boissons qui ont rapporté le plus
            boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM etablissements, ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Nu-Bahia"
                                              GROUP BY boisson_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)

            resultat = cursor.fetchall()
            print(f"\nListe des boissons qui ont rapportés le plus d'argent:\n('Nom_Boisson', 'Boisson_Id', 'Total')\n")
            for item in resultat:
                print(item)
#Chercher les 3 employés qui ont vendu le plus
            montant_total_emp = cursor.execute("""SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Nu-Bahia"
                                              GROUP BY employe_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont rapportés le plus d'argent:\n('Nom_Bar', 'Prenom', 'Nom', 'Total')\n")
            for item in res:
                print(item)
            break
        if find_matricule == "Q09012": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Antirouille"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
#Chercher les 3 boissons qui ont rapporté le plus
            boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM etablissements, ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Antirouille"
                                              GROUP BY boisson_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)

            resultat = cursor.fetchall()
            print(f"\nListe des boissons qui ont rapportés le plus d'argent:\n('Nom_Boisson', 'Boisson_Id', 'Total')\n")
            for item in resultat:
                print(item)
#Chercher les 3 employés qui ont vendu le plus
            montant_total_emp = cursor.execute("""SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Antirouille"
                                              GROUP BY employe_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont rapportés le plus d'argent:\n('Nom_Bar', 'Prenom', 'Nom', 'Total')\n")
            for item in res:
                print(item)
            break
        if find_matricule == "O42298": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir de l'Arc"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
#Chercher les 3 boissons qui ont rapporté le plus
            boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM etablissements, ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Comptoir de l'Arc"
                                              GROUP BY boisson_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)

            resultat = cursor.fetchall()
            print(f"\nListe des boissons qui ont rapportés le plus d'argent:\n('Nom_Boisson', 'Boisson_Id', 'Total')\n")
            for item in resultat:
                print(item)
#Chercher les 3 employés qui ont vendu le plus
            montant_total_emp = cursor.execute("""SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Comptoir de l'Arc"
                                              GROUP BY employe_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont rapportés le plus d'argent:\n('Nom_Bar', 'Prenom', 'Nom', 'Total')\n")
            for item in res:
                print(item)
            break
        if find_matricule == "A08113": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir Saint-Paul"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
#Chercher les 3 boissons qui ont rapporté le plus
            boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM etablissements, ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Comptoir Saint-Paul"
                                              GROUP BY boisson_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)

            resultat = cursor.fetchall()
            print(f"\nListe des boissons qui ont rapportés le plus d'argent:\n('Nom_Boisson', 'Boisson_Id', 'Total')\n")
            for item in resultat:
                print(item)
#Chercher les 3 employés qui ont vendu le plus
            montant_total_emp = cursor.execute("""SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Comptoir Saint-Paul"
                                              GROUP BY employe_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont rapportés le plus d'argent:\n('Nom_Bar', 'Prenom', 'Nom', 'Total')\n")
            for item in res:
                print(item)
            break
        if find_matricule == "Q42796": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "La Barbote"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
#Chercher les 3 boissons qui ont rapporté le plus
            boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM etablissements, ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "La Barbote"
                                              GROUP BY boisson_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)

            resultat = cursor.fetchall()
            print(f"\nListe des boissons qui ont rapportés le plus d'argent:\n('Nom_Boisson', 'Boisson_Id', 'Total')\n")
            for item in resultat:
                print(item)
#Chercher les 3 employés qui ont vendu le plus
            montant_total_emp = cursor.execute("""SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "La Barbote"
                                              GROUP BY employe_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont rapportés le plus d'argent:\n('Nom_Bar', 'Prenom', 'Nom', 'Total')\n")
            for item in res:
                print(item)
            break
        if find_matricule == "R66525": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Chez Félix"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
#Chercher les 3 boissons qui ont rapporté le plus
            boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM etablissements, ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Chez Félix"
                                              GROUP BY boisson_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)

            resultat = cursor.fetchall()
            print(f"\nListe des boissons qui ont rapportés le plus d'argent:\n('Nom_Boisson', 'Boisson_Id', 'Total')\n")
            for item in resultat:
                print(item)
#Chercher les 3 employés qui ont vendu le plus
            montant_total_emp = cursor.execute("""SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Chez Félix"
                                              GROUP BY employe_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont rapportés le plus d'argent:\n('Nom_Bar', 'Prenom', 'Nom', 'Total')\n")
            for item in res:
                print(item)
            break
        if find_matricule == "W04397": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Sens Six"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
#Chercher les 3 boissons qui ont rapporté le plus
            boissons_vendues = cursor.execute("""SELECT nom_Boisson, boisson_id, S FROM (SELECT nom_Boisson, boisson_id, SUM(prix) AS S
                                              FROM etablissements, ventes, carte
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Le Sens Six"
                                              GROUP BY boisson_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)

            resultat = cursor.fetchall()
            print(f"\nListe des boissons qui ont rapportés le plus d'argent:\n('Nom_Boisson', 'Boisson_Id', 'Total')\n")
            for item in resultat:
                print(item)
#Chercher les 3 employés qui ont vendu le plus
            montant_total_emp = cursor.execute("""SELECT prenom, nom, employe_id, ROUND(S, 6) FROM (SELECT prenom, nom, employe_id, boisson_id, SUM(prix) AS S
                                              FROM ventes, carte, employes
                                              WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_bar = "Le Sens Six"
                                              GROUP BY employe_id
                                              ORDER BY S DESC
                                              LIMIT 3)
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont rapportés le plus d'argent:\n('Nom_Bar', 'Prenom', 'Nom', 'Total')\n")
            for item in res:
                print(item)
            break
    else:
        print ("ERREUR. Vous n'avez pas d'accès à ces informations...")
        break


#Sauvegarde et déconnexion de la base 
connect.commit()
connect.close()
