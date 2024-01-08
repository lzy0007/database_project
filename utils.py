import pandas as pd
import numpy as np
import mysql.connector


# TASK 1: establish connection to MySQL
# You code starts here
conn = mysql.connector.connect(
    host='localhost',
    user = "root", # put your username here
    password='12345', # put your password here
    database='sakila'
)

# Use this function to get scalar values from MySQL
# To use the function, pass in the query variable and connection object.
def getOne_query(query,conn = conn):
    if query != '':
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return list(result)[0]
    else:
        return '--'

# Use this function to get dataframe from MySQL for ploting OR display of lists
# To use the function, pass in the query variable and connection object.
def getMany_query(query, conn = conn):
    if query != '':
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        result = pd.DataFrame(result, columns=cursor.column_names)
        cursor.close()
    else:
        result = pd.DataFrame()
    return result

