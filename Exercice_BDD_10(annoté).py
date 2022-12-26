#Exercice n° 10:
#Donner la possibilité aux managers de voir les employés qui ont vendu le plus de coktails du jour et de bières en pression
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
    else:
        print ("ERREUR. Vous n'avez pas d'accès à ces informations...")
        break

    if find_matricule == "T80612": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Saphir"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
                break
#Total de Cocktails vendus pour les 3 meilleurs employés
    cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Le Saphir"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
    resultat = cursor.fetchall()
    print(f"\nListe des employés qui ont vendus le plus de cocktails:\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n")
    for item in resultat: 
            print(item)
            break
#Total de Bières vendus par les 3 meilleurs employés 
    biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Le Saphir"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
    res = cursor.fetchall()
    print(f"\nListe des employés qui ont vendus le plus de bières :\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n" )
    for item in res:
            print(item)
            break 

    if find_matricule == "R25976": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "L'Envers Bodega"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
                break
#Total de Cocktails vendus pour les 3 meilleurs employés
    cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "L'Envers Bodega"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
    resultat = cursor.fetchall()
    print(f"\nListe des employés qui ont vendus le plus de cocktails:\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n")
    for item in resultat: 
                print(item)
                break
#Total de Bières vendus par les 3 meilleurs employés 
    biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "L'Envers Bodega"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
    res = cursor.fetchall()
    print(f"\nListe des employés qui ont vendus le plus de bières :\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n" )
    for item in res:
            print(item)
    break 

if find_matricule == "R81326": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "By Coss Bar"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
                break
#Total de Cocktails vendus pour les 3 meilleurs employés
cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "By Coss Bar"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
resultat = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de cocktails:\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n")
for item in resultat: 
                print(item)
                break
#Total de Bières vendus par les 3 meilleurs employés 
biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "By Coss Bar"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de bières :\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n" )
for item in res:
            print(item) 
            break 

if find_matricule == "Q66872": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Nu-Bahia"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
                break
#Total de Cocktails vendus pour les 3 meilleurs employés
cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Nu-Bahia"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
resultat = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de cocktails:\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n")
for item in resultat: 
                print(item)
                break
#Total de Bières vendus par les 3 meilleurs employés 
biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Nu-Bahia"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de bières :\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n" )
for item in res:
            print(item) 
            break 

if find_matricule == "Q09012": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Antirouille"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
                break
#Total de Cocktails vendus pour les 3 meilleurs employés
cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Antirouille"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
resultat = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de cocktails:\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n")
for item in resultat: 
                print(item)
                break
#Total de Bières vendus par les 3 meilleurs employés 
biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Antirouille"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de bières :\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n" )
for item in res:
            print(item) 
            break 

if find_matricule == "O42298": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir de l'Arc"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
                break
#Total de Cocktails vendus pour les 3 meilleurs employés
cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Comptoir de l'Arc"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
resultat = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de cocktails:\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n")
for item in resultat: 
                print(item)
                break
#Total de Bières vendus par les 3 meilleurs employés 
biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Comptoir de l'Arc"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de bières :\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n" )
for item in res:
            print(item) 
            break 

if find_matricule == "A08113": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Comptoir Saint-Paul"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
                break
#Total de Cocktails vendus pour les 3 meilleurs employés
cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Comptoir Saint-Paul"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
resultat = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de cocktails:\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n")
for item in resultat: 
                print(item)
                break
#Total de Bières vendus par les 3 meilleurs employés 
biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Comptoir Saint-Paul"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de bières :\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n" )
for item in res:
            print(item) 
            break 

if find_matricule == "Q42796": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "La Barbote"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
                break
#Total de Cocktails vendus pour les 3 meilleurs employés
cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "La Barbote"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
resultat = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de cocktails:\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n")
for item in resultat: 
                print(item)
                break
#Total de Bières vendus par les 3 meilleurs employés 
biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "La Barbote"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de bières :\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n" )
for item in res:
            print(item) 
            break 

if find_matricule == "R66525": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Chez Félix"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
                break
#Total de Cocktails vendus pour les 3 meilleurs employés
cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Chez Félix"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
resultat = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de cocktails:\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n")
for item in resultat: 
                print(item)
                break
#Total de Bières vendus par les 3 meilleurs employés 
biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Chez Félix"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de bières :\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n" )
for item in res:
            print(item) 
            break 

if find_matricule == "W04397": #Attribuer ce matricule à son établissement respectif
            vente_emp = cursor.execute("""SELECT nom_bar, prenom, nom, matricule, COUNT (employe_id)
                                        FROM employes, ventes
                                        WHERE ventes.employe_id = employes.matricule AND nom_bar = "Le Sens Six"
                                        GROUP BY nom_bar, nom
                                              """)
            res = cursor.fetchall()
            for item in res:
                print(item)
                break
#Total de Cocktails vendus pour les 3 meilleurs employés
cocktail = cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Cocktail du moment" AND nom_bar = "Le Sens Six"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
resultat = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de cocktails:\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n")
for item in resultat: 
                print(item)
                break
#Total de Bières vendus par les 3 meilleurs employés 
biere =  cursor.execute("""SELECT nom, prenom, employe_id, nom_Boisson, COUNT(employe_id) AS F
                                        FROM employes, ventes, carte
                                        WHERE ventes.boisson_id = carte.id_Boisson AND ventes.employe_id = employes.matricule AND nom_Boisson = "Blonde pression" AND nom_bar = "Le Sens Six"
                                        GROUP BY employe_id
                                        ORDER BY F DESC
                                        LIMIT 3""")
res = cursor.fetchall()
print(f"\nListe des employés qui ont vendus le plus de bières :\n('Nom_bar', 'Prenom', 'Nom', 'Total')\n" )
for item in res:
            print(item) 
            break 


#Sauvegarde et déconnexion de la base 
connect.commit()
connect.close()
