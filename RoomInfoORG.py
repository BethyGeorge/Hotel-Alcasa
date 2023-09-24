import os
import csv
    
def insertRec():
 f=open("RoomInfo.csv","a",newline='')
 mywriter=csv.writer(f)
 while True:
    roomno=input("Enter room no").upper()
    roomname=input("Enter room type").upper()
    rprice=float(input("Enter room price"))
    mywriter.writerow([roomno,roomname,rprice])
    print("\n~~~DATA saved~~~")
    if input("Do you want to add more rooms?").upper()!='Y':
        break


def readRec():
 with open("RoomInfo.csv") as f:
    myreader=csv.reader(f)
    print("-"*63)
    print('|  ROOM NO. |              ROOM TYPE             |  ROOM PRICE  |')
    for row in myreader:
        if len(row)>0:
            print("-"*63)
            print("|      ",row[0],"       |     ",row[1],'  '*(20-len(row[1])),"|       ",row[2],"      |")
    print("-"*63)

    
def Search():
 while True:
     f=open("RoomInfo.csv","r")
     csvreader=csv.reader(f)
     r=input("Enter room no").upper()
     for row in csvreader:
        if len(row)>0:
            if row[0]==r:
                 print("\t\t\t\tROOM NO=",row[0])
                 print("\t\t\t\tROOM TYPE=",row[1])
                 print("\t\t\t\tROOM PRICE=",row[2])
                 break
     else:
        print("No such room")
     if input("\nDo you want to continue searching?").upper()!='Y':
        f.close()
        break

    
def update():

 while True:
    print("\t\t\t\tChoose what to be updated")
    print("\t\t\t\t1.roomprice\n\t\t\t\t2.roomtype")
    choice=int(input("Enter the choice"))
    print("\n")
    if choice==1:
        f=open("RoomInfo.csv","r",newline='')
        fout=open("Room2.csv","w",newline='')
        csvreader=csv.reader(f)
        csvwriter=csv.writer(fout)
        rt=input("Enter room no. for which price has to be changed ").upper()
        found=0
        for row in csvreader:
            if row[0]==rt:
                for j in row:
                    print ("\t\t\t\t",j)
                roomprice=float(input("Enter new price"))
                row[2]=roomprice
                print("\n~~~~~Successfully updated~~~~~")
                found=1
            csvwriter.writerow(row)
                
        if found==0:
            print("Wrong room no.")
        fout.close()
        f.close()
        os.remove('RoomInfo.csv')
        os.rename('Room2.csv','RoomInfo.csv')

    elif choice==2:
        f=open("RoomInfo.csv","r",newline='')
        fout=open("Room2.csv","w",newline='')
        csvreader=csv.reader(f)
        csvwriter=csv.writer(fout)

        rt=input("Enter room no. for which roomtype has to be changed ").upper()
        found=0
        for row in csvreader:
            if row[0]==rt:
                for j in row:
                    print("\t\t\t\t",j)
                roomtype=input("Enter new room type").upper()
                row[1]=roomtype
                print("Successfully updated")
                found=1
            csvwriter.writerow(row)
        if found==0:
            print("Wrong room no.")
        fout.close()
        f.close()
        os.remove('RoomInfo.csv')
        os.rename('Room2.csv','RoomInfo.csv')
        
    if input("Do you want to continue updating(Y/N)").upper()!='Y':
        break
  
def deleteRec():
    while True:
         f=open("RoomInfo.csv","r",newline='')
         fout=open("TMP.csv","w",newline='')
         csvreader=csv.reader(f)
         csvwriter=csv.writer(fout)
         r=input("Enter  room no").upper()
         for row in csvreader:
             if r!=row[0]:
                 csvwriter.writerow(row)
         fout.close()
         f.close()
         os.remove("RoomInfo.csv")
         os.rename("TMP.csv","RoomInfo.csv")
         print("~~~~~~~~SUCCESSFULLY DELETED~~~~~~~~")
         if input("\nDo you want to delete more records").upper()!='Y':
             break 

def Rinfo():
 while True:
    print("\n\t\t\t------Welcome To Room Info Section------")

    print("\t\t\t\t1.Add room records")
    print("\t\t\t\t2.Display room records")
    print("\t\t\t\t3.Search records of a room")
    print("\t\t\t\t4.Update room records")
    print("\t\t\t\t5.Delete a room record")
    print("\t\t\t\tEnter your choice 0 to exit")
    choice=int(input("Enter the choice:"))
    if choice==0:
        break
    elif choice==1:
        insertRec()
    elif choice==2:
        readRec()
    elif choice==3:
        Search()
    elif choice==4:
        update()
    elif choice==5:
        deleteRec()
    else:
        print("Incorrect choice")

    if input("Do you want to return to main menu(Y/N)").upper()!='Y':
        
        break
    

