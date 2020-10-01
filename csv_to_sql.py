from sqlalchemy import create_engine
import sqlalchemy
import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import random

connection = pg.connect(host="localhost", port=5432,
                        database="db", user="postgres", password="iii1234!")
df = psql.read_sql("SELECT * FROM ogr", connection)


def insert_data_many(table_name, df):
    try:
        cursor = connection.cursor()
        rows = []
        for index, row in df.iterrows():
            rows.append(list(row))
        cursor.executemany(
            f"INSERT INTO {table_name}({','.join(list(df))}) VALUES ({','.join(['%s']*len(list(df)))})", rows)
        connection.commit()
        count = cursor.rowcount
        print(count, "inserted succesfully")
    except (Exception, pg.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)


bolum_df = pd.read_excel("bolumler.xls")
bolum_df = bolum_df.drop_duplicates(["Bölüm Adı"])
bolumler = list(bolum_df["Bölüm Adı"])

names_df = pd.read_csv("names.csv")
names = names_df["name"]
surnames = names_df["surname"]

datas = []
for i in range(100):
    datas.append((random.choice(names), random.choice(surnames),
                  random.choice([1, 2, 3, 4]), random.choice(bolumler)))
insert_data_many("ogr", datas)

df.to_csv("first_table.csv", index=False)

second_df = pd.read_csv("first_table.csv")

cursor = connection.cursor()

table_name = "duplicate_ogr"
create_table = "create table "+table_name + \
    " (_id serial primary key, name varchar(50) not null, surname varchar(70) not null, grade int not null, department varchar(255) not null);"

cursor.execute(create_table)

connection.commit()

# csv to sql


engine = create_engine('postgresql://postgres:iii1234!@localhost:5432/db')

second_df.to_sql(name='duplicate_ogr', con=engine,
                 if_exists='append', index=False)
