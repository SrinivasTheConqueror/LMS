#Library Mangement
#importing modules
from csv import writer
from pyfiglet import print_figlet
import mysql.connector as m


'''creating a connection'''

con=m.connect(host="localhost",user="root",passwd='123456',database='qwerty')
cur=con.cursor()
#creating tables
#table1
s1="create table book(bid int primary key,bname varchar(20),author varchar(20), price int, qty int,category varchar(20))"
cur.execute(s1)
#table2
#s2="create table borrower(bid int primary key,brname varchar(20),contact bigint,borrowdate date,returndate date,remarks varchar(10))"
cur.execute(s2)
#table3
s3="create table dealer(bid int primary key,dname varchar(20),contact bigint, price int, qty int,category varchar(20))"
cur.execute(s3)


#addfuctions

def addbooks():
        n=int(input("enter no of records:"))
        for i in range(n):
                Bid=int(input("enter book id:"))
                Bname=input("enter name of the book:")
                Author=input("enter name of the author:")
                Price=int(input("enter the price of the book:"))
                qty=int(input("enter the no of books:"))
                ctg=input("enter the category of the book:")
                s="insert into book(bid,bname,author,price,qty,category) values({},'{}','{}',{},{},'{}')".format(Bid,Bname,Author,Price,qty,ctg)
                cur.execute(s)
        con.commit()
def addborrower():
        n=int(input("Enter number of records:"))
        for i in range(n):
                Bid=int(input("Enter book id:"))
                Brname=input("Enter Borrower name:")
                Contact=int(input("Enter Contact:"))
                Borrowdate=input("Enter Borrowed Date(yyyy-mm-dd):")
                Returndate=input("Enter Return Date(yyyy-mm-dd):")
                Remarks=input("Enter Remarks:")
                s="insert into borrower(bid,brname,contact,borrowdate,returndate,remarks) values({},'{}',{},'{}','{}','{}')".format(Bid,Brname,Contact,Borrowdate,Returndate,Remarks)
                cur.execute(s)
        con.commit()
def adddealer():
        n=int(input("enter no of records:"))
        for i in range(n):
                Bid=int(input("enter book id:"))
                Dname=input("enter name of the dealer:")
                cont=int(input("enter the contact no of the dealer:"))
                Price=int(input("enter the price of the book:"))
                qty=int(input("enter the no of books:"))
                ctg=input("enter the category of the book:")
                s="insert into dealer(bid,dname,contact,price,qty,category)values({},'{}',{},{},{},'{}')".format(Bid,Dname,cont,Price,qty,ctg)
                cur.execute(s)
        con.commit()

#view book functions
def viewbooks():
        cur.execute("select * from book")
        vb=cur.fetchall()
        for i in vb:
                print(i)
        print("\t")
        csv=input("do you want save the details extracted into a csv file y/n")
        if csv=='y':
                with open("E:\\cs.csv",'w') as f:
                        w=writer(f)
                        for j in vb:
                                w.writerow(j)
     
def viewnobooks():
        cur.execute("select sum(qty) from book")
        vb=cur.fetchall()
        for i in vb:
                print("No. of books that are availiable in library:",i[0])
        
def viewnobookscat():
        cur.execute("select category,sum(qty) from book group by category")
        vb=cur.fetchall()
        print("catergory  qty")
        for i in vb:
                print(i[0] , i[-1
                               ])
        

#view borrower functions

def viewborrower():
        cur.execute("select * from borrower")
        vbr=cur.fetchall()
        for i in vbr:
                print(i)
        print("\t")
        csv=input("do you want save the details extracted into a csv file y/n")
        if csv=='y':
                with open("E:\\cs.csv",'w') as f:
                        w=writer(f)
                        for j in vbr:
                                w.writerow(j)

def viewborrowerdate():
        date1=input("Enter start date")
        date2=input("Enter end date")
        cur.execute("select * from borrower where returndate between '{}' and '{}' ".format(date1,date2))
        vbr=cur.fetchall()
        for i in vbr:
                print(i)

def viewlateborrower():
        cur.execute("select * from borrower where remarks='late' ")
        vbr=cur.fetchall()
        for i in vbr:
                print(i)

#view dealer functions

def viewdealer():
    cur.execute("select * from dealer")
    vd=cur.fetchall()
    for i in vd:
        print(i)
    csv=input("do you want save the details extracted into a csv file y/n")
    if csv=='y':
        with open("E:\\cs.csv",'w') as f:
            w=writer(f)
            for j in vd:
                w.writerow(j)
    
        

def viewdealerbooks():
    cur.execute("select b.bid,b.qty,b.price,d.dname,d.contact from book b ,dealer d where b.bid=d.bid")
    vd=cur.fetchall()
    for i in vd:
            print(i)
                        

