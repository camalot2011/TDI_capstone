import pandas as pd
import sqlite3
import os

conn = sqlite3.connect("grant.db")
cur=conn.cursor()

fns = os.listdir('./Data/PRJ')
for fn in fns:
    path = './Data/PRJ/'+fn
    df = pd.read_csv(path,header=0,low_memory=False)
    df.to_sql("application",conn,if_exists="append")
    conn.commit()
    
cur.close()
conn.close()