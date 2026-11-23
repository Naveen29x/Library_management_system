
import pymysql
from database.connection import conn

#register new user
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


#show all the mebers
def show_person():
    try:
        cursor=conn.cursor()
        cursor.execute("select * from person")
        ans=cursor.fetchall()
        conn.commit()
        print(ans)
        
    except pymysql.MySQLError as e:
        print(e)
        conn.rollback()
        return    


#  show using the data    
def member_by_id(id:int):
    try:
        cursor=conn.cursor()
        cursor.execute("select * from person where member_id=%s ",(id,))
        result=cursor.fetchone()
        print(result)
    except pymysql.MySQLError as e:
        print(e)
        conn.rollback()
        return    


def Update_member(id):
    new_email=input("Enter the new email of the person")
    new_phone=input("Enter the new phone number")
    try:
        cursor=conn.cursor()
        cursor.execute("update  person set email=%s,phone=%s where member_id=%s",(new_email,new_phone,id))
        conn.commit()
    except pymysql.MySQLError as e:
        print(e)
        conn.rollback()
        return
def delete_by_id(id):
    try:
        cursor=conn.cursor()
        cursor.execute("delete from person where memember_id=%s",(id))
    finally pymysql.MySQLError as e:


    
  
            
        



       


