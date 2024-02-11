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

# Function to get drink information
def get_drink_info(cursor, drink_id):
    cursor.execute("SELECT Description, Color FROM Drinks WHERE id = %s", (drink_id,))
    drink_info = cursor.fetchone()
    
    if drink_info:
        print(f"Description: {drink_info[0]}")
        print(f"Color: {drink_info[1]}")
    else:
        print("Sorry, Drink not found in menu")

# Function for placing the order
def place_order(cursor):
    order = []
    
    while True:
        display_drinks(cursor)
        answer = input("Welcome! Are you ready to place an order? (yes/no): ").upper()
        
        if answer == 'NO':
            break
        elif answer == 'YES':
            drink_id = int(input("Please enter the drink number you would like to order from the menu: "))
            get_drink_info(cursor, drink_id)
            
            quantity = int(input("Please enter how many servings you would like: "))
            order.append((drink_id, quantity))
            
            add_another = input("Would you like to add another drink to your order? (yes/no): ").upper()
            if add_another != 'YES':
                break

    return order
