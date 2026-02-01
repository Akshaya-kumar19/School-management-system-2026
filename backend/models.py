import mysql.connector
from config import Config

class Database : 
    def __init__(self):
        self.connection = None

    def connect(self):
        '''Create databse connection'''
        if not self.connection or not self.connection.is_connected():
            self.connection = mysql.connector.connect(
                host = Config.MYSQL_HOST,
                user = Config.MYSQL_USER,
                password = Config.MYSQL_PASSWORD,
                database = Config.MYSQL_DB
            )

        return self.connection
    
    def disconnect(self):
        """Close the database Connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, params = None, fetch = True):
        try : 
            connection = self.connect()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params or ())

            if fetch : 
                result = cursor.fetchall()
                cursor.close()
                return result
            else : 
                connection.commit()
                last_id = cursor.lastrowid
                cursor.close()
                return last_id
        except mysql.connector.Error as err :
            print(f"Database error: {err}")
            raise
        finally:
            self.disconnect()

db = Database()
                