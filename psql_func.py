import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

connection = pg.connect(host="localhost", port = 5432, database="iremdb", user="postgres", password="iii1234!")      
df = psql.read_sql("SELECT *FROM student", connection)
df.sort_values('_id')

def insert_data(name, surname, grade, department):
    try:
        cursor = connection.cursor()
        record_to_insert = (name, surname, grade, department)
        cursor.execute("INSERT INTO student(name, surname, grade, department) VALUES (%s,%s,%s,%s)", record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "inserted succesfully")
    except (Exception, pg.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

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

datas = [("rafet","topçu",3,"bm"),("irem","ekser",2,"bm")]
insert_data_many(datas)

insert_data('Rabia Sıla', 'Aydın', 4, 'Endüstri Müh.')

def delete_student(_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM student WHERE _id = (%s)", (_id, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "deleted succesfully")
    except (Exception, pg.Error) as error :
        if(connection):
            print("Failed to delete record into mobile table", error)

delete_student(99)

def update_grade(_id, grade):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE student SET grade = (%s) where _id = (%s)", (grade, _id))
        connection.commit()
        count = cursor.rowcount
        print(count, "updated succesfully")
    except (Exception, pg.Error) as error :
        if(connection):
            print("Failed to update record into mobile table", error)

update_grade(12, 2)