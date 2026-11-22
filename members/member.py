
import pymysql
from database.connection import conn

#regiter new user

def new_user(member_id:int,member_name:str,email:str,phone_no:int):
    try:
        cursor=conn.cursor()
        query="insert into person(member_id,member_name,email,phone)values (%s,%s,%s,%s) "
        values=(member_id,member_name,email,phone_no)
        cursor.execute(query,values)
        conn.commit()
        print("succesfully added")
    except pymysql.MySQLError as e:
        print(e)
        conn.rollback()
        return


def show_person():
    try:
        cursor=conn.cursor()
        cursor.execute("select * from person")
        ans=cursor.fetchall()
        cursor.commit()
        print(ans)
        
    except pymysql.MySQLError as e:
        print(e)
        conn.rollback()
        return    
def member_by_id(id:int):
    try:
        cursor=conn.cursor()
        cursor.execute("select * from person where member_id=%s ",(id,))
        result=cursor.fetchone()
        print(result)
    except pymysql.MySQLError as e:
        print(e)
        conn.rollback
        return    

            
        



       


