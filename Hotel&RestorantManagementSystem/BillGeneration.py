from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import tkinter as tk
import mysql.connector
import os
import datetime

class BillGeneration:
    def __init__(self,window):
        self.window=window
        self.window.title("Bill Generation")
        self.window.geometry("1280x725+0+0")
        #self.window.configure(bg="#e8e7dc")

        global DelQueue
        DelQueue=[]
        

        #variabel decalration
        self.itemname=StringVar()
        self.itemqnty=StringVar()
        self.itemgst=StringVar()
        self.itemprice=StringVar()

        self.Headinglabel=Label(self.window,text="Bill Generation",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        self.Headinglabel.place(x=0,y=0)

        self.Bill_DataFrame=Frame(self.window,height=550,width=500,bg="grey",bd=2,relief=RIDGE)
        self.Bill_DataFrame.place(x=720,y=90)

        self.Addbillitem=LabelFrame(self.window,height=200,text="Add Bill Item's",width=600,bd=2,relief=RIDGE,font=("times new roman",15,"bold"))
        self.Addbillitem.place(x=50,y=375)

        self.itemLabel=Label(self.Addbillitem,text="Item:-",font=("times new roman",15,"bold"))
        self.itemLabel.place(x=5,y=5)

        self.itemEntry=Entry(self.Addbillitem,font=("times new roman",15,"bold"),width=35,textvariable=self.itemname,state=DISABLED)
        self.itemEntry.place(x=100,y=5)

        self.qntyLabel=Label(self.Addbillitem,text="Quantity:-",font=("times new roman",15,"bold"))
        self.qntyLabel.place(x=5,y=45)

        self.qntyEntry=Entry(self.Addbillitem,font=("times new roman",15,"bold"),width=35,textvariable=self.itemqnty)
        self.qntyEntry.place(x=100,y=45)

        self.GstLabel=Label(self.Addbillitem,text="GST(%):-",font=("times new roman",15,"bold"))
        self.GstLabel.place(x=5,y=85)

        self.GstEntry=Entry(self.Addbillitem,font=("times new roman",15,"bold"),width=35,textvariable=self.itemgst)
        self.GstEntry.place(x=100,y=85)

        self.Addbtn=Button(self.Addbillitem,font=("times new roman",15,"bold"),bg="Black",fg="yellow",text="ADD",width=7,command=self.Additem)
        self.Addbtn.place(x=120,y=125)

        self.Updbtn=Button(self.Addbillitem,font=("times new roman",15,"bold"),bg="Black",fg="yellow",text="UPDATE",width=7,command=self.Update)
        self.Updbtn.place(x=225,y=125)

        self.Delbtn=Button(self.Addbillitem,font=("times new roman",15,"bold"),bg="Black",fg="yellow",text="DELETE",width=7,command=self.DeleteItem)
        self.Delbtn.place(x=330,y=125)

        refreshfield=Button(self.window,text="C",fg="yellow",bg="black",font=("ALGERIAN",5),width=72,command=self.clear)
        refreshfield.place(y=580,x=180)

        self.Delbillbtn=Button(self.window,font=("times new roman",15,"bold"),bg="Black",fg="yellow",text="Delete Bill",width=11,command=self.DeleteBill)
        self.Delbillbtn.place(x=337,y=650)

        self.Genbillbtn=Button(self.window,font=("times new roman",15,"bold"),bg="Black",fg="yellow",text="Generate Bill",width=11,command=self.generateBill)
        self.Genbillbtn.place(x=180,y=650)

        self.CalBillbtn=Button(self.window,font=("times new roman",16,"bold"),bg="Black",fg="yellow",text="!!! Calculate Bill !!!",width=24,command=self.gstcount)
        self.CalBillbtn.place(x=180,y=600)

        HotelrestoLogo=Image.open(r"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\VandVHotelResto.png")
        HotelrestoLogo=HotelrestoLogo.resize((490,490))
        self.photoimgcr=ImageTk.PhotoImage(HotelrestoLogo)
        logoLabel=Label(self.window,image=self.photoimgcr,bd=0,relief=RIDGE)
        logoLabel.place(x=120,y=50,width=400,height=300)


        self.Data=Button(self.window,font=("times new roman",15,"bold"),bg="Black",fg="yellow",text="Stuff's",width=10,command=self.Stuff)
        self.Data.place(x=820,y=660)

        self.Record=Button(self.window,font=("times new roman",15,"bold"),bg="Black",fg="yellow",text="R",width=2,command=self.Record)
        self.Record.place(x=965,y=660)

        self.Bill=Button(self.window,font=("times new roman",16,"bold"),bg="Black",fg="yellow",text="Bill",width=10,command=self.billitem)
        self.Bill.place(x=1015,y=660)

        #function calling
        self.Stuff()
        self.CleanQuit()
        self.FileNaming()
        """out=self.gstcount(10)
        print(out)"""
        #self.gstdisabled()

    def clear(self):
        self.fieldreset("Item")
        self.fieldreset("Quantity")
        self.fieldreset("Gst")
        self.deltemdata()
        

    def gstdisabled(self):
        if len(self.itemgst.get())!=0:
            self.GstEntry.configure(state=DISABLED)
        elif len(self.itemgst.get())==0:
            self.GstEntry.configure(state=NORMAL)
            

    def Stuff(self):
        global tree
        tree=ttk.Treeview(self.Bill_DataFrame)
        tree["columns"]=("sr_no.","item","price")

        s=ttk.Style(self.Bill_DataFrame)
        s.theme_use("classic")
        s.configure(".",font=("Helvetica",11,"bold"))
        s.configure("Treeview.Heading",foreground="black",font=("Helvetica",11,"bold"))

        tree['show']='headings'

        tree.column("sr_no.",width=70,minwidth=70,anchor=tk.CENTER,stretch=0)
        tree.column("item",width=315,minwidth=315,anchor=tk.CENTER,stretch=0)
        tree.column("price",width=115,minwidth=115,anchor=tk.CENTER,stretch=0)

        tree.heading("sr_no.",text="Sr_No.",anchor=tk.CENTER)
        tree.heading("item",text="Item's List",anchor=tk.CENTER)
        tree.heading("price",text="Price(per unit)",anchor=tk.CENTER)
        tree.bind("<ButtonRelease-1>",self.get_cursor)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        query="select * from restoitems "
        my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
        
        i=0
        for ro in my_cursor:
            tree.insert('',i+1,text="",values=(i+1,ro[0],ro[1]))
            i=i+1

        tree.place(x=0,y=0,width=495,height=550)

    def get_cursor(self,event=""):
        global itemprice
        row_cursor=tree.focus()
        content=tree.item(row_cursor)
        row=content["values"]

        if len(row)==0:
            messagebox.showinfo("Warning","Ooops...",parent=self.window)
        else:
            self.itemname.set(row[1])
            self.itemprice.set(row[2])


    def totalcount(self,price,n):
        totalcount=n*price
        print(totalcount)
        return totalcount

    def Additem(self):
        item=self.itemname.get()
        gst=self.itemgst.get()
        price=self.itemprice.get()
        n=self.itemqnty.get()
        #print("retfun",retfun)
        if gst=="" or item=="" or n=="":
            messagebox.showinfo("Warning","All Fields are Required!!!",parent=self.window)
        else:
            try:
                item=int(item)
                messagebox.showinfo("Warning","Item name Can't be numeric",parent=self.window)
            except:
                mes=""
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
                    my_cursor=conn.cursor()
                    mes="Quantity"
                    n=int(n)
                    mes="GST"
                    gst=int(gst)
                    mes="Price"
                    price=int(price)
                    my_cursor.execute("Select COUNT(*) from temporaryreceiptdata Where Item='{}'".format(item))
                    for i in my_cursor:
                        print("already data:",i[0])
                    if i[0]==1:
                        print("Here Bro")
                        my_cursor.execute("Select Priceperunit from restoitems Where Items='{}'".format(item))
                        for k in my_cursor:
                            print(k[0])
                        my_cursor.execute("Select Quantity from temporaryreceiptdata WHERE Item='{}'".format(item))
                        for j in my_cursor:
                            print(type(j[0]),j[0])
                        retfun=self.totalcount(int(k[0]),n+j[0])
                        my_cursor.execute("UPDATE temporaryreceiptdata SET Quantity='{}' ,Total='{}' WHERE Item='{}' ".format(n+j[0],retfun,item))
                        conn.commit()
                        conn.close()
                        self.billitem()
                        messagebox.showinfo("Warning","Quantity Added Successfully",parent=self.window)
                    elif i[0]==0:
                        retfun=self.totalcount(price,n)
                        my_cursor.execute("INSERT into temporaryreceiptdata values(%s,%s,%s,%s)",(
                                                                                              item,
                                                                                              n,
                                                                                              price,
                                                                                              retfun
                                                                                              ))
                        print("i am here")
                        conn.commit()
                        conn.close()
                        self.gstdisabled()
                        #self.billitem()
                        messagebox.showinfo("Note","Item added!!!",parent=self.window)
                        self.fieldreset("Item")
                        self.fieldreset("Quantity")
                    
                except:
                    messagebox.showinfo("Warning","{} can't be alphabetical/special symbol.".format(mes),parent=self.window)
                    if mes=="Quantity":
                        self.fieldreset("Quantity")
                    elif mes=="GST":
                        self.fieldreset("Gst")

    def deltemdata(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("Delete from temporaryreceiptdata")
        conn.commit()
        conn.close()
        

    def gstcount(self):
        try:
            gst=self.itemgst.get()
            gst=int(gst)
            conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from temporaryreceiptdata")
            temp=0
            for i in my_cursor:
                temp=temp+i[3]
            print(temp)

            gstamount=(gst/100)*temp
            messagebox.showinfo("Message","Subtotal:{}\nGstAmount:{}\nTotal:{}".format(temp,gstamount,temp+gstamount),parent=self.window)
            #self.deltemdata()
            #self.fieldreset("Gst")
            return round(gstamount),round(temp)
        
        except:
            messagebox.showinfo("Warning","Invalid Command")

    def fieldreset(self,which):
        if which=="Item":
            self.itemname.set("")
        elif which=="Quantity":
            self.itemqnty.set("")
        elif which=="Gst":
            self.itemgst.set("")
            self.gstdisabled()
            
            
        

        
            
            

       

    def billitem(self):
        global trees
        self.Bill_DataFrame=Frame(self.window,height=550,width=500,bd=2,relief=RIDGE,bg="white")
        self.Bill_DataFrame.place(x=720,y=90)

        BilLabel=Label(self.window,text="!!!-----------------------------Receipt--------------------------------!!!",font=("Cooper black",15))
        BilLabel.place(x=740,y=50)


        trees=ttk.Treeview(self.Bill_DataFrame)
        trees["columns"]=("Item","Qnty","Rate","Total")

        s=ttk.Style(self.Bill_DataFrame)
        s.theme_use("classic")
        s.configure(".",font=("Helvetica",11,"bold"))
        s.configure("Treeview.Heading",foreground="black",font=("Helvetica",11,"bold"),background="grey")

        trees['show']='headings'

        trees.column("Item",width=320,minwidth=320,anchor=tk.CENTER,stretch=0)
        trees.column("Qnty",width=50,minwidth=50,anchor=tk.CENTER,stretch=0)
        trees.column("Rate",width=60,minwidth=60,anchor=tk.CENTER,stretch=0)
        trees.column("Total",width=70,minwidth=70,anchor=tk.CENTER,stretch=0)


        trees.heading("Item",text="Item",anchor=tk.CENTER)
        trees.heading("Qnty",text="Qnty",anchor=tk.CENTER)
        trees.heading("Rate",text="Rate",anchor=tk.CENTER)
        trees.heading("Total",text="Total",anchor=tk.CENTER)
        trees.bind("<ButtonRelease-1>",self.get_cursorbill)

        conn=mysql.connector.connect(host="localhost",user="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from temporaryreceiptdata")
        i=0
        for ro in my_cursor:
            trees.insert('',i+1,text="",values=(ro[0],ro[1],ro[2],ro[3]))
            i=i+1
        trees.place(x=-3,y=0,width=500,height=550)

    def get_cursorbill(self,event=""):
        row_cursor=trees.focus()
        content=trees.item(row_cursor)
        row=content["values"]

        #print(row)
        if len(row)==0:
            messagebox.showinfo("Warning","Ooops...")
        else:
            self.itemname.set(row[0])
            self.itemqnty.set(row[1])

    def generateBill(self):
        #item=self.itemname.get()
        gst=self.itemgst.get()
        #n=self.itemqnty.get()
        Name=self.FileNaming()
        DelQueue.append(Name)
        if gst=="":
            messagebox.showinfo("Warning","Invalid Command",parent=self.window)
        else:
            f=open(f"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\BillFolder\{Name}","a")
            a=" "
            conn=mysql.connector.connect(username="root",password="vicky@123//",host="localhost",database="hotelandrestoproject")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from temporaryreceiptdata")
            Heading="""{}|-----------------------------------------------------------|
                    |{}V&V                            |
                    |{}Hotel and Restorant                    |
                    |{}Ghansoli Navi Mumbai ,Near Dmart Chinchali         | 
                    |{}Shop no.406 -400701                     |
                    |{}Phone No.:8451096034  GSTIN:-ASDFEX88897FNDUDJG3F     |
                    |{}Invoice No.:123454645DFD     Invoice Date:-12/12/2012   |
                    |{}--------------------------------------------------------- |
                    |{}Item's                       Qnty      Rate     Price    |""".format(a*20,a*28,a*20,a*8,a*19,a*5,a*3,a*1,a*2)
            f.write(Heading)
            for i in my_cursor:
                #for word spacing
                c=len(i[0])
                b=a*(29-c)
                d=len(str(i[1]))
                e=a*(10-d)
                f1=len(str(i[2]))
                g=a*(9-f1)
                f2=len(str(i[3]))
                h=a*(9-f2)
                bill="""\n{}|{}{}{}{}{}{}{}{}{}|""".format(a*20,a*2,i[0],b,i[1],e,i[2],g,i[3],h)
                f.write(bill)




            total=self.gstcount()
            subtotal=total[1]
            print(subtotal)
            sb=len(str(subtotal))
            sbt=a*(42-sb)
        
            gstamount=total[0]
            print(gstamount)
            gs=len(str(gstamount))
            gst=a*(40-gs)
        
            totals=subtotal+gstamount
            print(total)
            to=len(str(totals))
            total=a*(36-to)
        
            Tail="""\n{}|{}--------------------------------------------------------- |\n{}|{}{}|\n{}|{}{}|\n{}|{}  #SubTotal :-{}Rs{}|\n{}|{}  #GstAmount:-{}Rs  {}|\n{}|{}  #Total    :-{}Rs Only {}|\n{}|{}{}|\n{}|{}{}|\n{}|{}{}|\n{}|{}Thank You Visit Again!!!{}|\n{}|{}{}|\n{}|{}{}|\n{}|{}|\n\n\n\n\n
""".format(a*20,a*1,a*20,a*1,a*58,a*20,a*1,a*58,a*20,a*1,subtotal,sbt,a*20,a*1,gstamount,gst,a*20,a*1,totals,total,a*20,a*1,a*58,a*20,a*1,a*58,a*20,a*1,a*58,a*20,a*18,a*17,a*20,a*1,a*58,a*20,a*1,a*58,a*20,"-"*59)
            f.write(Tail)
            f.close()

            self.deltemdata()
            self.fieldreset("Gst")
            self.billrecord(Name,totals)
            messagebox.showinfo("NOTE","{}".format(Name),parent=self.window)

    def Update(self):
        n=self.itemqnty.get()
        item=self.itemname.get()
        if n=="" or item=="":
            messagebox.showinfo("Warning","invalid Command",parent=self.window)
        else:
            try:
                n=int(n)
                conn=mysql.connector.connect(username="root",password="vicky@123//",host="localhost",database="hotelandrestoproject")
                my_cursor=conn.cursor()
                my_cursor.execute("select COUNT(*) from temporaryreceiptdata WHERE Item='{}'".format(item))
                for i in my_cursor:
                    print("Have or not",i)
                if i[0]==0:
                    messagebox.showinfo("Warning","No Data Found",parent=self.window)
                elif(i[0]==1):
                    my_cursor.execute("Select Priceperunit from restoitems Where Items='{}'".format(item))
                    for k in my_cursor:
                        print("This is :",k[0])
                    retfun=self.totalcount(int(k[0]),int(n))
                    my_cursor.execute("UPDATE temporaryreceiptdata SET Quantity='{}',Total='{}' WHERE Item='{}' ".format(n,retfun,item))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Warning","Quantity Update successfully!!!",parent=self.window)
                    self.billitem()
            except:
                messagebox.showinfo("Warning","Quantity should Be in Numeric",parent=self.window)

    def DeleteItem(self):
        item=self.itemname.get()
        conn=mysql.connector.connect(username="root",password="vicky@123//",host="localhost",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select COUNT(*) from temporaryreceiptdata Where Item='{}'".format(item))
        for i in my_cursor:
            print("Present or not for delete",i[0])
        if i[0]==1:
            my_cursor.execute("DELETE from temporaryreceiptdata Where Item='{}'".format(item))
            conn.commit()
            conn.close()
            self.billitem()
            messagebox.showinfo("Warning","Bill Item Deleted Succesfully",parent=self.window)
        elif i[0]==0:
            messagebox.showinfo("Warning","No Such item in Bill to Delete!!!",parent=self.window)


    def CleanQuit(self):
        conn=mysql.connector.connect(username="root",password="vicky@123//",host="localhost",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("DELETE from temporaryreceiptdata")
        conn.commit()
        conn.close()

    def DeleteBill(self):
        if messagebox.askyesno("Warning","Do you want to delete recent bill?")==1:
            self.CleanQuit()
            self.fieldreset("Item")
            self.fieldreset("Quantity")
            self.fieldreset("Gst")
            self.gstdisabled()
            self.deltemdata()
            if len(DelQueue)==0:
                messagebox.showinfo("Warning","No Recent File to Delete",parent=self.window)
            else:
                delfile=DelQueue[-1]
                if os.path.exists(f"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\BillFolder\{delfile}"):
                    os.remove(f"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\BillFolder\{delfile}")
                    self.delbillrecord(delfile)
                    messagebox.showinfo("Note","{} File Deleted Successfully".format(delfile),parent=self.window)
                    DelQueue.clear()
                else:
                    print("The file does not exist")


    def FileNaming(self):
        current_time=datetime.datetime.now()
        print("year:",current_time.year,"\nMonth:",current_time.month,"\nDate:",current_time.day,"\nHour:",current_time.hour,"\nMinutes:",current_time.minute,"\nsecond:",current_time.second,"\nMicrosecond:",current_time.microsecond)
        Name="Bill"+str(current_time.year)+str(current_time.month)+str(current_time.day)+str(current_time.hour)+str(current_time.minute)+str(current_time.second)+str(current_time.microsecond)+".txt"
        print(Name)
        return Name

    def billrecord(self,name,total):
        current_time=datetime.datetime.now()
        print("year:",current_time.year,"\nMonth:",current_time.month,"\nDate:",current_time.day,"\nHour:",current_time.hour,"\nMinutes:",current_time.minute,"\nsecond:",current_time.second,"\nMicrosecond:",current_time.microsecond)

        datetimes=str(current_time.year)+"-"+str(current_time.month)+"-"+str(current_time.day)+"/"+str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
        print(datetimes)
        conn=mysql.connector.connect(username="root",password="vicky@123//",host="localhost",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select COUNT(*) from billrecord")
        for i in my_cursor:
            print("we have bill record:",i[0])
        my_cursor.execute("Insert into billrecord  values(%s,%s,%s,%s)",(
                                                                      i[0]+1,
                                                                      name,
                                                                      total,
                                                                      datetimes
                                                                        ))
        conn.commit()
        conn.close()

    def delbillrecord(self,name):
        conn=mysql.connector.connect(username="root",password="vicky@123//",host="localhost",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("DELETE from billrecord Where bill='{}'".format(name))
        conn.commit()
        conn.close()

    def Record(self):
        treeR=ttk.Treeview(self.Bill_DataFrame)
        treeR["columns"]=("serial","bill","total","datetimes")

        s=ttk.Style(self.Bill_DataFrame)
        s.theme_use("classic")
        s.configure(".",font=("Helvetica",11,"bold"))
        s.configure("Treeview.Heading",foreground="black",font=("Helvetica",11,"bold"),background="grey")

        treeR['show']='headings'

        treeR.column("serial",width=50,minwidth=50,anchor=tk.CENTER,stretch=0)
        treeR.column("bill",width=200,minwidth=200,anchor=tk.CENTER)
        treeR.column("total",width=70,minwidth=70,anchor=tk.CENTER)
        treeR.column("datetimes",width=150,minwidth=150,anchor=tk.CENTER,stretch=0)


        treeR.heading("serial",text="Serial",anchor=tk.CENTER)
        treeR.heading("bill",text="Bill",anchor=tk.CENTER)
        treeR.heading("total",text="Amount",anchor=tk.CENTER)
        treeR.heading("datetimes",text="Date",anchor=tk.CENTER)

        conn=mysql.connector.connect(host="localhost",user="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from billrecord")
        i=0
        for ro in my_cursor:
            treeR.insert('',i+1,text="",values=(ro[0],ro[1],ro[2],ro[3]))
            i=i+1
        treeR.place(x=-3,y=0,width=500,height=550)



        
        
        


            
        
    
if __name__=="__main__":
    window=Tk()
    obj=BillGeneration(window)
    window.mainloop()
    
    
