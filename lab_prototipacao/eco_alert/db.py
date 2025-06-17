import sqlite3
import pandas as pd

def create_tables():
    conn = sqlite3.connect("ecoalert.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY, name TEXT, password TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT, descricao TEXT, tipo TEXT, risco TEXT,
        data TEXT, local TEXT, latitude REAL, longitude REAL, arquivo TEXT)""")
    conn.commit()
    conn.close()

def register_user(name, email, password):
    conn = sqlite3.connect("ecoalert.db")
    conn.execute("INSERT INTO users VALUES (?, ?, ?)", (email, name, password))
    conn.commit()
    conn.close()

def check_user(email, password):
    conn = sqlite3.connect("ecoalert.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    return c.fetchone() is not None

def save_report(**kwargs):
    conn = sqlite3.connect("ecoalert.db")
    conn.execute("""INSERT INTO reports 
        (email, descricao, tipo, risco, data, local, latitude, longitude, arquivo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (kwargs["email"], kwargs["descricao"], kwargs["tipo"], kwargs["risco"],
         kwargs["data"], kwargs["local"], kwargs["latitude"], kwargs["longitude"], kwargs["arquivo"])
    )
    conn.commit()
    conn.close()

def get_reports():
    conn = sqlite3.connect("ecoalert.db")
    df = pd.read_sql_query("SELECT * FROM reports", conn)
    conn.close()
    return df
