from flask import Flask, render_template, request, url_for
import sqlite3 as sql

con = sql.connect("healthbuddy.db")

cur = con.cursor()
cur.executescript("""
        INSERT INTO p_info VALUES("123","23-02-2017","Diabetes","Sugar Level","Metformin","Sugar level is above normal"," low sucrose diet for 3 months");
        INSERT INTO p_info VALUES("312","12-01-2017","Jaundice","liver function test","Acetaminophen/naproxen","has shown symptoms of jaundice","avoid fried food and drink plenty of water");
        INSERT INTO p_info VALUES("213","29-12-2016","Leptospirosis","skin test","Doxycycline/Chloramphenicol","Patient has shown improvement","reduce fatty food ");
        INSERT INTO p_info VALUES("222","13-03-2017","Lymphatic filariasis","microfilariae","albendazole","No past History","low fat high protein diet with probiotics");
        INSERT INTO p_info VALUES("312","18-03-2017","Cirrhosis","liver test","Tylenol/ibuprofen","the previous jaundice has elevated to Cirrhosis","reduce alcohol consumption");
        """)

con.commit()

@app.route("/ngo")
def ngo():
    return render_template("ngo.html")