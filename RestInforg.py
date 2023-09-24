import os
import pickle

def insertmenu():
    ans='Y'
    f=open("menu.dat","ab")
    while ans=='Y':
        fcode=input("Enter food code:").upper()
        fname=input("Enter the food name:").upper()
        def checkftype():
            ftypel=["APPETIZER","MAIN COURSE","SNACKS","DESSERT","BEVERAGE"]
            global ftype
            print("Enter the food type:")
            print("\t\t\t1. Appetizer")
            print("\t\t\t2. Main course")
            print("\t\t\t3. Snacks")
            print("\t\t\t4. Dessert")
            print("\t\t\t5. Beverages")
            ch=int(input("choice:"))
            if ch not in [1,2,3,4,5]:
                print('Invalid entry')
                checkftype()
            else:
                ftype=ftypel[ch-1]
                return
        checkftype()
        fprice=int(input("Enter the food price:"))
        foodrec={"Food Code":fcode,"Food Name":fname,"Food type":ftype,"Price":fprice}
        pickle.dump(foodrec,f)
        ans=input("\nDo you want to add more item to the menu?:").upper()
    f.close()

def displaymenu():
    f=open("menu.dat","rb")
    flst=[]
    try:
        while True:
            foodrec=pickle.load(f)
            flst.append(foodrec)
    except EOFError:
        f.close()
    ftypel=["APPETIZER","MAIN COURSE","SNACKS","DESSERT","BEVERAGE"]
    print("~"*90)
    print("\t\t\t\tHOTEL ALCASA")
    print("\t\t\t\t      MENU          ")
    for i in ftypel:
        print("\t\t\t",'*'*43)
        print("\t\t\t",i)
        print("\t\t\t",'*'*43)
        print("\t\t\t","FCODE   ","FOOD NAME",'  '*8,"PRICE")
        print("\t\t\t",'-'*43)
        for j in flst:
            if j["Food type"]==i:
                print("\t\t\t",j["Food Code"],' '*6,j["Food Name"],'  '*(19-len(j["Food Name"])),j["Price"])
                print("\t\t\t","-"*43)
        #print()
def updatemenu():
    f=open("menu.dat","rb")
    flst=[]
    try:
        while True:
            foodrec=pickle.load(f)
            flst.append(foodrec)
    except EOFError:
        f.close()
    while True:
        for i in flst:
            print(i,"\n")
        updfc=input("Enter the food code of the food which is to be updated:").upper()
        print("\t\t\t\tChoose what to be updated?")
        print("\n\t\t\t\t1)Food name")
        print("\t\t\t\t2)Food type")
        print("\t\t\t\t3)Price")
        choice=int(input("enter the choice"))
        if choice==1:
            newfname=input("Enter new food name:").upper()
            for i in range(len(flst)):
                if flst[i]["Food Code"]==updfc:
                    flst[i]["Food Name"]=newfname
                    print("Successfully updated")
                    break
            else:
                print("Food code not found")
            f=open("menu.dat","wb")
            for x in flst:
                pickle.dump(x,f)
            f.close()
        elif choice==2:
            newftype=input("Enter new food type").upper()
            for i in range(len(flst)):
                if flst[i]["Food Code"]==updfc:
                    flst[i]["Food type"]=newftype
                    print("Successfully updated")
                    break
            else:
                print("Food code not found")
            f=open("menu.dat","wb")
            for x in flst:
                pickle.dump(x,f)
            f.close()
        elif choice==3:
            newfprice=int(input("Enter new food price:"))
            for i in range(len(flst)):
                if flst[i]["Food Code"]==updfc:
                    flst[i]["Price"]=newfprice
                    print("Successfully updated")
                    break
            else:
                print("Food code not found")
            f=open("menu.dat","wb")
            for x in flst:
                pickle.dump(x,f)
            f.close()
        if input("Do you wanna continue updating(Y/N)").upper()!="Y":
            break

