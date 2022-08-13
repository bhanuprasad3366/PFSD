import sqlite3
conn = sqlite3.connect('pfsd2.db')
print("opened data succesfully")
conn.execute('''CREATE TABLE student1(ID number,name text,subject1 text,subject2 text,subject3 text)''')
print("table is created successfully")
data1 = [(2100032222, 'raju', 'python', 'dbms', 'cns'), (2100038574, 'kiran', 'python', 'dbms', 'cns')]
conn.execute("INSERT INTO student1 values (2100032221,'bhanu prasad','python','dbms','cns')")
conn.execute("INSERT INTO student1 values (2100032222,'varun','msd','sql','gdf')")
cur = conn.cursor()
cur.executemany('INSERT INTO student1 VALUES(?,?,?,?,?);', data1)
print("inserted succesfully")
for row in cur.execute('SELECT * FROM student1'):
    print(row)