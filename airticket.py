import os                    #for remove or rename functions
import platform              #to retrieve info abt pltform on which is executed
import mysql.connector       #to connect mysql with python
import datetime              #to work with date and time in module

tamt=0
mydb = mysql.connector.connect(user='root', password='proxjersey',host='localhost',database='air',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()
def registercust():
    L=[]
    name=input("enter name:")
    L.append(name)
    addr=input("enter address:")
    L.append(addr)
    jr_date=input("enter date of journey:")
    L.append(jr_date)
    source=input("enter source:")
    L.append(source)
    destination=input("enter destination:")
    L.append(destination)
    cust=(L)
    sql="insert into pdata(name,addr,jrdate,source,destination)values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()
    print("customer data has been filled")
def classtypeview():
    print("Do you want to see class type available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from classtype"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
def ticketprice():
    global tamt
    print ("We have the following rooms for you:-")
    print ("1. type First class---->rs 6000 PN\-")
    print ("2. type Business class---->rs 4000 PN\-")
    print ("3. type Economy class---->rs 2000 PN\-")
    x=int(input("Enter Your Choice Please->"))
    n=int(input("No of passenger:"))
    if(x==1):
        print ("you have opted First class")
        s=6000*n
        print("your amount for first class is :",s,"\n")
    elif (x==2):
        print ("you have opted Business class")
        s=4000*n
        print("your amount for business class is :",s,"\n")
    elif (x==3):
        print ("you have opted Economy class")
        s=2000*n
        print("your amount for economy class is :",s,"\n")
    else:
        print ("please choose a class type")
        print ("your room rent is =",s,"\n")
    tamt+=s   
def menuview():
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from food"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
def orderitem():
    global s
    global tamt
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from food"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    print("do you want to purchase from above list:enter your choice:")
    d=int(input("enter your choice:"))
    if(d==1):
        print("you have ordered tea")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for tea is :",s,"\n")
    elif (d==2):
        print("you have ordered coffee")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for coffee is :",s,"\n")
    elif(d==3):
        print("you have ordered colddrink")
        a=int(input("enter quantity"))
        s=20*a
        print("your amount for colddrink is :",s,"\n")
    elif(d==4):
        print("you have ordered samosa")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount fopr samosa is :",s,"\n")
    elif(d==5):
        print("you have ordered sandwich")
        a=int(input("enter quantity"))
        s=50*a
        print("your amount for sandwich is :",s,"\n")
    elif(d==6):
        print("you have ordered dhokla")
        a=int(input("enter quantity"))
        s=30*a
        print("your amount for dhokla is :",s,"\n")
    elif(d==7):
        print("you have ordered kachori")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for kachori is :",s,"\n")
    
    elif(d==8):
        print("you have ordered noodles")
        a=int(input("enter quantity"))
        s=50*a
        print("your amount for noodles is :",s,"\n")
    elif(d==9):
        print("you have ordered pasta")
        a=int(input("enter quantity"))
        s=50*a
        print("your amount for pasta is :",s,"\n")
    else:
        print("please enter your choice from the menu")
    tamt+=s    
def lugagebill():
    global z
    global tamt
    print("Do yoy want to see rate for lugage : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from lugage"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    y=int(input("Enter Your weight of extra lugage->"))
    z=y*1000
    print("your laundarybill:",z,"\n")
    tamt+=z
    return z
def lb():
    print(z)
def res():
    print(s)
def ticketamount():
    '''
    a=input("enter classtype amount:")
    print("your amount:",a,"\n")
    b=input("enter lugage bill:")
    print("your amount:",b,"\n")
    c=input("enter food bill:")
    print("your amount:",c,"\n")
    '''
    print("your total bill:",tamt)#int(a)+int(b)+int(c),"\n")
def Menuset():
    while True:
        print("AIR TICKET RESERVATION")
        print("enter 1: To enter customer data")
        print("enter 2 : To view class")
        print("enter 3 : for ticketamount")
        print("enter 4 : for viewing food menu")
        print("enter 5 : for food bill")
        print("enter 6 : for lugage bill")
        print("enter 7 : for ticket amount")
        print("enter 8 : for exit")
        userinput=int(input("enter your choice"))
        if(userinput==1):
            registercust()
        elif(userinput==2):
            classtypeview()
        elif(userinput==3):
            ticketprice()
        elif(userinput==4):
            menuview()
        elif(userinput==5):
            orderitem()
        elif(userinput==6):
            lugagebill()
        elif(userinput==7):
            ticketamount()
        elif(userinput==8):
            quit()
        
        else:
            print("enter correct choice")
            
Menuset()

runagain()
def runagain():
    runagn=input("\n want to run again y/n:")
    while(runagn.lower()=='y'):
        if(platform.system()=="windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn=input("\n want to run again y/n:")
        runagain()

