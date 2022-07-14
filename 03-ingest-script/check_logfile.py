#!/usr/bin/env python
# coding: utf-8

from time import time
from sqlalchemy import create_engine
import pandas as pd
import pyarrow.parquet as pq


def main():
    file = './yellow_tripdata_2022-01.parquet'
    df=pd.read_parquet(file, engine= 'pyarrow')
    df.to_csv('taxi_data.csv')


    engine=create_engine('postgresql://root:root@localhost:5432/dump_data')
    engine.connect()

    df_iterate=pd.read_csv('./taxi_data.csv', iterator=True, chunksize=100000)

    # Insert only column names of data to the db.
    df.head(n=0).to_sql(name='taxi_data', con=engine, if_exists='replace')

    while True:
        # Get the next batch of csv file
        df=next(df_iterate)    
        df.to_sql(name='taxi_data', con=engine, if_exists='append')
        print(time())


