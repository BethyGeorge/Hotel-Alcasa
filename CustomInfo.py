import pickle
def Cinfo():
   while True:
      print("\n\t\t\t--------Welcome To Customer Info Section--------")
      print()
      print("\t\t\t\t1.Booking")
      print("\t\t\t\t2.Displaying all records")
      print("\t\t\t\t3.Deletion of existing records")
      print("\t\t\t\t4.Searching of an existing record")
      print("\t\t\t\t5.Updation of existing record")
      ch1=int(input("Enter your choice"))
      if ch1==1:
         Booking()
      elif ch1==2:
         Display()
      elif ch1==3:
         Deletion()
      elif ch1==4:
         Searching()
      elif ch1==5:
         Update()
      else:
         print("Wrong choice selected")
      if input("Do you want to return to main menu").upper()!='Y':
         break

def checkdate():
        global cin,cout
        cin=input("Enter check-in date in the format(YYYY-MM-DD)")
        cout=input("Enter check-out date in the format(YYYY-MM-DD)")
        if cin>cout:
           print('Invalid entry')
           checkdate()
        else:
           return

def checkphno():
       global cphn
       cphn=input("Enter your 10 digit mobile number")
       if len(cphn)!=10:
        print('Invalid entry')
        checkphno()
       else:
        return
def checkroom():
             import os
             import csv
             global croomno,Croomp
             if os.path.exists("RoomInfo.csv"):
                croomno=input("Enter the room no.").upper()
                g=open("RoomInfo.csv","r")
                csvreader=csv.reader(g)
                for row in csvreader:
                   if len(row)>0:
                      if row[0]==croomno:
                         Croomp=float(row[2])
                         g.close()
                         break
                else:
                   print("No such room")
                   checkroom()
             else:
                  print("File doesn't exist")
                  
def Booking():
   f=open("managmentnew.dat","ab")
   while True:
     cid=int(input("Enter Customer id"))
     cname=input("Enter the name")
     checkphno()
     checkdate()
     cdate=int(input("Enter no of days of stay"))
     checkroom()
     ccom=int(input("Enter no of companions"))
     totrbill=Croomp*cdate
     print("\nTotal bill :",totrbill,"\n")
     cust={"Custid":cid,"Cname":cname,"Cphn":cphn,"Cin":cin,"Cout":cout,"Cdate":cdate,"Croomno":croomno,"Ccom":ccom,"Croomprice":totrbill}
     
     pickle.dump(cust,f)
     
     if input("Do u want to insert new customer data").upper()!='Y':
        break
   f.close()
     
     
def  Display():
   f=open("managmentnew.dat","rb")
   try:
      print()
      print('-'*172)
      print("| CUST ID |        CUST NAME       | CUST PHNUMBER | CUST CHECKIN | CUST CHECKOUT | NO. OF DAYS STAYED | CUST ROOMNO | CAMPANIONS | TOTAL BILL |")
      while True:               
               cust=pickle.load(f)
               print('-'*172)
               print('|    ',cust["Custid"],'    |      ',(cust["Cname"]).upper(),'  '*(10-len(cust["Cname"])),'      |     ',cust["Cphn"],'     |    ',cust["Cin"],'    |   ',cust["Cout"],'        |',' '*18,cust["Cdate"],' '*18,'|          ',cust["Croomno"],'         |            ',cust["Ccom"],'            |    ',cust["Croomprice"],'   |' )
      
   except EOFError:
      f.close()
   print('-'*172)
   print()
def  Deletion():
   f=open("managmentnew.dat","rb")
   custlist=[]
   try:
      while True:
         cust=pickle.load(f)
         custlist.append(cust)
   except EOFError:
      f.close()
   f=open("managmentnew.dat","wb")
   Ncid=int(input("Enter customer id to be deleted"))
   for i in custlist:
      if i["Custid"]==Ncid:
         continue
      pickle.dump(i,f)
   print("\n~~~~~~SUCCESSFULLY DELETED~~~~~~\n")
   f.close()
