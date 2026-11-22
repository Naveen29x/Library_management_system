import os
from dotenv import load_dotenv

load_dotenv()

import pymysql



try:
    conn = pymysql.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="library_management_system",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)
    print("connection sucfull")

except pymysql.MySQLError as e:
    print("error as occured",e)


    

    




