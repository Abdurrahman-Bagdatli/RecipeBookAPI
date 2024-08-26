from flask import Flask,request,jsonify
from flask_cors import CORS
import pymysql

app=Flask(__name__)
CORS(app)

def db_connection_database():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Abdr20087434",
        database="sweetsalty",
    )


@app.route("/breakfast",methods=["GET"])
def get_Breakfast():
 connection = db_connection_database()
 cursor = connection.cursor()
 try:
  sql = "SELECT * FROM breakfast"
  cursor.execute(sql)
  rows = cursor.fetchall()
  column = [desc[0] for desc in cursor.description]
  result = [dict(zip(column,row)) for row in rows]  
  return jsonify(result) ,200
 finally:
   cursor.close()
   connection.close()

@app.route("/lunch", methods=["GET"])
def get_lunch():
    connection = db_connection_database()
    cursor = connection.cursor()
    try:
        sql = "SELECT * FROM lunch"
        cursor.execute(sql)
        rows = cursor.fetchall()
        column = [desc[0] for desc in cursor.description]
        result = [dict(zip(column, row)) for row in rows]
        return jsonify(result), 200
    finally:
        cursor.close()
        connection.close()

@app.route("/dinner",methods=["GET"])
def get_Dinner():
  connection = db_connection_database()
  cursor = connection.cursor()
  try:
    sql = "Select * from dinner"
    cursor.execute(sql)
    rows = cursor.fetchall()
    column = [desc[0] for desc in cursor.description ]
    result =[dict(zip(column,row)) for row in rows]
    return jsonify(result)
  finally:
    cursor.close()
    connection.close()

@app.route("/allmeals",methods=["GET"])
def all_meals():
 connection = db_connection_database()
 cursor = connection.cursor()
 try:
   sql = "Select * from allmeals"
   cursor.execute(sql)
   rows =cursor.fetchall()
   column = [desc[0] for desc in cursor.description]
   result = [dict(zip(column,row)) for row in rows]
   return jsonify(result)
 finally:
   cursor.close()
   connection.close() 
    


if __name__ == "__main__":
   app.run(host="0.0.0.0",port=5000,debug=True)