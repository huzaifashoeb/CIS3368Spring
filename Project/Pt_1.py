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

