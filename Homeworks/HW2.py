#Student name: Huzaifa Shoeb, ID: 1925670
#Following is the Python Code for Homework 2

from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL database connection
db_config = {
    'host': 'cis3368spring.c7ykkkkkq29g.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'saturnskyblack',
    'database': 'cis3368springdb'

}

# Function to execute SQL read query
def sql_read_query(query, Parameters=()):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, Parameters)
    result = cursor.fetchall()
    conn.close()
    return result

# Function to execute SQL write query
def sql_write_query(query, Parameters=()):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query, Parameters)
    conn.commit()
    conn.close()

# API Endpoint to get all Tires from Inventory
@app.route('/api/Inventory', methods=['GET'])
def get_Inventory():
    query = 'SELECT * FROM Inventory'
    Tires = sql_read_query(query)

    return jsonify({'Inventory': Tires})

# API Endpoint to add a new Tire to Inventory
@app.route('/api/Inventory', methods=['POST'])
def add_Tire():
    data = request.get_json()
    query = 'INSERT INTO Inventory (Brand, Model, Loadrating, Speedrating, Type, Stock) VALUES (%s, %s, %s, %s, %s, %s)'
    Parameters = (data['Brand'], data['Model'], data['Loadrating'], data['Speedrating'], data['Type'], data['Stock'])
    sql_write_query(query, Parameters)

    return jsonify({'message': 'Tire added successfully'})

# API Endpoint to update the Stock column of a Tire, provided a given ID
@app.route('/api/Inventory/<int:Tire_ID>', methods=['PUT'])
def update_Stock(Tire_ID):
    data = request.get_json()
    query = 'UPDATE Inventory SET Stock = %s WHERE ID = %s'
    Parameters = (data['Stock'], Tire_ID)
    sql_write_query(query, Parameters)

    return jsonify({'message': 'Stock updated successfully'})

# API Endpoint to delete a Tire, provided a given ID
@app.route('/api/Inventory/<int:Tire_ID>', methods=['DELETE'])
def delete_Tire(Tire_ID):
    query = 'DELETE FROM Inventory WHERE ID = %s'
    Parameters = (Tire_ID,)
    sql_write_query(query, Parameters)

    return jsonify({'message': 'Tire deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)


