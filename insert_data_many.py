import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import random
import time
connection = pg.connect(host="localhost", port = 5432, database="iremdb", user="postgres", password="iii1234!")      

start = time.time()
df = psql.read_sql("SELECT *FROM student", connection)
end = time.time()
print(end - start)

def insert_data_many(datas):
    try:
        cursor = connection.cursor()
        cursor.executemany("INSERT INTO student(name, surname, grade, department) VALUES (%s,%s,%s,%s)", datas)
        connection.commit()
        count = cursor.rowcount
        print(count, "inserted succesfully")
    except (Exception, pg.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

bolum_df = pd.read_excel("bolumler.xls")
bolum_df = bolum_df.drop_duplicates(["Bölüm Adı"])
bolumler = list(bolum_df["Bölüm Adı"])

names_df = pd.read_csv("names.csv")
names = names_df["name"]
surnames = names_df["surname"]

datas = []
for i in range(10000):
    datas.append((random.choice(names), random.choice(surnames), random.choice([1,2,3,4]), random.choice(bolumler)))

start = time.time()
insert_data_many(datas)
end = time.time()
print(end - start)