import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user="root",
    port = 3306 ,   
    database = "projectwork"
)
print(db)

terminal() = db.cursor
#insert
query = "Insert INTO student (name, address, phone) VALUES ('sujan', 'dang', 1230);"
terimnal.execute(query)
db.commit()

#update
query = "UPDATE Student SET phone = '9800' where id = 3;"
terminal.execute(query)
db.commit() 

#delete
query = "DELETE FROM student WHERE id = 2"
terminal.execute(query)
db.commit

#fetch data 
query = "select * from student"
terminal.execute (query)
result = terminal.fetchall()
print(result)
for i in result:
    print(i)
    print(list(i))
print(db)
