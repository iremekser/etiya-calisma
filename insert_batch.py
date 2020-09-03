import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import time
import random
from psycopg2 import extras
connection = pg.connect(host="localhost", port=5432,
                        database="iremdb", user="postgres", password="iii1234!")

def insert_data_batch(datas):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO students (name, surname, grade, department) VALUES (%s,%s,%s,%s)"
        extras.execute_batch(cursor, query, datas)
        connection.commit()
        print("inserted succesfully")
    except (Exception, pg.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)


# hazır csv'den datalar alındı
df = pd.read_csv('first_table.csv')
start = time.time()
insert_data_batch(zip(df.name, df.surname, df.grade.apply(str), df.department))
end = time.time()
print(end - start)
