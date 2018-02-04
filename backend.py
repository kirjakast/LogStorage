import sqlite3

def connect():
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS logpath (id INTEGER PRIMARY KEY, application text, environment text, log_path text, log_type text, log_note text)")
    conn.commit()
    conn.close()

def insert(application,environment,log_path,log_type,log_note):
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO logpath VALUES (NULL,lower(?),lower(?),lower(?),lower(?),?)",(application,environment,log_path,log_type,log_note))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM logpath ORDER BY application ASC")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(application="",environment="",log_path="",log_type="",log_note=""):
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()

    dict = {}
    if application != "":
        dict['application'] = application
    if environment != "":
        dict['environment'] = environment
    if log_path != "":
        dict['log_path'] = log_path
    if log_type != "":
        dict['log_type'] = log_type
    if log_note != "":
        dict['log_note'] = log_note

    t = []
    l = []
    for k,v in dict.items():
            t.append(k)
            l.append(v)

    if len(l) == 5:
        cur.execute("SELECT * FROM logpath WHERE " + t[0]+"=? AND " + t[1]+"=? AND "+ t[2]+"=? AND "+ t[3]+"=? AND "+ t[4]+"=? ORDER BY environment DESC", (l[0],l[1],l[2],l[3],l[4],))
    elif len(l) == 4:
        cur.execute("SELECT * FROM logpath WHERE " + t[0]+"=? AND " + t[1]+"=? AND "+ t[2]+"=? AND "+ t[3]+"=? ORDER BY environment DESC", (l[0],l[1],l[2],l[3],))
    elif len(l) == 3:
        cur.execute("SELECT * FROM logpath WHERE " + t[0]+"=? AND " + t[1]+"=? AND "+ t[2]+"=? ORDER BY environment DESC", (l[0],l[1],l[2],))
    elif len(l) == 2:
        cur.execute("SELECT * FROM logpath WHERE " + t[0]+"=? AND " + t[1]+"=? ORDER BY environment DESC" , (l[0],l[1],))
    elif len(l) == 1:
        cur.execute("SELECT * FROM logpath WHERE " + t[0]+"=? ORDER BY environment DESC" , (l[0],))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM logpath WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,application,environment,log_path,log_type,log_note):
    conn=sqlite3.connect("baas.db")
    cur=conn.cursor()
    cur.execute("UPDATE logpath SET application=lower(?), environment=lower(?), log_path=lower(?), log_type=lower(?), log_note=? WHERE id=?",(application,environment,log_path,log_type,log_note,id))
    conn.commit()
    conn.close()
connect()
