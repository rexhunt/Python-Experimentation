#Grab JSON data & print it

import urllib.request, json

url="https://api.coinmarketcap.com/v1/ticker/"

with urllib.request.urlopen(url) as jsonurl:
    data = json.loads(jsonurl.read().decode())
    print(data)


##
##Set up connection to database
##
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='rex', password='rexhunt1',
                                      host='rexoregan.linkpc.net',
                                      database='cryptovalue')
cursor = mariadb_connection.cursor()#buffered=True)


##
##Print Data
## from https://stackoverflow.com/questions/30421466/why-would-mysql-execute-return-none
##
cursor.execute("SELECT * FROM Table1")

data = cursor.fetchall()
for r in data:
    print(r)

##
##Add data to database

cursor.execute("INSERT INTO Table1 (Text1,Text2) VALUES (%s,%s)",
               ("Test1","Test2"))
mariadb_connection.commit()

