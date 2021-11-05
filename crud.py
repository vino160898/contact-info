from flask import *
import sqlite3
app = Flask(__name__)

@app.route("/")  #decorator 
def index():
    return render_template("index.html");

@app.route("/add")
def add():   
    return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            address = request.form["address"]
            city = request.form["city"]
            state = request.form["state"]
            country = request.form["country"]
            with sqlite3.connect("/home/vino/Documents/oo/Address-Book-master/data.db") as con:
                cur = con.cursor()   
                cur.execute("INSERT into Address (name, email,phone, address, city, state, country) values (?,?,?,?,?,?,?)",(name,email,phone,address,city,state,country))
                con.commit()
                msg = "Contact successfully Added"   
        except:
            con.rollback()
            msg = "We can not add Contact to the list"
        finally:
            return render_template("success.html",msg = msg)
            con.close()
@app.route("/view")
def view():
    con = sqlite3.connect("/home/vino/Documents/oo/Address-Book-master/data.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Address")   
    rows = cur.fetchall()
    return render_template("view.html",rows = rows)

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])   
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("/home/vino/Documents/oo/Address-Book-master/data.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Address where id = ?",id)
            msg = "Contact successfully deleted"   
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html",msg = msg)

if __name__ == "__main__":
    app.run(debug = True)  
