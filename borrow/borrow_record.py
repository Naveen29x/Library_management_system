import pymysql
from  database.connection import conn
from datetime import date


def new_borrow_records( borrow_id: int, book_id: int, member_id: int, 
                       borrow_date: date, return_date: date, status_of_book: int):
    try:
         cursor=conn.cursor()
         query="insert into borrow_records(borrow_id,book_id,member_id,borrow_id,return_date,status_of_book) " \
         "values(%s,%s,%s,%s,%s,%s)"
         values=(borrow_id,book_id,member_id,member_id, borrow_date,return_date,status_of_book)
         cursor.execute(query,values)
         conn.commit()
    except pymysql.MySQLError as e:
         conn.rollback()
         print(e)
         return     



                     



