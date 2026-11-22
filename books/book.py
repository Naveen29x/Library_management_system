from sqlite3 import Cursor

import pymysql
from database.connection import conn


def add_books(book_id :int ,title:str,author:str,quantity:int,availabel_quantity:int):
    try:
        
        cursor=conn.cursor()
        query="insert into books(book_id,title,author,quantity,availabel_quantity) values (%s,%s,%s,%s,%s)"
        values=(book_id,title,author,quantity,availabel_quantity) 
        cursor.execute(query,values)
        conn.commit()
        return {"MESSAGE":"Student added succesfully"}
    except pymysql.MySQLError as e:
        print("eorr:",e)
        conn.rollback()
        return {"we got an error"}

def show_books():
    try:
        cursor=conn.cursor()
        cursor.execute("select * from books")
        ans=cursor.fetchall()
        print(ans)
        conn.commit()
        return {"messge":"student seen succesfuly"}
        
    except pymysql.MySQLError as e:
        print("error",e)
        conn.rollback()
        return{"we got error"}

def search_book_by_id(id:int):
    try:
        cursor=conn.cursor()
        cursor.execute("select * from books where book_id=%s",id)
        ans=cursor.fetchone()    
        print(ans)
        conn.commit()
    except pymysql.MySQLError as e:
        print("Error",e)
        conn.rollback()
        return{"we got an error"}    

def update_book_by_id(id:int):
    new_quantity= int(input("Enter the new book quantity::::"))
    new_available_quanty=int(input("Enter the new avaialble quantyt"))
    try:
        Cursor=conn.cursor()
        Cursor.execute("update books set quantity=%s,availabel_quantity=%s where book_id=%s",(new_quantity,new_available_quanty,id))
        print("Updated successfuly")
        conn.commit()

    except pymysql.MySQLError as e:
        print("error",e)
        conn.rollback()
        return {
            "we got an error"
        }

def delete_book_by_id(id:int):
    try:

        cursor=conn.cursor()
        cursor.execute("select * from books where book_id=%s",(id,))
        data=cursor.fetchone()
        if data is None:
            return{ 
                "message":"Data not available"
                }
        cursor.execute("Delete from books where book_id=%s",(id,))
        conn.commit()
        
    except pymysql.MySQLError as e:
        print("error",e)
        conn.rollback()
        return{
            "we got error"
        }    

        
        











