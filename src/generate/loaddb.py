# This file contains code for loading password hashes into the database
#
# Author: Josh McIntyre
#
import mysql.connector

import auth

# Define a class for loading password hashes into the database
class HashLoader:

    # Constants
    LOAD_QUERY = "INSERT INTO PwHashes (Hash, Password) VALUES (%s, %s)"

    # Initialize the database connection
    def __init__(self):

        try:
            self.conn = mysql.connector.connect(user=auth.USER,
                                           password=auth.PASSWORD,
                                           host=auth.HOST,
                                           database=auth.DATABASE)
            self.cursor = self.conn.cursor(prepared=True)
        except mysql.connector.Error as err:
            print(f"Unable to connect to database: {err}")
 
    # Cleanup
    def __del__(self):

        self.conn.close()
        
    # Insert a password hash and corresponding password into the database
    def load_hash(self, password_hash, password):
    
        try:
            self.cursor.execute(self.LOAD_QUERY, (password_hash, password))
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Unable to insert record for {password}: {password_hash}: {err}")
    