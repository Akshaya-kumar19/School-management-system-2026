import os
class Config:
    #  database
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DB", 'school_management')


    # secret key
    SECRET_KEY = os.getenv("SECRET_KEY", "secret-key-which-change-in-production")

    # cors header 
    CORS_HEADERS = 'Content-Type'