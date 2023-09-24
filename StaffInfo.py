import mysql.connector as mys
mydb=mys.connect(host='localhost',user='root',passwd='mys#q#l#1234')
cursor=mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS STAFFDETAILS")
cursor.execute("USE STAFFDETAILS")
cursor.execute("CREATE TABLE IF NOT EXISTS SDET(STAFFNO INTEGER PRIMARY KEY,STAFFNAME VARCHAR(30),STAFFAGE INT(3),STAFFJOB VARCHAR(20),STAFFSALARY INTEGER,STAFFPHNUMBER INT(10),STAFFADDRESS VARCHAR(20),STAFFGENDER CHAR(1),STAFFHIREDATE DATE)")
mydb.close()
cursor.close()
#checking whether phone no. has 10 digits
def checkphno():
  global staffphnumber
  staffphnumber=input("Enter 10 digit phone no.")
  if len(staffphnumber)!=10:
    print('Invalid entry')
    checkphno()
  else:
    return

def instaffdet():
  import mysql.connector as mys
  mydb=mys.connect(host='localhost',user='root',passwd='mys#q#l#1234',database="staffdetails")
  cursor=mydb.cursor()
  print("\t.......Data Entry .......")
  while True:
    staffno=int(input("Enter the staff no"))
    staffname=input("Enter the staff name").upper()
    staffjob=input("Enter the staff job").upper()
    bs=float(input("Enter the basic salary"))
    hra=0.25*bs
    da=0.1*bs
    ta=0.05*bs
    gs=bs+hra+ta+da
    tax=0.12*gs
    staffsalary=gs-tax
    staffage=int(input("Enter the staff age"))
    checkphno()
    staffaddress=input("Enter the staff address").upper()
    staffgender=input("Enter the staff gender").upper()
    staffhiredate=input("Enter the staff hiredate in the format(YYYY-MM-DD)")
    q1="insert into SDET values({},'{}',{},'{}',{},'{}','{}','{}','{}')".format(staffno,staffname,staffage,staffjob,staffsalary,staffphnumber,staffaddress,staffgender,staffhiredate)
    cursor.execute(q1)
    mydb.commit()
    if input("Do you wanna continue inserting(Y/N)").upper()!="Y":
        break
  mydb.close()
  cursor.close()
  
def display():
    import mysql.connector as mys
    mydb=mys.connect(host='localhost',user='root',passwd='mys#q#l#1234',database="staffdetails")
    cursor=mydb.cursor()
    cursor.execute("select * from sdet")
    data=cursor.fetchall()
    print('-'*175)
    print("|STAFF NO. |         STAFFNAME       |  STAFFAGE  |        STAFFJOB        |  STAFFSALARY  |  STAFF PHNUMBER  |   STAFF ADDRESS   |  STAFF GENDER  |  STAFF HIREDATE |")
    for row in data:        
        print("-"*175)
        print("|     ",row[0],"      |  ",row[1],'  '*(15-len(row[1])),"  |        ",row[2],"        |  ",row[3],'   '*(10-len(row[3])),"  |     ",row[4],"     |       ",row[5],'  '*(10-len(row[5])),"       |  ",row[6],'   '*(11-len(row[6])),"  |            ",row[7],"             |      ",row[8],"      |")
    print("-"*175)
    print("\n")        
    mydb.close()
    cursor.close()
    
