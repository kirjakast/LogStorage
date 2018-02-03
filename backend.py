import sqlite3

def connect():
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS logpath (id INTEGER PRIMARY KEY, application text, environment text, log_path text)")
    conn.commit()
    conn.close()

def insert(application,environment,log_path):
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO logpath VALUES (NULL,?,?,?)",(application,environment,log_path))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM logpath")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(application="",environment="",log_path=""):
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM logpath WHERE application=? OR environment=? OR log_path=?", (application,environment,log_path))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM logpath WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,application,environment,log_path):
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("UPDATE logpath SET application=?, environment=?, log_path=? WHERE id=?",(application,environment,log_path,id))
    conn.commit()
    conn.close()
connect()
#insert("SADHES","Live","/usr/home/list")
#delete(8)
#print(view())
#update(7,"SADHES","Koolitus","/home")
#print(view())
#print(search(application="SADHES"))
