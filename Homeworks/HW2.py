#Student name: Huzaifa Shoeb, ID: 1925670
#Following is the Python Code for Homework 1

from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'cis3368spring.c7ykkkkkq29g.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'saturnskyblack',
    'database': 'cis3368springdb'

}

# Function to execute SQL read query
def sql_read_query(query, params=()):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

# Function to execute SQL write query
def sql_write_query(query, params=()):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# API Endpoint to get all tires from Inventory
@app.route('/api/Inventory', methods=['GET'])
def get_Inventory():
    query = 'SELECT * FROM Inventory'
    tires = sql_read_query(query)

    return jsonify({'Inventory': tires})

