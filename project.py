import pandas as pd

import psycopg2

conn = psycopg2.connect(
    "dbname='etiya' user='dwh_stg' host='192.168.1.45' password='Stg1220'")
cursor = conn.cursor()

owner = pd.DataFrame()

table_names = ['stg_dce_cust', 'stg_dce_party', 'stg_dce_gnl_st',
               'stg_dce_cust_tp', 'stg_dce_gnl_tp', 'stg_dce_gnl_st']
tables = {}

for name in table_names:
    sql = "select * from {} limit 10".format(name)
    tables[name] = (pd.read_sql_query(sql, conn))

m = pd.concat([owner, tables['stg_dce_cust']])

# m = pd.merge(m, tables['stg_dce_party'], how='left', on='party_id')
m = m.join(tables['stg_dce_party'], lsuffix='party_id', rsuffix='party_id')

m = m.join(tables['stg_dce_gnl_st'], lsuffix='st_id', rsuffix='gnl_st_id')

m = m.join(tables['stg_dce_cust_tp'],
           lsuffix='cust_tp_id', rsuffix='cust_tp_id')

m = m.join(tables['stg_dce_gnl_tp'],
           lsuffix='party_tp_id', rsuffix='gnl_tp_id')

m = m.join(tables['stg_dce_gnl_st'], lsuffix='st_id', rsuffix='gnl_st_id')
