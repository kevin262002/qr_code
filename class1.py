from tkinter import *
import mysql.connector
import smtplib, ssl
import qrcode

top = Tk()
top.geometry("250x250")

def insert():
    idd = t1.get()
    name = t2.get()
    sal = t3.get()
    date = t4.get()
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="emp_data"
        )

    mycur=mydb.cursor()

    sql = "insert into emp_detail(emp_id,emp_name,salary,join_date)values(%s,%s,%s,%s)"

    values = (idd,name,sal,date)

    mycur.execute(sql,values)

    mydb.commit()

def update():
    idd = t1.get()
    sal = t3.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="emp_data"
        )
    
    mycur=mydb.cursor()

    sql = "update emp_detail set salary=%s where emp_id=%s"

    values = (sal,idd)

    mycur.execute(sql,values)

    mydb.commit()

def delete():
    idd = t1.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="emp_data"
        )
    
    mycur=mydb.cursor()

    sql = "delete from emp_detail where emp_id=%s"

    values = (idd,)

    mycur.execute(sql,values)

    mydb.commit()

def email():
    port = 465  
    smtp_server = "smtp.gmail.com"
    sender_email = t1.get()  
    receiver_email = t2.get()
    subject = t3.get
    password = input("Type your password and press enter: ")
    message = t4.get()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email,subject,message)
        
def qr():
    img = qrcode.make("http://localhost/phpmyadmin/index.php?route=/sql&db=emp_data&table=emp_detail&pos=0")
    img.save("kevin_qr-img.jpg")
        

l1 = Label(top,text = "emp_id :")
l1.grid(row=0,column=0)

t1 = Entry(top)
t1.grid(row=0,column=1)

l2 = Label(top,text = "emp_name :")
l2.grid(row=1,column=0)

t2 = Entry(top)
t2.grid(row=1,column=1)

l3 = Label(top,text = "emp_salary :")
l3.grid(row=2,column=0)

t3 = Entry(top)
t3.grid(row=2,column=1)

l4 = Label(top,text = "join_date :")
l4.grid(row=3,column=0)

t4 = Entry(top)
t4.grid(row=3,column=1)

b1 = Button(top,text = "Insert",command = insert)
b1.grid(row=4,column=0)

b2 = Button(top,text = "Update",command = update)
b2.grid(row=4,column=1)

b3 = Button(top,text = "Delete",command = delete)
b3.grid(row=5,column=0)

b4 = Button(top,text = "Email",command = email)
b4.grid(row=5,column=1)

b5 = Button(top,text = "QR Code",command = qr)
b5.grid(row=6,column=0)






top.mainloop
