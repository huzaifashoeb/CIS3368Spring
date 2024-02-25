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
