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

# -----SPARK-----
# import findspark
# findspark.init()
# import pyspark
# sc = pyspark.SparkContext(appName="myAppName")

# start = time.time()
# sqlContext = SQLContext(sc)
# sqlContext.createDataFrame(df).count()
# print('spark func ile geçen süre =', time.time() - start)
