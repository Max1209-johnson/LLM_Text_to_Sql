import sqlite3


## connect to sqlite


Connection=sqlite3.connect("student.db")


## Create a cursur object to insert record, create, table , retrieve


cursor=Connection.cursor()


#create the table
table_info="""
Create table STUDENT(NAME CARCHAR(25),CLASS VARCHAR(25), SEXTION VARCHAR(25), MARKS INT );

"""

cursor.execute(table_info)

## Insert Some more recors


cursor.execute(" ")


cursor.execute(''' Insert Into STUDENT values('Max', 'Consultant', 'A', 90)''')
cursor.execute(''' Insert Into STUDENT values('Chirag', 'Staff Consultant', 'B', 100)''')
cursor.execute(''' Insert Into STUDENT values('Ross', 'Consultant', 'C',200)''')
cursor.execute(''' Insert Into STUDENT values('Dillon', 'Consultant', 'D', 86)''')
cursor.execute(''' Insert Into STUDENT values('Raunak ', 'Consultant', 'E', 120)''')

## Display all the records

print("The inserted records are")


data=cursor.execute('''Select * From STUDENT''')



for row in data:
    print(row)




##Close the connection


Connection.commit()
Connection.close()

