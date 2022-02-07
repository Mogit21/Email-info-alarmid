"""
Creating a sample database with generic values, the database will contain two tables:
Table id and table region

"""

import sqlite3

idlist = [(x, "name"+str(x), "ipaddress"+str(x), "office"+str((x-1)//10+1)) for x in range(1,101)]
# Generates a list of 100 tuples for 100 NEs with the first NE ID == 1
# Starting from the first NE, each 10 NEs belong to a differnet office
# NE IDs from 1 to 10 belong to office 1, NE IDs from 11 to 20 belong to office 2, and so on ...

regionlist1 = [("office"+str(x), "region"+str(1), "owner"+str(1)) for x in range(1,5)]
regionlist2 = [("office"+str(x), "region"+str(2), "owner"+str(2)) for x in range(5,8)]
regionlist3 = [("office"+str(x), "region"+str(3), "owner"+str(3)) for x in range(8,11)]
regionlist = [*regionlist1, *regionlist2, *regionlist3]
# Generates a list of 10 tuples, distributing the 10 offices amongst 3 Regions having 1 different owner each

connection = sqlite3.connect("info-alarmid-db.db")
print ("Database opened successfully!")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS id (id integer primary key, name text, ipaddress text, office text)")
print ("Table id created successfully!")
cursor.executemany("INSERT INTO id VALUES (?,?,?,?)", idlist)
#connection.executemany("insert into id values (?,?,?,?)", idlist)    shortcut?
print ("Records created successfully in table id")

cursor.execute("CREATE TABLE IF NOT EXISTS region (office text primary key, region text, owner text)")
print ("Table region created successfully!")
cursor.executemany("INSERT INTO region VALUES (?,?,?)", regionlist)

print ("Records created successfully in table region")
cursor.execute ("SELECT * FROM region")
print (cursor.fetchall())

connection.commit()

connection.close()