def update():
    import mysql.connector as mys
    mydb=mys.connect(host='localhost',user='root',passwd='mys#q#l#1234',database="staffdetails")
    cursor=mydb.cursor()
    while True:
        print("\t\t\t~~~~~~STAFF UPDATION~~~~~~") 
        print("\t\t\t----Choose what to be updated?----")
        print("\t\t\t\t1)Name")
        print("\t\t\t\t2)Age")
        print("\t\t\t\t3)Salary")
        print("\t\t\t\t4)Phone No.")
        print("\t\t\t\t5)Address")
        choice=int(input("enter the choice"))
        if choice==1:
            Nstano=int(input("Enter the staffno to be updated"))
            q1="select * from sdet where staffno={}".format(Nstano)
            cursor.execute(q1)
            data=cursor.fetchone()
            if data!=None:
                name=input("Enter the new staff name").upper()
                q2="update sdet set staffname='{}' where staffno={}".format(name,Nstano)
                cursor.execute(q2)
                mydb.commit()
                print("\n\t***RECORD UPDATED****")
            else:
                print("NO SUCH STAFF FOUND")
            
        elif choice==2:
            Nstano=int(input("Enter the staffno to be updated"))
            q1="select * from sdet where staffno={}".format(Nstano)
            cursor.execute(q1)
            data=cursor.fetchone()
            if data!=None:
                nage=int(input("enter the new age"))
                q2="update sdet set staffage={} where staffno={}".format(nage,Nstano)
                cursor.execute(q2)
                mydb.commit()
                print("\n\t****RECORD UPDATED****")
            else:
                print("NO SUCH STAFF FOUND")
            
        elif choice==3:
            Nstano=int(input("Enter the staffno to be updated"))
            q1="select * from sdet where staffno={}".format(Nstano)
            cursor.execute(q1)
            data=cursor.fetchone()
            if data!=None:
                bs=float(input("Enter the new salary"))
                hra=0.25*bs
                da=0.1*bs
                ta=0.05*bs
                gs=bs+hra+ta+da
                tax=0.12*gs
                newsal=gs-tax
                q2="update sdet set staffsalary={} where staffno={}".format(newsal,Nstano)
                cursor.execute(q2)
                mydb.commit()
                print("\n\t****RECORD UPDATED****")
            else:
                print("NO SUCH STAFF FOUND")
            
        elif choice==4:
            Nstano=int(input("Enter the staffno to be updated"))
            q1="select * from sdet where staffno={}".format(Nstano)
            cursor.execute(q1)
            data=cursor.fetchone()
            if data!=None:
                checkphno()
                newphno=staffphnumber
                q2="update sdet set staffphnumber='{}' where staffno={}".format(newphno,Nstano)
                cursor.execute(q2)
                mydb.commit()
                print("\n\t****RECORD UPDATED****")
            else:
                print("NO SUCH STAFF FOUND")
            
        elif choice==5:
            Nstano=int(input("Enter the staffno to be updated"))
            q1="select * from sdet where staffno={}".format(Nstano)
            cursor.execute(q1)
            data=cursor.fetchone()
            if data!=None:
                newadd=input("Enter the new address").upper()
                q2="update sdet set staffaddress='{}' where staffno={}".format(newadd,Nstano)
                cursor.execute(q2)
                mydb.commit()
                print("\n\t****RECORD UPDATED****")
            else:
                print("NO SUCH STAFF FOUND")
        if input("\nDO YOU WANNA CONTINUE UPDATING").upper()!="Y":
          break
    mydb.close()
    cursor.close()
    
