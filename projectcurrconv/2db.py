#Create a table in stores database

import sqlite3

def save_to_database(amount, exrate, descurr, time):
    try:
        conn =sqlite3.connect('pro.db')
        cursor = conn.cursor()
        #print(conn)
        SQL="""
        CREATE TABLE currency 
        (Amount VARCHAR,ExchangeRate VARCHAR, 
        DestCurrency VARCHAR, Timestamp VARCHAR)
        """
        cursor.execute(SQL)
        print("Currency Table created")
        sqlinsert="""insert into currency(Amount, ExchangeRate, DestCurrency, Timestamp) values(?,?,?)"""
        val = tuple(amount, exrate, descurr, time)
        cursor.execute(sqlinsert,val)
        # Display data inserted
        print("Data Inserted in the table: ")
        data=cursor.execute('''SELECT * FROM STUDENT''')
        for row in data:
            print(row)
        conn.commit()
    except sqlite3.Error as e:
        print("error in connection", e)
    finally:
        # close the connection
        conn.close()
