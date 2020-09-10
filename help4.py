import pandas as pd

import psycopg2

conn = psycopg2.connect(
    "dbname='etiya' user='dwh_stg' host='192.168.1.45' password='Stg1220'")

table_names = {'stg_dce_cust', 'stg_dce_party',
               'stg_dce_gnl_st', 'stg_dce_cust_tp', 'stg_dce_gnl_tp'}

df_tables = {}
for table in table_names:
    d = pd.read_sql_query(("select * from {}").format(table), conn)
    df_tables[table] = d

m = pd.DataFrame()

k = df_tables['stg_dce_cust'].merge(
    df_tables['stg_dce_party'], left_on='party_id', right_on='party_id', how='left')

l = df_tables['stg_dce_gnl_st'].merge(
    df_tables['stg_dce_cust'], left_on='gnl_st_id', right_on='st_id', how='inner')

p = df_tables['stg_dce_cust_tp'].merge(
    df_tables['stg_dce_cust'], left_on='cust_tp_id', right_on='cust_tp_id', how='inner')

r = df_tables['stg_dce_gnl_tp'].merge(
    df_tables['stg_dce_party'], left_on='gnl_tp_id', right_on='party_tp_id', how='inner')

# m = pd.concat([m, k])
# m = pd.concat([m, l])
# m = pd.concat([m, p])
# m = pd.concat([m, r])

# len(m)
# len 11964 geliyor concat ile
