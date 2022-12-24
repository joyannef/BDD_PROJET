import sqlite3
import csv

#connect to the database
connect = sqlite3.connect('/Users/jfoster/Documents/PluriTAL/BDD/test/bars.db')
cursor = connect.cursor()

#La date le moins de vente a été enregistré
moins_vente = cursor.execute ("""SELECT date, COUNT(date)
                                             FROM ventes
                                             GROUP BY date
                                             ORDER BY (SELECT COUNT(no_vente)) LIMIT 1""")
res = cursor.fetchall()
for item in res:
    print(item)

#La date les benefices ont été moins importants

connect.commit()

all = cursor.fetchall()
for item in all:
    print (item)

#final commit of all commands and print
connect.commit()

connect.close()