def Searching():
   f=open("managmentnew.dat","rb")
   Ncid=int(input("Enter customer id to be searched"))
   rec=False
   try:
      while True:
         cust=pickle.load(f)
         if  cust["Custid"]==Ncid:
             print()
             print("\t\t\t~~~~~~~CUSTOMER DETAILS~~~~~~~~")
             print("\t\t\t\tCustomer id=",cust["Custid"])
             print("\t\t\t\tCustomer name=",cust["Cname"])
             print("\t\t\t\tCustomer phn=",cust["Cphn"])
             print("\t\t\t\tCustomer check in date=",cust["Cin"])
             print("\t\t\t\tCustomer check out date=",cust["Cout"])
             print("\t\t\t\tDays of stay=",cust["Cdate"])
             print("\t\t\t\tRoom No.=",cust["Croomno"])
             print("\t\t\t\tNo of companions=",cust["Ccom"])
             print()
             rec=True
   except EOFError:
      f.close()
   if rec==False:
      print("\tNo such record")
      
def Update():
   f=open("managmentnew.dat","rb")
   custlist=[]
   try:
      while True:
         cust=pickle.load(f)
         custlist.append(cust)
   except EOFError:
      f.close()
      
   while True:
      cid=int(input("Enter the customer id to be updated"))
      for i in custlist:
          if i['Custid']==cid:
              break
      else:
          print("Customer ID not found")
          Update()
      print("\t\t\t\t1.NAME")
      print("\t\t\t\t2.PHONE NO.")
      print("\t\t\t\t3.CHECK- IN DATE")
      print("\t\t\t\t4. CHECK- OUT DATE")
      print("\t\t\t\t5.DOS")
      print("\t\t\t\t6.ROOM NO.")
      print("\t\t\t\t7.NO OF COMPANIONS")
      
      ch=int(input("Enter your choice"))
      if ch==1:
         newname=input("Enter new name")
         for i in custlist:
            if  i['Custid']==cid:
               i['Cname']=newname
               print("Successfully updated")
               break
         else:
            print("Customer ID not found")
            
      elif ch==2:
         checkphno()
         for i in custlist:
            if i['Custid']==cid:
               i['Cphn']=cphn
               print("Successfully updated")
               break
         else:
            print("Customer ID not found")
            
      elif ch==3:
         newindate=input("Enter new check-in date(YYYY-MM-DD)")
         for i in custlist:
            if  i['Custid']==cid:
               i['Cin']=newindate
               print("Successfully updated")
               break
         else:
            print("Customer ID not found")
            
      elif ch==4:
         newoutdate=input("Enter new check-out date(YYYY-MM-DD)")
         for i in custlist:
            if  i['Custid']==cid:
               i['Cout']=newoutdate
               print("Successfully updated")
               break
         else:
            print("Customer ID not found")
         
      elif ch==5:
         newdaty=int(input("Enter no of days of stay"))

         for i in custlist:
            if  i['Custid']==cid:
               i['Cdate']=newdaty
               import os
               import csv
               global Croomp
               if os.path.exists("RoomInfo.csv"):
                  g=open("RoomInfo.csv","r")
                  csvreader=csv.reader(g)
                  for row in csvreader:
                     if len(row)>0:
                      if row[0]==i['Croomno']:
                         Croomp=float(row[2])
                         g.close()
                         break
               i["Croomprice"]=i["Cdate"]*Croomp
               print("Successfully updated")
               break
         else:
            print("Customer ID not found")
            
      elif ch==6:
         checkroom()
         for i in custlist:
            if  i["Custid"]==cid:
               i["Croomno"]=croomno
               i["Croomprice"]=i["Cdate"]*Croomp
               print("Successfully updated")
               break
         else:
            print("Customer ID not found")
               
      elif ch==7:
         newcom=int(input("Enter the updated no of companions"))
         for i in custlist:
            if  i["Custid"]==cid:
               i["Ccom"]=newcom
               print("Successfully updated")
               break
         else:
            print("Customer ID not found")
            
      else:
         print("Wrong  option")
         
      f=open("managmentnew.dat","wb")
      for x in custlist:
         pickle.dump(x,f)
      f.close()
      if input("\nDo you wanna continue updating:(Y/N)?").upper()!='Y':
         break
         
