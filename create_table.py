# this code to create the "proverbs" table and "proverb_db" database an this needs to run only once

import sqlite3
import pandas as pd
df = pd.read_csv("proverb_scrapping.csv") # , encoding='cp1252')

connection = sqlite3.connect('proverb_db.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS proverbs (Proverb_Num INTEGER PRIMARY KEY, Author text, Proverb text)")
df.to_sql('proverbs', connection, if_exists='append', index = False)

retrieved = cursor.execute("SELECT * FROM proverbs").fetchall()

for r in retrieved:
    print(r)

connection.commit()
connection.close()

