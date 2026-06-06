import os
import sqlite3
from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

#Database name expenses.db
db_path=os.path.join(BASE_DIR,'expenses.db')

#Home page Add Expenses

@app.route("/",methods=["GET","POST"])
def expense():
    if request.method=="POST":
        name=request.form["name"]
        category=request.form["category"]
        amount=request.form["amount"]
        date=request.form["date"]
        conn=sqlite3.connect(db_path)
        cursor=conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,category TEXT,amount REAL,date TEXT)""")
        cursor.execute("""INSERT INTO expenses (name,category,amount,date) VALUES(?,?,?,?)""",(name,category,amount,date))
        conn.commit()
        conn.close()
        return """<h1 style='color:white; background-color:black; padding:20px; text-align:center'>Your expenses added successfully!</h1>"""
    return render_template('expense.html')

#View Expenses 

@app.route("/view",methods=["GET","POST"])
def view():
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    data=cursor.fetchall()
    conn.close()
    return render_template('view.html',data=data)

#Update expenses

@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    if request.method=="POST":
        name=request.form["name"]
        category=request.form["category"]
        amount=request.form["amount"]
        date=request.form["date"]
        cursor.execute("""UPDATE expenses SET  name=?,category=?,amount=?,date=? WHERE id=?""",(name,category,amount,date,id))
        conn.commit()
        conn.close()
        return """<h1 style='color:black;background-color:pink;padding:20px;text-align:center;'> "Update successfully"</h1>"""
    cursor.execute("SELECT * FROM expenses WHERE id=?",(id,))
    data=cursor.fetchone()
    conn.close()
    return render_template("update.html",data=data)

#Delete expenses

@app.route("/delete/<int:id>")
def delete(id):
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id=?",(id,))
    conn.commit()
    conn.close()
    return """<h1 style='color:white;background-color:blue;padding:20px;text-align:center;'> "Deleted Successfully"</h1>"""

app.run(debug=True)