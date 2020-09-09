import pandas as pd

import psycopg2

conn = psycopg2.connect(
    "dbname='etiya' user='dwh_stg' host='192.168.1.45' password='Stg1220'")

tables = {'stg_dce_cust': None,
          'stg_dce_party': {'lsuffix': 'party_id', 'rsuffix': 'party_id'},
          'stg_dce_gnl_st': {'lsuffix': 'st_id', 'rsuffix': 'gnl_std_id'},
          'stg_dce_cust_tp': {'lsuffix': 'cust_tp_id', 'rsuffix': 'cust_tp_id'},
          'stg_dce_gnl_tp': {'lsuffix': 'party_tp_id', 'rsuffix': 'gnl_st_id'},
          'stg_dce_gnl_st': {'lsuffix': 'st_id', 'rsuffix': 'gnl_st_id'}}

m = pd.DataFrame()
for table_name, suffixs in tables.items():
    df = pd.read_sql_query("select * from {}".format(table_name), conn)
    m = df if m.empty else m.join(
        df, lsuffix=suffixs['lsuffix'], rsuffix=suffixs['rsuffix'])
