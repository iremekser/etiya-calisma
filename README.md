# etiya-calisma
*Bu kütüphane Etiya Bilgi Teknoloji ve Hizmetlerinde yaptığım staj boyunca kullandığım fonksiyonlardır. Bu fonksiyonlar şirket içinde kullanılmak ve yapılan işleri kolaylaştırmak için yazılmıştır.*
## Kurulum
```
pip install etiya_ie
```

## Tablodaki Satır Sayısı
Tablodaki satır sayısına ulaşmak için farklı kütüphanelerin kullanıldığı fonksiyonları içerir.
```python
import etiya_ie

from psycopg2 import connect

connection = connect(host="localhost", port=5432,
                     database="db", user="username", password="pass")
table_name = "students"
count_row_functions = etiya_ie.count_row(connection, table_name)

count = count_row_functions.pandas_count_row()
count = count_row_functions.sql_count_row()
count = count_row_functions.psycopg2_count_row()
count = count_row_functions.spark_count_row()
```

## CSV Dosyasının SQL'e Aktarımı - CRUD İşlemleri
Csv dosyasındaki verileri SQL'e Python yardımıyla aktarmak için kullanılan fonksiyonları içermektedir. SQL tablosu için create-read-update-delete fonksiyonlarını içermektedir.
```python
import etiya_ie
import pandas as pd

from psycopg2 import connect

connection = connect(host="localhost", port=5432,
                     database="db", user="username", password="pass")

csv_to_sql_funcs = etiya_ie.csv_to_sql(connection)
df = pd.read_csv("example.csv")

csv_to_sql_funcs.create_table(table_name, df)
csv_to_sql_funcs.insert_data_many(table_name, df)
csv_to_sql_funcs.insert_data_batch(table_name, df)
csv_to_sql_funcs.delete_student(table_name, 5)
csv_to_sql_funcs.update_column(table_name, 7, column_name, 2)
```

## Serverda SSH Yoluyla Dosya Oluşturma
Girilen bilgileri kullanarak SSH yoluyla serverda dosya oluşturmak için kullanılan fonksiyonları içermektedir. 
```python
import ie_funcs

user = 'iremekser'
host = '000.000.0.00'

ssh_funcs = etiya_ie.ssh_funcs(user, host)
ssh_funcs.create_file_to_server(filename)
```

## SQL Tablolarındaki Join İşlemleri
SQL koduyla yazılan join işlemlerini python ile yazarak daha kolay hale getirebilmek için kullanılan fonksiyonları içermektedir.
```python
import etiya_ie

from psycopg2 import connect

connection = connect(host="localhost", port=5432,
                     database="db", user="username", password="pass")

tables = {'stg_dce_cust': None,
          'stg_dce_party': {'lsuffix': 'party_id', 'rsuffix': 'party_id'},
          'stg_dce_gnl_st': {'lsuffix': 'st_id', 'rsuffix': 'gnl_std_id'},
          'stg_dce_cust_tp': {'lsuffix': 'cust_tp_id', 'rsuffix': 'cust_tp_id'},
          'stg_dce_gnl_tp': {'lsuffix': 'party_tp_id', 'rsuffix': 'gnl_st_id'},
          'stg_dce_gnl_st': {'lsuffix': 'st_id', 'rsuffix': 'gnl_st_id'}}

df = etiya_ie.join_funcs(conn, tables).join()
```
