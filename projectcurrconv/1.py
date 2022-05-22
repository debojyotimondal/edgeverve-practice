import requests
from dateutil.parser import parse 

API_KEY = "f9161ebcd341d90ddf66a302"

def get_all_exchange_rates(src):
    # request the ExchangeRate API and convert to Python dict using .json()
    url = f"https://v6.exchangerate-api.com/v6/f9161ebcd341d90ddf66a302/latest/USD?access_key={API_KEY}&symbols={src}&format=1"
    #data = requests.get(url).json()
    data = requests.get(url).json()
    #print(data)
    if data["result"] == "success":
        # request successful
        # get the last updated datetime
        last_updated_datetime = parse(data["time_last_update_utc"])
        # get the exchange rates
        exchange_rates = data["conversion_rates"]
    return last_updated_datetime, exchange_rates, data

def convert_currency(src, dst, amount):
    # get all the exchange rates
    last_updated_datetime, exchange_rates, data = get_all_exchange_rates(src)
    # convert by simply getting the target currency exchange rate and multiply by the amount
    if src != 'USD':
        amount = amount / exchange_rates[src]
    rates = []
    for i in dst:
        try:
            #for i in dst:
            i = i.strip()
            #datetime.append(last_updated_datetime)
            rates.append(exchange_rates[i] * amount)
            #print(rates)
        except:
            print(f'Destination Currency {i} not eligible')
    return last_updated_datetime, rates

import sqlite3

def save_to_database(amount, exrate, descurr, time):
    try:
        conn =sqlite3.connect('pro.db')
        cursor = conn.cursor()
        #print(conn)
        SQL="""
        CREATE TABLE IF NOT EXISTS currency 
        (Amount FLOAT,ExchangeRate VARCHAR, 
        DestCurrency VARCHAR, Timestamp TIMESTAMP)
        """
        cursor.execute(SQL)
        #print("Currency Table created")
        sqlinsert="""insert into currency(Amount, ExchangeRate, DestCurrency, Timestamp) values(?,?,?,?)"""
        val = tuple([amount, exrate, descurr, time])
        cursor.execute(sqlinsert,val)
        # Display data inserted
        #print("Data Inserted in the table: ")
        data=cursor.execute('''SELECT * FROM currency''')
        for row in data:
            print(row)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("error in connection", e)
    finally:
        # close the connection
        conn.close()


if __name__ == "__main__":
    import sys
    #source_currency = sys.argv[1]
    ####INPUT FROM USER######
    source_currency  = input('Enter base currency:')
    print(source_currency )
    destination_currency = input('Enter destination currencies:')
    print(destination_currency)
    amount = float(input('Enter amount:'))
    #n = len(sys.argv[2])
    #a = sys.argv[2][1:n-1]
    #destination_currency = sys.argv[2]
    destination_currency = destination_currency.split(',')
    #amount = float(input('Enter amount:'))
    last_updated_datetime, exchange_rate = convert_currency(source_currency, destination_currency, amount)
    print("Last updated datetime:", last_updated_datetime)
    print(f"{amount} {source_currency} = {exchange_rate} {destination_currency}")
    #saving to database
    if source_currency == "INR":
        for exr, des in zip(exchange_rate, destination_currency):
            save_to_database(amount, exr, des, last_updated_datetime)
        
