# This file contains code for searching password hashes in the database
#
# Author: Josh McIntyre
#
import mysql.connector

import auth

# Define a class for searching passwords in the database
class HashSearcher:

    # Constants
    SEARCH_QUERY = "SELECT Hash, Password FROM PwHashes WHERE Hash = %s"

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
        
    # Search for a password hash in the database
    # Return a tuple of (password_hash, password) if found
    # Return None if no suitable hash is found
    def search_hash(self, password_hash):
    
        self.cursor.execute(self.SEARCH_QUERY, (password_hash,))
        result = list(self.cursor)
        if result:
            password_hash, password = result[0]
            return (password_hash, password)
        return None
    