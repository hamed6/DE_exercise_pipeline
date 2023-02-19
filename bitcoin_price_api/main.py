import requests
import sqlite3
from datetime import datetime

def call_api():
    """call the free api to get bitcoin details"""
        
    api_response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    full_response=api_response.json()

    return full_response


def extract_from_api():
    """extract date and rate"""
    full_response=call_api()
    get_coin_date = full_response['time']['updated']
    get_coin_rate = full_response['bpi']['USD']['rate_float']
    # convert date to db format
    get_coin_date=datetime.strptime(get_coin_date, "%b %d, %Y %H:%M:%S %Z")
    get_coin_date=datetime.strftime(get_coin_date, "%Y%M%d")
    
    return get_coin_date, get_coin_rate

def load_data():
    """connect to db and save data"""
    get_coin_date,get_coin_rate=extract_from_api() 
    
    insert_sql=f"INSERT INTO bitcoin_daily_rate VALUES ({get_coin_date}, {get_coin_rate})" 
    con=sqlite3.connect("bicoin_price_db.db")
    cursor=con.cursor()
    cursor.execute(insert_sql)
    con.commit()


if __name__=="__main__":
    load_data()