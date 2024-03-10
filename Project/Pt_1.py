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
