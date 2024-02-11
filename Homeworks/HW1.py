#Student name: Huzaifa Shoeb, ID: 1925670
#Following is the Python Code for Homework 1

import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="cis3368spring.c7ykkkkkq29g.us-east-1.rds.amazonaws.com",
    user="admin",
    password="saturnskyblack",
    database="cis3368springdb"
)

# Function to display all the drinks in database
def display_drinks(cursor):
    cursor.execute("SELECT id, Drink, Price FROM Drinks")
    drinks = cursor.fetchall()
    
    for drink in drinks:
        print(f"{drink[0]} - {drink[1]}: ${drink[2]}")
