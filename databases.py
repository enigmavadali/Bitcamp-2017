import sqlite3 as sql
conn = sql.connect("healthbuddy.db")


conn.execute("CREATE TABLE p_info (p_id TEXT, p_date TEXT, p_illness TEXT, p_test TEXT, p_presc TEXT, p_comments TEXT, p_diet TEXT) ")
