from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class ItemAndPrice:
    def __init__(self,window):
        self.window=window
        self.window.title("ItemAndPrice")
        self.window.geometry("1280x725+0+0")
        #self.window.configure(bg="#e8e7dc")



        #varible declaration
        self.AddEntry=StringVar()
        self.AddValue=StringVar()
        self.Updateitem=StringVar()
        self.UpdatePrice=StringVar()
        self.deleteItem=StringVar()
        
        

        

        self.Headinglabel=Label(self.window,text="FoodStuffs",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        self.Headinglabel.place(x=0,y=0)

        self.Additemframe=LabelFrame(self.window,text="Add Item's",height=220,width=650,bd=2,relief=RIDGE,font=("times new roman",18,"bold"))
        self.Additemframe.place(x=10,y=40)

        self.AdditemframeLabel=Label(self.Additemframe,text="Enter Item Name:-",font=("arial",15,"bold"))
        self.AdditemframeLabel.place(x=20,y=20)

        self.AdditemframeEntry=Entry(self.Additemframe,textvariable=self.AddEntry,font=("arial",15,"bold"),width=30)
        self.AdditemframeEntry.place(x=200,y=20)

        self.AdditempriceLabel=Label(self.Additemframe,text="Enter Item Price:-",font=("arial",15,"bold"))
        self.AdditempriceLabel.place(x=20,y=70)

        self.AdditemPriceEntry=Entry(self.Additemframe,textvariable=self.AddValue,font=("arial",15,"bold"),width=30)
        self.AdditemPriceEntry.place(x=200,y=70)

        self.AdditemButton=Button(self.Additemframe,text="ADD",font=("times new roman",15,"bold"),bg="black",fg="yellow",width=8,command=self.Add)
        self.AdditemButton.place(x=250,y=130)

        self.AddClearButton=Button(self.Additemframe,text="CLEAR",font=("times new roman",15,"bold"),bg="black",fg="yellow",width=8,command=lambda:self.clear("self.AddEntry"))
        self.AddClearButton.place(x=400,y=130)




        self.Updateitemframe=LabelFrame(self.window,text="Update Item's",height=220,width=650,bd=2,relief=RIDGE,font=("times new roman",18,"bold"))
        self.Updateitemframe.place(x=10,y=280)

        self.itemframeLabel=Label(self.Updateitemframe,text="Enter Item Name:-",font=("arial",15,"bold"))
        self.itemframeLabel.place(x=20,y=20)

        #self.itemframeEntry=Entry(self.Updateitemframe,textvariable=self.Updateitem,font=("arial",15,"bold"),width=30)
        #self.itemframeEntry.place(x=200,y=20)

    

        self.updateitempriceLabel=Label(self.Updateitemframe,text="Updated Price:-",font=("arial",15,"bold"))
        self.updateitempriceLabel.place(x=20,y=70)

        self.updateitempriceEntry=Entry(self.Updateitemframe,textvariable=self.UpdatePrice,font=("arial",15,"bold"),width=30)
        self.updateitempriceEntry.place(x=200,y=70)

        self.UpdateitemButton=Button(self.Updateitemframe,text="UPDATE",font=("times new roman",15,"bold"),bg="black",fg="yellow",width=8,command=self.Update)
        self.UpdateitemButton.place(x=250,y=130)

        self.UpdateClearButton=Button(self.Updateitemframe,text="CLEAR",font=("times new roman",15,"bold"),bg="black",fg="yellow",width=8,command=lambda:self.clear("self.Updateitem"))
        self.UpdateClearButton.place(x=400,y=130)






        self.Deleteitemframe=LabelFrame(self.window,text="Delete Item's",height=150,width=650,bd=2,relief=RIDGE,font=("times new roman",18,"bold"))
        self.Deleteitemframe.place(x=10,y=520)

        self.DeleteitemframeLabel=Label(self.Deleteitemframe,text="Enter Item Name:-",font=("arial",15,"bold"))
        self.DeleteitemframeLabel.place(x=20,y=20)

        #self.DeleteitemframeEntry=Entry(self.Deleteitemframe,textvariable=self.deleteItem,font=("arial",15,"bold"),width=30)
        #self.DeleteitemframeEntry.place(x=200,y=20)


        self.DelteitemButton=Button(self.Deleteitemframe,text="DELETE",font=("times new roman",15,"bold"),bg="black",fg="yellow",width=8,command=self.Delete)
        self.DelteitemButton.place(x=250,y=65)

        self.DeleteClearButton=Button(self.Deleteitemframe,text="CLEAR",font=("times new roman",15,"bold"),bg="black",fg="yellow",width=8,command=lambda:self.clear("self.deleteItem"))
        self.DeleteClearButton.place(x=400,y=65)


        


        self.ViewItems=LabelFrame(self.window,text="Stuff's",height=630,width=550,bd=2,relief=RIDGE,font=("times new roman",18,"bold"))
        self.ViewItems.place(x=700,y=40)

        self.ViewItemsframe=LabelFrame(self.window,height=510,width=500,bd=3,relief=RIDGE)
        self.ViewItemsframe.place(x=730,y=80)

        self.RefreshitemButton=Button(self.ViewItems,text="REFRESH",font=("times new roman",15,"bold"),bg="black",fg="yellow",width=8,command=self.Refresh)
        self.RefreshitemButton.place(x=220,y=537)

        #calling fucntion
        self.Refresh()
        self.updt()
        self.dele()

    def dele(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select Items from restoitems")
        l=[]
        for i in my_cursor.fetchall():
            l.append(i[0])

        combo_Items=ttk.Combobox(self.Deleteitemframe,textvariable=self.deleteItem,font=("arial",14,"bold"),width=29,state="readonly")
        combo_Items["value"]=l
        combo_Items.current(0)
        combo_Items.place(x=200,y=20)

    def updt(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select Items from restoitems")
        l=[]
        for i in my_cursor.fetchall():
            l.append(i[0])

        combo_Items=ttk.Combobox(self.Updateitemframe,textvariable=self.Updateitem,font=("arial",14,"bold"),width=29,state="readonly")
        combo_Items["value"]=l
        combo_Items.current(0)
        combo_Items.place(x=200,y=20)

        

    def Add(self):
        #messagebox.showinfo("Warning","ADD")
        print(self.AddEntry.get(),self.AddValue.get())
        if (self.AddEntry.get()=="" or self.AddValue.get()==""):
            messagebox.showinfo("Warning","None Of the Field Should Empty")

        else:
            try:
                int(self.AddEntry.get())
                messagebox.showinfo("Warning","Item Name Cannot be Numeric",parent=self.window)
            except:
                try:
                    int(self.AddValue.get())
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into restoitems values(%s,%s)",(
                                                                       self.AddEntry.get(),
                                                                       self.AddValue.get()
                                                                              ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Note","Your Data Added Successfully",parent=self.window)
                    self.clear("self.AddEntry")
                    self.Refresh()
                    self.updt()
                    self.dele()
                                                                            
                except:
                    messagebox.showinfo("Warning","Item Price Should be in Numeric Form",parent=self.window)
                    self.clear("self.AddEntry")

    def Update(self):
        print(self.Updateitem.get())
        if (self.Updateitem.get()==""):
            messagebox.showinfo("Warning","Please select item",parent=self.window)
        else:
            if (self.UpdatePrice.get()==""):
                messagebox.showinfo("Warning","Please Enter the Updated Price of selected item",parent=self.window)
            else:
                try:
                    int(self.UpdatePrice.get())
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
                    my_cursor=conn.cursor()
                    query="UPDATE restoitems SET Priceperunit='{}' Where Items='{}'".format(self.UpdatePrice.get(),self.Updateitem.get())
                    my_cursor.execute(query)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Warning","Your Data Updated Successfully",parent=self.window)
                    self.Refresh()
                    self.clear("self.Updateitem")
                    self.updt()
                    self.dele()
                except:
                    messagebox.showinfo("Warning","Please Enter the Price in Numeric form Only",parent=self.window)
                    self.clear("self.Updateitem")
        

    def Delete(self):
        #messagebox.showinfo("Warning","Delete")
        print(self.deleteItem)
        if(self.deleteItem.get()==""):
            messagebox.showinfo("Warning","Please select Item which you want to Delete",parent=self.window)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
            my_cursor=conn.cursor()
            if messagebox.askyesno("Warning","Are you Want to delete {} item from the list".format(self.deleteItem.get()),parent=self.window)==True:
                my_cursor.execute("DELETE from restoitems Where Items='{}'".format(self.deleteItem.get()))
                conn.commit()
                conn.close()
                self.Refresh()
                messagebox.showinfo("Warning","Your Item Deleted Successfully",parent=self.window)
                self.clear("self.deleteItem")
                self.updt()
                self.dele()
            else:
                messagebox.showinfo("Alert","Operation Denied",parent=self.window)
                self.Refresh()
                self.clear("self.deleteItem")
            



    def Refresh(self):
        #messagebox.showinfo("Warning","Refresh")

        tree=ttk.Treeview(self.ViewItemsframe)
        tree["columns"]=("sr_no.","item","price")

        s=ttk.Style(self.ViewItemsframe)
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
        
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        query="select * from restoitems "
        my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
        
        i=0
        for ro in my_cursor:
            tree.insert('',i+1,text="",values=(i+1,ro[0],ro[1]))
            i=i+1

        tree.place(x=0,y=0,width=505,height=505)



    def clear(self,which):
        if ("self.AddEntry"==which):
            self.AddEntry.set("")
            self.AddValue.set("")
        elif ("self.Updateitem"==which):
            self.Updateitem.set("")
            self.UpdatePrice.set("")
        elif ("self.deleteItem"==which):
            self.deleteItem.set("")

        


        



if __name__=="__main__":
    window=Tk()
    obj=ItemAndPrice(window)
    window.mainloop()






















"""from tkinter import *

class ItemAndPrice:
    def __init__(self,window):
        self.window=window
        self.window.title("ItemAndPrice")
        self.window.geometry("1280x725+0+0")
        #self.window.configure(bg="#e8e7dc")

        Headinglabel=Label(self.window,text="FoodStuffs",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)

        



if __name__=="__main__":
    window=Tk()
    obj=ItemAndPrice(window)
    window.mainloop()"""

