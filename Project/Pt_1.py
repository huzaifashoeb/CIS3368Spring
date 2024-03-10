#Student Name: Huzaifa Shoeb, ID: 1925670
#Project part 1 CIS 3368 (11AM to 1PM) Code

# Importing all the tools that might by needed for this code (SQL, Flask, Hashlib, Datetime, Creds)
import mysql.connector
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
import hashlib
import datetime
import time
import creds
import flask
from flask import Flask
from flask import jsonify
from flask import request, make_response
from flask import abort      # Importing 'abort' from the module Flask for this part - saw this on Stack Overflow

# # Connect to the MySQL database, I have put this information here so I do not have to submit multiple files, using same setup from my HW 2 submission
connection = mysql.connector.connect(
     host="cis3368spring.c7ykkkkkq29g.us-east-1.rds.amazonaws.com",
     user="admin",
     password="saturnskyblack",
     database="cis3368springdb"
       )

#Below is my code for the MySQL part of this project. Including here as comments for future references.
# CREATE TABLE Facility (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     Name VARCHAR(255) NOT NULL
# );

# CREATE TABLE Classroom (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     Capacity INT NOT NULL,
#     Name VARCHAR(255) NOT NULL,
#     Facility_id INT,
#     FOREIGN KEY (Facility_id) REFERENCES Facility(id)
# );

# CREATE TABLE Teacher (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     Firstname VARCHAR(255) NOT NULL,
#     Lastname VARCHAR(255) NOT NULL,
#     Room INT,
#     FOREIGN KEY (Room) REFERENCES Classroom(id)
# );

# CREATE TABLE Child (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     Firstname VARCHAR(255) NOT NULL,
#     Lastname VARCHAR(255) NOT NULL,
#     Age INT NOT NULL,
#     Room INT,
#     FOREIGN KEY (Room) REFERENCES Classroom(id)
# );

# Confirming the connection to the db is established
if connection.is_connected():
    print("Connection to MySQL databse successful!")

# Checking if the connection to db was not successful
def error_connecting():
    if not connection.is_connected():
        return jsonify({"message": "There was an Error in establishing connection to the MySQL Database"}), 200

# Creating the application for flask fo CRUD operations
app = Flask(__name__)



# CRUD Operations part of the Project
# CRUD operations for the Facilities
# GET for Facilities
@app.route('/Facilities', methods=['GET'])
def Facilities_grab():
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Facility")
        Facilities = cursor.fetchall()
        return jsonify(Facilities)
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# POST for Facilities
@app.route('/Facilities', methods=['POST'])
def add_Facility():
    try:
        data = request.get_json()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Facility (name) VALUES (%s)", (data['name'],))
        connection.commit()
        return jsonify({"message": "New Facility is now available for use!"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()


# PUT for Facilities
@app.route('/Facilities/<int:Facility_id>', methods=['PUT'])
def update_Facility(Facility_id):
    try:
        data = request.get_json()
        cursor = connection.cursor()
        cursor.execute("UPDATE Facility SET name = %s WHERE id = %s", (data['name'], Facility_id))
        connection.commit()
        return jsonify({"message": "Facility update successful!"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()


# DELETE for Facilities
@app.route('/Facilities/<int:Facility_id>', methods=['DELETE'])
def delete_Facility(Facility_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Facility WHERE id = %s", (Facility_id,))
        connection.commit()
        return jsonify({"message": "Facility is deleted and unavailable for use now!"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

