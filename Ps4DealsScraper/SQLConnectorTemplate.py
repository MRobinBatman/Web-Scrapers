# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 22:57:51 2022

@author: Micha
"""
import mysql.connector
from mysql.connector import Error

def create_connection(ip_addr,user_name,user_password,ip_port,dB):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=ip_addr,
            user=user_name,
            passwd=user_password,
            port=ip_port,
            database=dB
            )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
# connection = create_connection("IPADDR","USERNAME","PASSWORD",PORT,"DATABASE")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfuly")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def get_query_results(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error '{e}' occured when pulling up sql table")
