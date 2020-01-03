"""
INPUT DATA:
Order_Date,Region,Name,Item,Units,UnitCost,Total
4/18/2016,Asia,RAM,Pencil,75,1.99,149.25
4/10/2017,Asia,LAXMAN,Pencil,66,1.99,131.34

OUTPUT:
NAME,ITEM,UNITS,TOTAL
"""

from dask.distributed import Client
from datetime import datetime
import dask.bag as bg
import dask.dataframe as dd
import sys

print('Start Time ::',datetime.now())
x1=datetime.now()
client=Client('tcp://<Dask Scheduler IP>:<PORT>')
input_file = str(sys.argv[1])
df = dd.read_csv(input_file, blocksize=10000000)
df=client.persist(df)
#df=df.groupby(['NAME', 'ITEM', 'ORDER_DATE']).agg({'UNITS':'sum', 'TOTAL':'sum'})
df = df.groupby(['NAME','ITEM']).agg({'UNITS':'sum','TOTAL':'sum'})
df=df.repartition(npartitions=1)
print(df.head(10))
print(datetime.now())
df.to_csv('dask_output/')
print(datetime.now()-x1)