def search():
    import mysql.connector as mys
    mydb=mys.connect(host='localhost',user='root',passwd='mys#q#l#1234',database="staffdetails")
    cursor=mydb.cursor()
    while True:
        print("\t\t\t\tchoose the attribute to search by:")
        print(" \t\t\t\t1)staff no","\n","\t\t\t\t2)staff name","\n","\t\t\t\t3)staff job")
        choice=int(input("enter the choice"))
        print("\n")
        if choice==1:
            Nstano=int(input("Enter the staffno to be searched"))
            rec=False
            cursor.execute("select * from sdet")
            data=cursor.fetchall()
            for row in data:
                  if row[0]==Nstano:
                      print("\n\t\t\t~~~~~~~~STAFF DETAILS~~~~~~~~")
                      print("\t\t\t\tstaff no.=",row[0])
                      print("\t\t\t\tstaff name=",row[1])
                      print("\t\t\t\tstaff age=",row[2])
                      print("\t\t\t\tstaff salary=",row[3])
                      print("\t\t\t\tstaff job=",row[4])
                      print("\t\t\t\tstaff phnumber=",row[5])
                      print("\t\t\t\tstaff address=",row[6])
                      print("\t\t\t\tstaff gender=",row[7])
                      print("\t\t\t\tstaff hiredate=",row[8])
                      #print("\n")
                      rec=True
            if rec==False:
                     print("***RECORD NOT FOUND***")
                
        elif choice==2:
            Nstaname=input("Enter the staffname to be searched").upper()
            rec=False
            q="select * from sdet"
            cursor.execute(q)
            data=cursor.fetchall()
            for row in data:
                  if row[1]==Nstaname:
                      print("\n\t\t\t~~~~~~STAFF DETAILS~~~~~~")
                      print("\t\t\t\tstaff no.=",row[0])
                      print("\t\t\t\tstaff name=",row[1])
                      print("\t\t\t\tstaff age=",row[2])
                      print("\t\t\t\tstaff job=",row[3])
                      print("\t\t\t\tstaff salary=",row[4])
                      print("\t\t\t\tstaff phnumber=",row[5])
                      print("\t\t\t\tstaff address=",row[6])
                      print("\t\t\t\tstaff gender=",row[7])
                      print("\t\t\t\tstaff hiredate=",row[8])
                      print("\n")
                      rec=True
            if rec==False:
                 print("***RECORD NOT FOUND***")
        elif choice==3:
            stajob=input("Enter the staffjob to be searched").upper()
            rec=False
            cursor.execute("select * from sdet")
            data=cursor.fetchall()
            for row in data:
                  if row[3]==stajob:
                      print("\n\t\t\t~~~~~~STAFF DETAILS~~~~~~")
                      print("\t\t\t\tstaff no.=",row[0])
                      print("\t\t\t\tstaff name=",row[1])
                      print("\t\t\t\tstaff age=",row[2])
                      print("\t\t\t\tstaff job=",row[3])
                      print("\t\t\t\tstaff salary=",row[4])
                      print("\t\t\t\tstaff phnumber=",row[5])
                      print("\t\t\t\tstaff address=",row[6])
                      print("\t\t\t\tstaff gender=",row[7])
                      print("\t\t\t\tstaff hiredate=",row[8])
                      print("\n")
                      rec=True
            if rec==False:
               print("***RECORD NOT FOUND***")
        if input("Do you want to coninue searching?").upper()!="Y":
                  break
    mydb.close()
    cursor.close()      
    
def deleterec():
    import mysql.connector as mys
    mydb=mys.connect(host='localhost',user='root',passwd='mys#q#l#1234',database="staffdetails")
    cursor=mydb.cursor()
    Nstano=int(input("Enter the staffno to be deleted"))
    cursor.execute("delete from sdet where staffno={}".format(Nstano))
    mydb.commit()
    print("\t~~~~SUCCESSFULLY DELETED~~~~")

def Sinfo():
  while True:
            print("\n\t\t\t------Welcome To Staff Info Section------")
            print(" \t\t\t\t1)Insert record","\n","\t\t\t\t2)Display the record","\n","\t\t\t\t3)Update record","\n","\t\t\t\t4)Search for a record","\n","\t\t\t\t5)Delete a record")
            print(" \t\t\t\tChoose 0 to exit")
            choice=int(input("Enter the choice"))
            print("\n")
            if choice==0:
                break
            elif choice==1:
                instaffdet()
            elif choice==2:
                display()
            elif choice==3:
                update()
            elif choice==4:
                search()
            elif choice==5:
                deleterec()
            if input("Do you wanna return to the main menu(Y/N)").upper()!="Y":
                break

    
    
            
        
                
                
            
                
            
            
            
         
                
            
            
            
    
    