def viewdealercat():
        cur.execute("select category,sum(qty) from dealer group by category ")
        vd=cur.fetchall()
        print("Total no.of books supplied by dealer in each category")
        for i in vd:
                print(i[0],i[-1])
        

#update functions

def updatebooks():
        print("\t")
        ub=input('Enter  column name do you want to update\n Bid\n Bname\n Author\n Price\n Qty\n Category :')
        if ub in ["Bid","Price","Qty"]:
                new1=int(input("Please enter the value"))
                bid=int(input("Please enter the Bid of the book"))
                q="update book set {}={} where bid={}".format(ub,new1,bid)
        else:
                new1=input("Please enter the value")
                bid=int(input("Please enter the Bid of the book"))
                q="update book set {}='{}' where bid={}".format(ub,new1,bid)
        cur.execute(q)
        con.commit()
        
def updateborrower():
        print("\t")
        ubr=input('Enter column  do you want to update\n Bid\n Brname\n Contact\n Borrowdate\n Returndate :')
        bid=int(input("Please enter the Bid of the book :"))
        if ubr in ['Bid','Contact']:
                new2=int(input("Please enter the value :"))
                t="update borrower set {}={} where bid={}".format(ubr,new2,bid)
                
        else:
                new2=input("Please enter the value")
                t="update borrower set {}='{}' where bid={}".format(ubr,new2,bid)
        cur.execute(t)
        con.commit()
        
 
def updatedealer():
        print("\t")
        ud=input('Enter column  do you want to update\n Bid\n Dname\n Contact\n Price\n Qty\n Category :')
        bid=int(input("Please enter the Bid of the Book:"))
        if ud in ["Dname","Category"]:
                new3=input("Please enter the new value")
                z="update dealer set {}='{}' where bid={}".format(ud,new3,bid)
                
        else:
                new3=int(input("Please enter the new value"))
                z="update dealer set {}={} where bid={}".format(ud,new3,bid)
        cur.execute(z)
        con.commit()
        


#main function    
def main():
        print_figlet("Library\nManagement",font="ansi_regular",width=100)   
        print("\t")
        print("1.Add details of books")
        print("2.View details of books")
        print("3.Update details of books")
        print("4.Exit")
        choice=int(input("Enter the choice :"))
        if choice==1:
                print("\t")
                addchoice=int(input("Which table\n 1.Books\n 2.Borrower\n 3.Dealer\n 4.Main Menu :"))
                if addchoice==1:
                        addbooks()
                elif addchoice==2:
                        addborrower()
                elif addchoice==3:
                        adddealer()
                elif addchoice==4:
                        main()
                else:
                        print("\t")
                        print("invalid choice")
        elif choice==2:
                print("\t")
                viewchoice=int(input("which table\n 1.Books\n 2.Borrower\n 3.Dealer\n 4.Main Menu\n Enter the choice :"))
                if viewchoice==1:
                        print("\t")
                        bookchoice=int(input("What do you want to view\n 1.Full table\n 2.No of books available\n 3.No of books according to the catergory : "))
                        if bookchoice==1:
                                viewbooks()
                        elif bookchoice==2:
                                viewnobooks()
                        elif bookchoice==3:
                                viewnobookscat()
        
                        else:
                                print("\t")
                                print("Invalid choice")
                                
                elif viewchoice==2:
                        print("\t")
                        borrowerchoice=int(input("What do you want to view\n 1.Full table\n 2.Search details of borrower who returned the books within the date\n 3.Details of borrower who returned late\n Enter the choice :"))
                        if borrowerchoice==1:
                                viewborrower()
                        elif borrowerchoice==2:
                                viewborrowerdate()
                        elif borrowerchoice==3:
                                viewlateborrower()
                        else:
                                print("\t")
                                print("Invalid Choice")
                elif viewchoice==3:
                        print("\t")
                        dealerchoice=int(input("What do you want to view\n 1.Full table\n 2.Books supplied by the dealer to Library \n 3.No of books supplied by the dealer in each catergory :"))
                        if dealerchoice==1:
                                viewdealer()
                        elif dealerchoice==2:
                                viewdealerbooks()
                        elif dealerchoice==3:
                                viewdealercat()
                        else:
                                print("\t")
                                print("Invalid choice")
                elif viewchoice==4:
                        main()
                else:
                        print("\t")
                        print("Invalid choice")
        elif choice==3:
                print("\t")
                updatechoice=int(input("Which table do you want to update\n 1.Books\n 2.Borrower\n 3.Dealer\n 4.Main Menu\n Enter the choice :"))
                if updatechoice==1:
                        updatebooks()
                elif updatechoice==2:
                        updateborrower()
                elif updatechoice==3:
                        updatedealer()
                elif updatechoice==4:
                        print("\t")
                        main()
                else:
                        print("\t")
                        print("invalid choice")
        elif choice==4:
                exit 
main()
con.close()
print("Thank you for using Library Mangement")
                

                
                        
                        












        
