import requests
import sqlite3
from datetime import datetime

"""Call the free api to get bitcoin details"""
def call_api():
    api_response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    full_response=api_response.json()

    return full_response

"""Extract date and rate"""
def extract_from_api():
    full_response=call_api()
    get_coin_date = full_response['time']['updated']
    get_coin_rate = full_response['bpi']['USD']['rate_float']
    # convert date to db format
    get_coin_date=datetime.strptime(get_coin_date, "%b %d, %Y %H:%M:%S %Z")
    get_coin_date=datetime.strftime(get_coin_date, "%Y%M%d")
    
    return get_coin_date, get_coin_rate

"""Connect to db and save data"""
def load_data():
    get_coin_date,get_coin_rate=extract_from_api() 
   
    insert_sql=f"INSERT INTO bitcoin_daily_rate VALUES ({get_coin_date}, {get_coin_rate})" 
    con=sqlite3.connect("bicoin_price_db.db")
    cursor=con.cursor()
    cursor.execute(insert_sql)
    con.commit()


if __name__=="__main__":
    load_data()