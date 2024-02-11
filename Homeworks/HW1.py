#Student name: Huzaifa Shoeb, ID: 1925670
#The databse is in MySQL, 11 drinks added to the table 'Drinks' with unique auto generating IDs. Following is the Python Code for Homework 1

import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

# Create a connection to mysql database
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.username, myCreds.password, myCreds.dbname)

# add a table for drinks
create_drinks_table = """
CREATE TABLE IF NOT EXISTS Drinks(
    id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    Drink VARCHAR(255) NOT NULL,
    Price INT NOT NULL,
    Color VARCHAR(255) NOT NULL,
    Description VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
) """

execute_query(conn, create_drinks_table)