def fsearch():
    while True:
        print("\t\t\t\tchoose the attribute to search by:")
        print("\n\t\t\t\t1)Food code")
        print("\t\t\t\t2)Food name")
        print("\t\t\t\t3)Food type")
        choice=int(input("enter the choice"))
        if choice==1:
            f=open("menu.dat","rb")
            srcfc=input("Enter the foodcode to be searched\n").upper()
            cnt=False
            try:
                while True:
                    foodrec=pickle.load(f)
                    if foodrec["Food Code"]==srcfc:
                        print("Food code=",foodrec["Food Code"])
                        print("Food name=",foodrec["Food Name"])
                        print("Food type=",foodrec["Food type"])
                        print("Price=",foodrec["Price"])
                        rec=True
            except EOFError:
                f.close()
            if rec==False:
                print("No records found")

        elif choice==2:
            f=open("menu.dat","rb")
            srcfn=input("Enter the foodname to be searched\n").upper()
            cnt=False
            try:
                while True:
                    foodrec=pickle.load(f)
                    if foodrec["Food Name"]==srcfn:
                        print("\t\t\t\tFood code=",foodrec["Food Code"])
                        print("\t\t\t\tFood name=",foodrec["Food Name"])
                        print("\t\t\t\tFood type=",foodrec["Food type"])
                        print("\t\t\t\tPrice=",foodrec["Price"])
                        rec=True
            except EOFError:
                f.close()
            if rec==False:
                print("No records found")
        elif choice==3:
            f=open("menu.dat","rb")
            def checkftype():
                global srcft
                print("\t\t\t\t1. Appetizer")
                print("\t\t\t\t2. Main course")
                print("\t\t\t\t3. Snacks")
                print("\t\t\t\t4. Dessert")
                print("\t\t\t\t5. Beverages")
                ftypel=["APPETIZER","MAIN COURSE","SNACKS","DESSERT","BEVERAGE"]
                ftype=int(input("Enter the food type:"))
                if ftype not in [1,2,3,4,5]:
                    print('Invalid entry')
                    checkftype()
                else:
                    srcft=ftypel[ftype-1]
                    #global srcft
                    return
            checkftype()
            cnt=False
            try:
                while True:
                    foodrec=pickle.load(f)
                    if foodrec["Food type"]==srcft:
                        print("\t\t\t\tFood code=",foodrec["Food Code"])
                        print("\t\t\t\tFood name=",foodrec["Food Name"])
                        print("\t\t\t\tFood type=",foodrec["Food type"])
                        print("\t\t\t\tPrice=",foodrec["Price"])
                        rec=True
                        print()
            except EOFError:
                f.close()
            if rec==False:
                print("No records found")
        else:
            print("--------INVALID CHOICE---------")
        if input("\nDo you want to continue searching:(Y/N)").upper()!="Y":
            break

def deletefrec():
    while True:
        f=open("menu.dat","rb")
        flst=[]
        try:
            while True:
                foodrec=pickle.load(f)
                flst.append(foodrec)
        except EOFError:
            f.close()
        f=open("menu.dat","wb")
        delfc=input("Enter the foodcode to be deleted").upper()
        for x in flst:
            if x["Food Code"]==delfc:
                print(x["Food Name"],'deleted')
                continue
            pickle.dump(x,f)
        f.close()
        if input("Do you want to delete more(Y/N)").upper()!='Y':
            break
        
