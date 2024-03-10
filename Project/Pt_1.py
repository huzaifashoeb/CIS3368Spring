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
    print("Connection to MySQL database successful!")

# Checking if the connection to db was not successful
def error_connecting():
    if not connection.is_connected():
        return jsonify({"message": "There was an Error in establishing connection to the MySQL Database"}), 500

# Creating the application for flask fo CRUD operations
app = Flask(__name__)



# CRUD Operations part of the Project
# CRUD operations for the Facility
# GET for Facility
@app.route('/Facility', methods=['GET'])
def Facility_grab():
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Facility")
        Facility = cursor.fetchall()
        return jsonify(Facility)
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# POST for Facility
@app.route('/Facility', methods=['POST'])
def add_Facility():
    try:
        data = request.get_json()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Facility (Name) VALUES (%s)", (data['Name'],))
        connection.commit()
        return jsonify({"message": "New Facility is now available for use!"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()


# PUT for Facility
@app.route('/Facility/<int:Facility_id>', methods=['PUT'])
def update_Facility(Facility_id):
    try:
        data = request.get_json()
        cursor = connection.cursor()
        cursor.execute("UPDATE Facility SET Name = %s WHERE id = %s", (data['Name'], Facility_id))
        connection.commit()
        return jsonify({"message": "Facility update successful!"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()


# DELETE for Facility
@app.route('/Facility/<int:Facility_id>', methods=['DELETE'])
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


# CRUD operations for the Classroom
# GET for Classroom
@app.route('/Classroom', methods=['GET'])
def Classroom_grab():
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Classroom")
        Classroom = cursor.fetchall()
        return jsonify(Classroom)
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# POST for Classroom
@app.route('/Classroom', methods=['POST'])
def add_Classroom():
    try:
        data = request.get_json()
        Facility_id = data.get('Facility_id')
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Facility WHERE id = %s", (Facility_id,))
        Facility = cursor.fetchone()
        cursor.close()

        # Checking to make sure that a Facility exists for Classroom to add
        if not Facility:
            return jsonify({"message": f"The Facility {Facility_id} does not exist"}), 404

        # Add the Classroom if the Facility exists
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Classroom (Capacity, Name, Facility_id) VALUES (%s, %s, %s)", 
                       (data['Capacity'], data['Name'], Facility_id))
        connection.commit()
        return jsonify({"message": "The Classroom is added and ready to be assigned!"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# PUT for Classroom
@app.route('/Classroom/<int:Classroom_id>', methods=['PUT'])
def update_Classroom(Classroom_id):
    try:
        data = request.get_json()
        Facility_id = data.get('Facility_id')
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Facility WHERE id = %s", (Facility_id,))
        Facility = cursor.fetchone()
        cursor.close()

        # Check if the Facility_id exists
        if not Facility:
            return jsonify({"message": f"The Facility {Facility_id} does not exist"}), 404

        # Update the Classroom if the Facility exists
        cursor = connection.cursor()
        cursor.execute("UPDATE Classroom SET Capacity = %s, Name = %s, Facility_id = %s WHERE id = %s", 
                       (data['Capacity'], data['Name'], Facility_id, Classroom_id))
        connection.commit()
        return jsonify({"message": "Classroom update successful!"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# DELETE for Classroom
@app.route('/Classroom/<int:Classroom_id>', methods=['DELETE'])
def delete_Classroom(Classroom_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Classroom WHERE id = %s", (Classroom_id,))
        connection.commit()
        return jsonify({"message": "The Classroom is deleted and not available for assignment anymore!"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()


# CRUD operations for the Teacher
# GET for Teacher
@app.route('/Teacher', methods=['GET'])
def Teacher_grab():
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Teacher")
        Teacher = cursor.fetchall()
        return jsonify(Teacher)
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# POST for Teacher
@app.route('/Teacher', methods=['POST'])
def add_Teacher():
    try:
        data = request.get_json()
        Room_id = data.get('Room')
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Classroom WHERE id = %s", (Room_id,))
        Room = cursor.fetchone()
        cursor.close()

        # Check if the Room exists
        if not Room:
            return jsonify({"message": f"Classroom {Room_id} does not exist"}), 404
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT COUNT(*) as count FROM Teacher WHERE Room = %s", (Room_id,))
        Teacher_count = cursor.fetchone()['count']
        cursor.close()

        # Check to see if adding the Teacher will exceeds the limit of 10 Children per Teacher
        if Teacher_count >= 10:
            return jsonify({"message": f"Cannot add to this Room {Room_id}. Maximum capacity has been reached. Please try a different Room. You can also add a new Classroom!"}), 400

        # Add the Teacher if the Room exists and the limit is not exceeded
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Teacher (Firstname, Lastname, Room) VALUES (%s, %s, %s)",
                       (data['Firstname'], data['Lastname'], Room_id))
        connection.commit()
        return jsonify({"message": "Teacher assigned successfully"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# PUT for Teacher
@app.route('/Teacher/<int:Teacher_id>', methods=['PUT'])
def update_Teacher(Teacher_id):
    try:
        data = request.get_json()
        Room_id = data.get('Room')
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Classroom WHERE id = %s", (Room_id,))
        Room = cursor.fetchone()
        cursor.close()

        if not Room:
            return jsonify({"message": f"Classroom {Room_id} does not exist"}), 404

        # Check if updating the Teacher exceeds the maximum limit of 10 Child per Teacher
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT COUNT(*) as count FROM Teacher WHERE Room = %s AND id != %s", (Room_id, Teacher_id))
        Teacher_count = cursor.fetchone()['count']
        cursor.close()

        if Teacher_count >= 10:
            return jsonify({"message": f"Cannot update Teacher in Room {Room_id}. Capacity has been reached!"}), 400

        # Continue if the Room exists and the capacity is not reached
        cursor = connection.cursor()
        cursor.execute("UPDATE Teacher SET Firstname = %s, Lastname = %s, Room = %s WHERE id = %s",
                       (data['Firstname'], data['Lastname'], Room_id, Teacher_id))
        connection.commit()
        return jsonify({"message": "Teacher update successful!"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# DELETE for Teacher
@app.route('/Teacher/<int:Teacher_id>', methods=['DELETE'])
def delete_Teacher(Teacher_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Teacher WHERE id = %s", (Teacher_id,))
        connection.commit()
        return jsonify({"message": "The Teacher has been Removed successfully!"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()


# CRUD operations for Child
# GET for Child
@app.route('/Child', methods=['GET'])
def Child_grab():
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Child")
        Child = cursor.fetchall()
        return jsonify(Child)
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# POST for Child
@app.route('/Child', methods=['POST'])
def add_Child():
    try:
        data = request.get_json()
        Room_id = data.get('Room_id')
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Classroom WHERE id = %s", (Room_id,))
        Room = cursor.fetchone()
        cursor.close()

        if not Room:
            return jsonify({"message": f"Classroom {Room_id} does not exist"}), 404

        # Check if the Teacher is already watching 10 Children at full capacity
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM Child WHERE Room_id = %s", (Room_id,))
        Child_count = cursor.fetchone()[0]
        cursor.close()

        if Child_count >= 10:
            return jsonify({"message": "Teacher is already watching 10 Children in this Classroom! More Students cannot be assigned."}), 400

        # Add the Child if the Room exists and the capacity of 10 children per teacher is not reached
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Child (Firstname, Lastname, Age, Room_id) VALUES (%s, %s, %s, %s)", 
                       (data['Firstname'], data['Lastname'], data['Age'], Room_id))
        connection.commit()
        return jsonify({"message": f"Child was added to the {Room_id} room successfully"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# PUT for Child
@app.route('/Child/<int:Child_id>', methods=['PUT'])
def update_Child(Child_id):
    try:
        data = request.get_json()
        Room_id = data.get('Room_id')

        # Check if the specified Room_id exists
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Classroom WHERE id = %s", (Room_id,))
        Room = cursor.fetchone()
        cursor.close()

        if not Room:
            return jsonify({"message": f"Classroom with id {Room_id} does not exist"}), 404

        # Check if the Teacher is already watching 10 Child
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM Child WHERE Room_id = %s AND id != %s", (Room_id, Child_id))
        Child_count = cursor.fetchone()[0]
        cursor.close()

        if Child_count >= 10:
            return jsonify({"message": "Teacher is already watching 10 Child in this Classroom"}), 400

        # Update the Child if the Room exists and the limit is not reached
        cursor = connection.cursor()
        cursor.execute("UPDATE Child SET Firstname = %s, Lastname = %s, Age = %s, Room_id = %s WHERE id = %s", 
                       (data['Firstname'], data['Lastname'], data['Age'], Room_id, Child_id))
        connection.commit()
        return jsonify({"message": "Child updated successfully"})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

# DELETE for Child
@app.route('/Child/<int:Child_id>', methods=['DELETE'])
def delete_Child(Child_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Child WHERE id = %s", (Child_id,))
        connection.commit()
        return jsonify({"message": "Child was successfully removed from room."})
    except Error as e:
        return error_connecting()
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
