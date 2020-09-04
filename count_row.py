from pyspark.sql import SparkSession
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext
import pyspark  # Call this only after findspark.init()
import findspark
import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import pandasql as ps
import time
import sys
import pyspark
from pyspark.sql import SQLContext

connection = pg.connect(host="localhost", port=5432,
                        database="iremdb", user="postgres", password="iii1234!")

start = time.time()
df = psql.read_sql("SELECT *FROM students", connection)
print(df['_id'].count())
print('pandas count func ile geçen süre =', time.time()-start)

start = time.time()
df = psql.read_sql("SELECT count(*) FROM students", connection)
print(time.time() - start)

cursor = connection.cursor()

start = time.time()
cursor.execute('select count(*) from students')
id_of_new_row = cursor.fetchone()[0]
print(id_of_new_row)
print('psycopg2 (cursor) ile geçen süre =', time.time() - start)

findspark.init()

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)


spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/iremdb") \
    .option("dbtable", "students") \
    .option("user", "postgres") \
    .option("password", "iii1234!") \
    .option("driver", "org.postgresql.Driver") \
    .load()

start = time.time()
print(df.count())
print('spark ile count etme süresi =', time.time() - start)
