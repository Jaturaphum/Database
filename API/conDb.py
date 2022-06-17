from time import time
import mysql.connector

class condb:
  def condb():
    mydb = mysql.connector.connect(
      host="localhost",
      user="project_coin",
      password="12345",
      database ="project_coin"
    )
    return mydb

class Con:
  def get_on_off(status):
    mydb = condb.condb()
    mycursor = mydb.cursor(dictionary=True)
    sql = "UPDATE coin SET status = '{}'".format(status)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()        
    return True
  
  def show_stack_all():
    mydb=condb.condb()
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT stack_coin FROM coin"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return data
  
  def show_all():
    mydb=condb.condb()
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM coin"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return data

  def show_stack_coin(id):
    mydb=condb.condb()
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT stack_coin FROM coin WHERE id = {}".format(id)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return data

  def get_stack_coin(stack_coin,id):
    mydb = condb.condb()
    mycursor = mydb.cursor(dictionary=True)
    sql = "UPDATE coin SET stack_coin = {} WHERE id = {}".format(stack_coin,id)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()        
    return True

  def reset_stack_coin(id):
    mydb = condb.condb()
    mycursor = mydb.cursor(dictionary=True)
    sql = "UPDATE coin SET stack_coin = 0 WHERE id = {}".format(id)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()        
    return True
  
  def reset_stack_coin_all():
    mydb = condb.condb()
    mycursor = mydb.cursor(dictionary=True)
    sql = "UPDATE coin SET stack_coin = 0".format()
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()        
    return True

  def update_status_id(status,id):
    mydb = condb.condb()
    mycursor = mydb.cursor(dictionary=True)
    sql = "UPDATE coin SET status = '{}' WHERE id = {}".format(status,id)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()        
    return True

  def show_all():
        mydb=condb.condb()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM coin"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

  def show_stack_coin(id):
        mydb=condb.condb()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT stack_coin FROM coin WHERE id = {}".format(id)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

  def get_stack_coin(stack_coin,id):
        mydb = condb.condb()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE coin SET stack_coin = {} WHERE id = {}".format(stack_coin,id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()        
        return True

  def reset_stack_coin(id):
        mydb = condb.condb()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE coin SET stack_coin = 0 WHERE id = {}".format(id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()        
        return True


  def update_status_id(status,id):
        mydb = condb.condb()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE coin SET status = '{}' WHERE id = {}".format(status,id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()        
        return True

  def Add_coin_1():
        mydb = condb.condb()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE coin SET stack_coin =stack_coin+1 WHERE id = 1"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()        
        return True
