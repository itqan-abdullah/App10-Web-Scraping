import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM events")
result = cursor.fetchall()
print(result)

cursor.execute("INSERT INTO events values('Feng Suave','Minimalia City','5.5.2089')")
connection.commit()
"""
cursor.execute("delete from events")
connection.commit()
"""