import sys
import os
import pickle
import CustomInfo
import RoomInfoORG
import StaffInfo
import RestInforg
def Home():
   while True:
      print("\n\t\t\t-------Welcome to Hotel ALCASA-------")
      print("\t\t\t\t1.Customer Info")
      print("\t\t\t\t2.Room Info")
      print("\t\t\t\t3.Staff Info ")
      print("\t\t\t\t4.Restaurant Info")
      print("\t\t\t\t0.EXIT")
      ch=int(input('Enter your choice'))
      if ch==1:
         print()
         sec=input("Enter the security code")
         if sec=="916":
            CustomInfo.Cinfo()
         else:
            print("Unauthorized user!!!\n")      
      elif ch==2:
         RoomInfoORG.Rinfo()
      elif ch==3:
         sec=input("\nEnter the security code")
         if sec=="916":
            StaffInfo.Sinfo()
         else:
            print("Unauthorized user!!!\n")
      elif ch==4:
         RestInforg.Finfo()
      elif ch==0:
         sys.exit()
      else:
         print("Wrong choice selected")
      if input("Do you want to return to Home page").upper()!='Y':
          sys.exit()

def login():
   print("<>"*40)
   print("\n\t\t\t\t\t WELCOME  TO  HOTEL\n\t\t\t\t\t               ALCASA \n\n\t\t\t\t\t ~~~LOGIN PAGE~~~")
   print()
   print("<>"*40)
   print()
   logid=input("Enter the login id")
   pswd=input("Enter the password")
   print()
   if logid=="staff@alcasa" and pswd=='@|C@$@':
      Home()
   else:
      print("Invalid id or password")
      print()
   if input("Do you want to return to login page(Y/N)?").upper()=='Y':
      login()
   else:
      sys.exit()

login()
      

            
   
   
      
         
