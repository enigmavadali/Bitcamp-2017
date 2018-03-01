from flask import Flask, render_template, request, url_for,redirect,session
import sqlite3 as sql

conn = sql.connect("healthbuddy.db")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/doctor_signup")
def doctor():
    return render_template("doc-signup.html")


@app.route("/doc_put", methods=["POST", "GET"])
def doc_put():
    if request.method == "POST":
        try:
            adoc_id = request.form["Doc-id"]
            adoc_name = request.form["name"]
            adoc_qual = request.form["degree"]
            adoc_p = request.form["pass"]
            adoc_con=request.form["contact"]
            adoc_city=request.form["city"]
            adoc_email=request.form["mailid"]
            with sql.connect("healthbuddy.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO doc_profile (doc_id, doc_name, doc_qual, doc_p, doc_con,doc_email,doc_city)VALUES(?, ?, ?, ?, ?, ?,?)",(adoc_id, adoc_name, adoc_qual, adoc_p, adoc_con,adoc_email, adoc_city) )

                con.commit()
                msgd = "You have successfully signed up."
        except:
            con.rollback()
            msgd = "error: Please try again"

        finally:
            return render_template("result.html", msg=msgd)
            con.close()

@app.route("/patient_signup")
def patient():
    return render_template("patient-signup.html")

@app.route("/patient_put", methods=["POST", "GET"])
def patient_put():
    if request.method == "POST":
        try:
            bp_id = request.form["pid"]
            bp_name = request.form["pname"]
            bp_email = request.form["pmailid"]
            bp_p = request.form["ppass"]
            bp_con=request.form["cno"]
            bp_add1=request.form["phouse"]
            bp_add2=request.form["pstreet"]
            bp_city=request.form["pcityname"]
            bp_pincode=request.form["p-Pin-code"]
            bp_history=request.form["phis"]

            with sql.connect("healthbuddy.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO p_profile (p_id, p_name, p_email, p_p, p_con, p_add1, p_add2,p_city, p_pincode, p_history) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(bp_id, bp_name, bp_email, bp_p, bp_con, bp_add1, bp_add2,bp_city, bp_pincode,bp_history) )

                con.commit()
                msgp = "You have successfully signed up."
        except:
            con.rollback()
            msgp = "error: Please try again"

        finally:
            return render_template("result.html", msg=msgp)
            con.close()

# @app.route("/listd")
# def list():
#     con = sql.connect("healthbuddy.db")
#     con.row_factory = sql.Row
#
#     cur = con.cursor()
#     cur.execute("select * from doc_profile")
#
#     rows = cur.fetchall();
#     return render_template("listdoctor.html", rows=rows)

@app.route("/doctor_login")
def doctor_log():
    return render_template("Doc-log.html")

@app.route("/doctor_after_login")
def doctor_after_log():
    return render_template("doc-after-login.html")

@app.route("/patient_login")
def patient_log():
    return render_template("Pat-log.html")

@app.route("/check_id")
def check_id():
    if request.method == "POST":
        try:
            #session["u_id"] = request.form("U-id")
            uid= session["u_id"]
            with sql.connect("healthbuddy.db") as con:
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute("select * from p_info where p_id = 'uid'")
                con.commit()

                rows = cur.fetchall();
                return render_template("patient-histroy.html", rows=rows)
        except:
            con.rollback()

# @app.route("/patient_details")
# def pat_deatils():
#     id=session["u_id"]
#     con = sql.connect("healthbuddy.db")
#     con.row_factory = sql.Row
#
#     cur = con.cursor()
#     cur.execute("select * from p_info where p_id = 'id'")
#
#     rows = cur.fetchall();
#     return render_template("pat-details.html", rows=rows)

if __name__ == "__main__":
    app.run()