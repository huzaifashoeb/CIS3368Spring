#Student name: Huzaifa Shoeb, ID: 1925670
#Following is the Python Code for Homework 1

import mysql.connector
from mysql.connector import Error

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="cis3368spring.c7ykkkkkq29g.us-east-1.rds.amazonaws.com",
    user="admin",
    password="saturnskyblack",
    database="cis3368springdb"
)

#Function for Displaying the menu of drinks and the information
def display_drinks(cursor):
    cursor.execute("SELECT id, Drink, Price FROM Drinks")
    drinks = cursor.fetchall()

    for drink in drinks:
        print(f"{drink[0]} - {drink[1]}: ${drink[2]}")

def get_drink_info(cursor, drink_id):
    cursor.execute("SELECT Description, Color FROM Drinks WHERE id = %s", (drink_id,))
    drink_info = cursor.fetchone()

    if drink_info:
        print(f"Description: {drink_info[0]}")
        print(f"Color: {drink_info[1]}")
    else:
        print("Sorry, Drink not found in the menu")   #If a number is entered which is not found in menu

def place_order(cursor):
    order = []
    drink_info_requested = False  # This Boolean is to check if the user requested information on a drink

    while True:
        if not drink_info_requested:
            display_drinks(cursor)

        answer = input("Welcome! Would you like information about a drink from our menu or to place an order? (i = Description / o = Order / c = Checkout): ").upper()
#Using the .upper() function to make sure user input is not case sensitive
        if answer == 'C':
            break
        elif answer == 'I':
            drink_id = int(input("Certainly! Please enter the drink number you would like the description of: "))
            get_drink_info(cursor, drink_id)
            drink_info_requested = True   #This Boolean helps to hide the menu and not repeat it after each step of order
        elif answer == 'O':
            drink_id = int(input("Please enter the drink number you would like to order from the menu: "))
            get_drink_info(cursor, drink_id)

            quantity = int(input("Please enter how many servings you would like: "))
            order.append((drink_id, quantity))

# Ask user if they want to add anyhting else to the order
            add_another = input("Would you like to add another drink to your order? (y = yes / n = no): ").upper()
            if add_another != 'Y':order
            drink_info_requested = False  # Display the menu again if the order is completed 

    return order

def print_receipt(order, cursor):
    total = 0

# Reciept for the user
    print("\nReceipt:")
    for items in order:
        drink_id, quantity = items
        cursor.execute("SELECT Drink, Price FROM Drinks WHERE id = %s", (drink_id,))
        drink_info = cursor.fetchone()

        if drink_info:
            drinkname, price = drink_info
            total += price * quantity
            print(f"{quantity} x {drinkname}: ${price * quantity}")

    print(f"\nTotal: ${total:.2f}")

try:
    cursor = db_connection.cursor()

    while True:
        order_or_info = input("Welcome! Would you like information about a drink from our menu or to place an order? (i = Description / o = Order / c = Checkout): ").upper()

        if order_or_info == 'C':
            break
        elif order_or_info == 'I':
            drink_id = int(input("Please enter the drink number you would like information about: "))
            get_drink_info(cursor, drink_id)
        elif order_or_info == 'O':
            order = place_order(cursor)
            print_receipt(order, cursor)

except mysql.connector.Error as e:
    print(f"Error: {e}")
