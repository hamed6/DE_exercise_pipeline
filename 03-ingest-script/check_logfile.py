#!/usr/bin/env python
# coding: utf-8
import argparse
import os
from time import time

import pandas as pd
from sqlalchemy import create_engine

def main(user_args):
    user_name = user_args.user_name
    password = user_args.password
    host= user_args.host
    port= user_args.port
    db_name= user_args.db_name
    table_name= user_args.table_name
    url= user_args.url
    file_name= 'sample.csv'
    
    # os.system(f"wget {url} -O {file_name}")
    

    engine=create_engine(f'postgresql://{user_name}:{password}@{host}:{port}/{db_name}')
    engine.connect()

    
    df_iterate=pd.read_csv(url, iterator=True, chunksize=100000)
    df=next(df_iterate)

    # Insert only column names of data to the db.
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')


    while True:
        # Get the next batch of csv file
        df=next(df_iterate)    
        df.to_sql(name=table_name, con=engine, if_exists='append')
        print(time())

if __name__=="__main__":
    # To get initial values from the user input as arguments
    parser=argparse.ArgumentParser(description="To build ingestion")

    parser.add_argument('--user_name')
    parser.add_argument('--password')
    parser.add_argument('--host')
    parser.add_argument('--port')
    parser.add_argument('--db_name')
    parser.add_argument('--table_name')
    parser.add_argument('--url')
    
    user_args=parser.parse_args()
    
    main(user_args)