def placingorder():
    m=open("custfoodorder.dat","ab")
    while True:
        custno=int(input("Enter customer no."))
        totbill=0
        ans='y'
        foodordrec={}
        foodordrec['cust no.']=custno
        printbill=["|\n|\t\t\tHOTEL ALCASA","|\n|~~~~Cust No.:","|          DESCRIPTION           |           QNTY                |                 PRICE                    "]
        
        while ans=='y':
            fcode=input("Enter the fcode of the food which is to be ordered:").upper()
            quant=int(input("Enter the quantity required:"))
            f=open("menu.dat","rb")
            cnt=False
            
            try:
                while True:
                    foodrec=pickle.load(f)
                    if foodrec["Food Code"]==fcode:
                        Price=foodrec["Price"]
                        cnt=True
                        totprice=quant*Price
                        totbill+=totprice
                        foodordrec[foodrec["Food Name"]]=quant
                        x=[foodrec["Food Name"],quant,Price]
                        printbill.append(x)
            except EOFError:
                f.close()
            if cnt==False:
                print("Invalid fcode")
            ans=input("Do you wish to order more?(Y/N)").lower()
        foodordrec["Total bill"]=totbill
        printbill.append(totbill)
        printbill.append("|\t\tTHANK YOU FOR VISITING\n\t\tHAVE A NICE DAY : )\n")
        v=len(printbill)
        for c in range(v):
            if c in [0,2] or c==v-1:
                print('I',"-"*80)
                
                print(printbill[c])                
            elif c==1:
                print(printbill[c],custno)
            elif c==v-2:
                print('|',"-"*80)
                print("|\t\t\t\t\tTOTAL BILL:",float(printbill[c]))
            else:
                print('|',"-"*80)
                print('|        ',printbill[c][0],'  '*(25-len(printbill[c][0])),printbill[c][1],'  '*18,printbill[c][2],'  '*12)
        pickle.dump(foodordrec,m)
        if input("Do you want to place orders of more customers?(Y/N)").upper()!='Y':
            break
    m.close()
    
def dispforderrec():
    m=open("custfoodorder.dat","rb")
    try:
        while True:
            foodordrec=pickle.load(m)
            print("\n")
            for key in foodordrec:
                if key=='cust no.':
                    print(key,'  :', foodordrec[key])
                else:
                    print(key,'  :', foodordrec[key],end='   ')
    except EOFError:
        m.close()
    print()

def searfdordrec():
    while True:
         m=open("custfoodorder.dat","rb")
         custno=int(input("Enter the customer no."))
         rec=False
         try:
             while True:
                 foodordrec=pickle.load(m)
                 if foodordrec["cust no."]==custno:
                     print(foodordrec)
                     rec=True
                
         except EOFError:
            m.close()
         if rec==False:
            print("No records of food ordered by customer no:",custno ,"was found")
         if input("\nDo you want to continue searching?(Y/N)").upper()!='Y':
            break
           
def delcustfrec():
    while True:
        f=open("custfoodorder.dat","rb")
        flst=[]
        try:
            while True:
                foodrec=pickle.load(f)
                flst.append(foodrec)
        except EOFError:
            f.close()
        f=open("custfoodorder.dat","wb")
        delfc=int(input("Enter the code of the customer whose record is to be deleted"))
        for x in flst:
            if x["cust no."]==delfc:
                print(x)
                continue
            pickle.dump(x,f)
        f.close()        
        print("******SUCCESSFULLY DELETED******")    
        if input("Do you want to continue deleting?(Y/N)").upper()!='Y':
            break
        
def Finfo():
    while True:
        print("\t\t\t------Welcome To Restaurant Info Section------")
        print("\n\t\t\t\t1)Insert new item")
        print("\t\t\t\t2)Display menu")
        print("\t\t\t\t3)Update menu")
        print("\t\t\t\t4)Search for a food")
        print("\t\t\t\t5)Delete an item")
        print("\t\t\t\t6)Placing order")
        print("\t\t\t\t7)display food order records")
        print("\t\t\t\t8)search for a customer's record of food ordered")
        print("\t\t\t\t9)Delete a customer's food order record ")
        print("\t\t\t\t Choose 0 to exit")
        choice=int(input("Enter the choice"))
        print()
        if choice==0:
            break
        elif choice==1:
            insertmenu()
        elif choice==2:
            displaymenu()
        elif choice==3:
            updatemenu()
        elif choice==4:
            fsearch()
        elif choice==5:
            deletefrec()
        elif choice==6:
            placingorder()
        elif choice==7:
            dispforderrec()
        elif choice==8:
            searfdordrec()
        elif choice==9:
            delcustfrec()
        else:
            print("INVALID CHOICE")
        if input("\nDo you wanna return to the main menu(Y/N)").upper()!="Y":
             break
            
