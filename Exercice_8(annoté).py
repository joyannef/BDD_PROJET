#Exercice n° 8:
#Afficher les boissons les moins vendues dans l'établissement et afficher les employés qui ont le moins vendu

#Importer les modules
import sqlite3
import csv

#Connexion à la base de données 
connect = sqlite3.connect('/Users/Laetitia/Documents/M1/BDD/Projet/bars.db')
cursor = connect.cursor()

#L’identifiant du manager accédant aux informations.
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

#Pour verifier que les matricules dans b sont bien celles des managers, on peut exécuter la commande suivante en enlevant le "#"
# print (b)

#Accès aux ventes effectuées, afficher les boissons les moins vendues et les employés ayant vendu le moins de boissons
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
#Chercher les 3 boissons les moins vendues dans cet établissement 
            boissons_vendues = cursor.execute("""SELECT name, nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte, etablissements
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Le Saphir"
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des boissons les moins vendues :\n('Nom_du_Bar', 'Nom_Boisson', 'Id_Boisson', 'Total_Vendues')\n")
            for item in res:
                print(item)
#Chercher les 3 employés ayant vendu le moins dans cet établissement 
            vente_moins_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Saphir"
                                        GROUP BY nom
                                        ORDER BY F ASC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont vendus les moins de boissons :\n('Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
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
#Chercher les 3 boissons les moins vendues dans cet établissement 
            boissons_vendues = cursor.execute("""SELECT name, nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte, etablissements
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "L'Envers Bodega"
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des boissons les moins vendues :\n('Nom_du_Bar', 'Nom_Boisson', 'Id_Boisson', 'Total_Vendues')\n")
            for item in res:
                print(item)
#Chercher les 3 employés ayant vendu le moins dans cet établissement 
            vente_moins_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "L'Envers Bodega"
                                        GROUP BY nom
                                        ORDER BY F ASC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont vendus les moins de boissons :\n('Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
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
#Chercher les 3 boissons les moins vendues dans cet établissement
            boissons_vendues = cursor.execute("""SELECT name, nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte, etablissements
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "By Coss Bar"
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des boissons les moins vendues :\n('Nom_du_Bar', 'Nom_Boisson', 'Id_Boisson', 'Total_Vendues')\n")
            for item in res:
                print(item)
#Chercher les 3 employés ayant vendu le moins dans cet établissement 
            vente_moins_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "By Coss Bar"
                                        GROUP BY nom
                                        ORDER BY F ASC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont vendus les moins de boissons :\n('Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
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
#Chercher les 3 boissons les moins vendues de cet établissement
            boissons_vendues = cursor.execute("""SELECT name, nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte, etablissements
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Nu-Bahia"
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des boissons les moins vendues :\n('Nom_du_Bar', 'Nom_Boisson', 'Id_Boisson', 'Total_Vendues')\n")
            for item in res:
                print(item)
#Chercher les 3 employés ayant vendu le moins dans cet établissement 
            vente_moins_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Nu-Bahia"
                                        GROUP BY nom
                                        ORDER BY F ASC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont vendus les moins de boissons :\n('Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
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
#Chercher les 3 boissons les moins vendues dans cet établissement 
            boissons_vendues = cursor.execute("""SELECT name, nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte, etablissements
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Antirouille"
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des boissons les moins vendues :\n('Nom_du_Bar', 'Nom_Boisson', 'Id_Boisson', 'Total_Vendues')\n")
            for item in res:
                print(item)
#Chercher les 3 employés ayant vendu le moins dans cet établissement
            vente_moins_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Antirouille"
                                        GROUP BY nom
                                        ORDER BY F ASC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont vendus les moins de boissons :\n('Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
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
#Cherhcer les 3 boissons les moins vendues dans cet établissement 
            boissons_vendues = cursor.execute("""SELECT name, nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte, etablissements
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Comptoir de l'Arc"
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des boissons les moins vendues :\n('Nom_du_Bar', 'Nom_Boisson', 'Id_Boisson', 'Total_Vendues')\n")
            for item in res:
                print(item)
#Chercher les 3 employés ayant vendu le moins dans cet établissement 
            vente_moins_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir de l'Arc"
                                        GROUP BY nom
                                        ORDER BY F ASC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont vendus les moins de boissons :\n('Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
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
#Chercher les 3 boissons les moins vendues dans cet établissement 
            boissons_vendues = cursor.execute("""SELECT name, nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte, etablissements
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Comptoir Saint-Paul"
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des boissons les moins vendues :\n('Nom_du_Bar', 'Nom_Boisson', 'Id_Boisson', 'Total_Vendues')\n")
            for item in res:
                print(item)
#Chercher les 3 employés ayant vendu le moins dans cet établissement 
            vente_moins_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir Saint-Paul"
                                        GROUP BY nom
                                        ORDER BY F ASC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont vendus les moins de boissons :\n('Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
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
#Chercher les 3 boissons les moins vendues dans cvet établissement 
            boissons_vendues = cursor.execute("""SELECT name, nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte, etablissements
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "La Barbote"
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des boissons les moins vendues :\n('Nom_du_Bar', 'Nom_Boisson', 'Id_Boisson', 'Total_Vendues')\n")
            for item in res:
                print(item)
#Chercher les 3 employés ayant vendu le moins dans cet établissement 
            vente_moins_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "La Barbote"
                                        GROUP BY nom
                                        ORDER BY F ASC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont vendus les moins de boissons :\n('Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
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
#Chercher les 3 boissons les moins vendues de l'établissement 
            boissons_vendues = cursor.execute("""SELECT name, nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte, etablissements
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Chez Félix"
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des boissons les moins vendues :\n('Nom_du_Bar', 'Nom_Boisson', 'Id_Boisson', 'Total_Vendues')\n")
            for item in res:
                print(item)
#Chercher les 3 employés ayant vendu le moins dans cet établissement 
            vente_moins_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Chez Félix"
                                        GROUP BY nom
                                        ORDER BY F ASC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont vendus les moins de boissons :\n('Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
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
#Chercher les 3 boissons les moins vendues dans cet établissement
            boissons_vendues = cursor.execute("""SELECT name, nom_Boisson, boisson_id, COUNT(boisson_id) AS S
                                              FROM ventes, carte, etablissements
                                              WHERE ventes.boisson_id = carte.id_Boisson AND name = "Le Sens Six"
                                              GROUP BY boisson_id
                                              ORDER BY S ASC
                                              LIMIT 3
                                             """)
            res = cursor.fetchall()
            print(f"\nListe des boissons les moins vendues :\n('Nom_du_Bar', 'Nom_Boisson', 'Id_Boisson', 'Total_Vendues')\n")
            for item in res:
                print(item)
#Chercher les 3 employés ayant vendu le moins dans cet établissement                 
            vente_moins_emp = cursor.execute("""SELECT prenom, nom, matricule, COUNT (employe_id) AS F
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Sens Six"
                                        GROUP BY nom
                                        ORDER BY F ASC
                                        LIMIT 3""")
            res = cursor.fetchall()
            print(f"\nListe des employés qui ont vendus les moins de boissons :\n('Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
            for item in res:
                print(item)
            break
    else:
        print ("ERREUR. Vous n'avez pas d'accès à ces informations...")
        break

#Sauvegarde et déconnexion de la base
connect.commit()
connect.close()
