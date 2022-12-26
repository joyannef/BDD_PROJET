#Exercice n° 12:
#On vous demande de déterminer quelles boissons devraient être supprimées de la carte. Pour
#cela, vous avez le choix entre retirer les boissons les moins consommées et retirer les boissons
#qui rapportent le moins d’argent. Rédigez un script permettant une solution aux deux propositions. Le nombre de boissons à supprimer devra être défini en ligne de commande, en entrée
#du script.

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
        print ("Vous avez l'accès aux informations suivantes...\n('Nom_du_Bar','Prenom', 'Nom', 'Matricule', 'Total_Ventes')\n")
        if find_matricule == "T80612": 
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Saphir"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break

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
                break 

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
                break 

        if find_matricule == "R25976":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "L'Envers Bodega"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
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
                break 

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
                break 

        if find_matricule == "R81326":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "By Coss Bar"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
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
                break 

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
                break 
        if find_matricule == "Q66872":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Nu-Bahia"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
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
                break 

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
                break 
        if find_matricule == "Q09012":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Antirouille"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
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
                break 

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
                break 
        if find_matricule == "O42298":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir de l'Arc"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
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
                break 

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
                break 
        if find_matricule == "A08113":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir Saint-Paul"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
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
                break 

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
                break 
        if find_matricule == "Q42796":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "La Barbote"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
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
                break 

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
                break 
        if find_matricule == "R66525":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Chez Félix"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
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
                break 

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
                break 
        if find_matricule == "W04397":
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Sens Six"
                                        GROUP BY nom_bar, nom""")
            res = cursor.fetchall()
            for item in res:
                print(item)
            break
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
                break 

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
                break 
    else:
        print ("ERREUR. Vous n'avez pas d'accès à ces informations...")
        break




#Sauvegarder et déconnexion de la base 
connect.commit()
connect.close()
