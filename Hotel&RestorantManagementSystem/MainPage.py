from tkinter import *
from PIL import Image,ImageTk
from RoomAllotmentStatus import RoomAllotmentStatus
from CustomersDetails import CustomerDetails
from HotelBillGeneration import HotelBillGeneration
from hotelCustomerHistory import CustomerHistory
from HotelBillrecord import HotelBillRecord
from ItemAndPriceManipulation import ItemAndPrice
from BillGeneration import BillGeneration
from FoodBillrecord import FoodBillRecord
from LoginRegistrationHr import LoginRegistration
from HotelHelp import HelpH
from RestoHelp import HelpR
from AdminHelp import HelpA

class MainPage:
    def __init__(self,window):
        self.window=window
        self.window.title("MainPage")
        self.window.geometry("1280x725+0+0")
        #self.window.configure(bg="#e8e7dc")

        Headinglabel=Label(self.window,text="Hotel And Restorant Management System",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)
        #self.window.wm_attributes('-transparentcolor', '#ab23ff')

        HotelrestoLogo=Image.open(r"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\VandVHotelResto.png")
        HotelrestoLogo=HotelrestoLogo.resize((30,30))
        self.photoimgcr=ImageTk.PhotoImage(HotelrestoLogo)
        logoLabel=Label(Headinglabel,image=self.photoimgcr,bd=0,relief=RIDGE,bg="black")
        logoLabel.place(x=0,y=0,width=30,height=30)

        HotelrestoLogo1=Image.open(r"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\VandVHotelResto.png")
        HotelrestoLogo1=HotelrestoLogo1.resize((30,30))
        self.photoimgcr1=ImageTk.PhotoImage(HotelrestoLogo1)
        logoLabel1=Label(Headinglabel,image=self.photoimgcr,bd=0,relief=RIDGE,bg="black")
        logoLabel1.place(x=1230,y=0,width=30,height=30)

        self.Demofrmae=Frame(self.window,height=600,width=1000,bd=5,bg="white",relief=RIDGE)
        self.Demofrmae.place(x=250,y=90)

        HotelrestoLogo2=Image.open(r"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\Hotel.jpg")
        HotelrestoLogo2=HotelrestoLogo2.resize((1000,600))
        self.photoimgcr2=ImageTk.PhotoImage(HotelrestoLogo2)
        logoLabel2=Label(self.Demofrmae,image=self.photoimgcr2,bd=0,relief=RIDGE,bg="black")
        logoLabel2.place(x=0,y=0,width=990,height=590)

        HotelrestoLogo3=Image.open(r"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\mainpage.jpg")
        HotelrestoLogo3=HotelrestoLogo3.resize((220,200))
        self.photoimgcr3=ImageTk.PhotoImage(HotelrestoLogo3)
        logoLabel3=Label(self.window,image=self.photoimgcr3,bd=0,relief=RIDGE,bg="black")
        logoLabel3.place(x=18,y=295,width=220,height=200)

        HotelrestoLogo4=Image.open(r"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\food.jpg")
        HotelrestoLogo4=HotelrestoLogo4.resize((220,200))
        self.photoimgcr4=ImageTk.PhotoImage(HotelrestoLogo4)
        logoLabel4=Label(self.window,image=self.photoimgcr4,bd=0,relief=RIDGE,bg="black")
        logoLabel4.place(x=18,y=500,width=220,height=200)

        HotelrestoLogo5=Image.open(r"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\VandVHotelResto.png")
        HotelrestoLogo5=HotelrestoLogo5.resize((220,200))
        self.photoimgcr5=ImageTk.PhotoImage(HotelrestoLogo5)
        logoLabel5=Label(self.window,image=self.photoimgcr5,bd=0,relief=RIDGE,bg="black")
        logoLabel5.place(x=18,y=90,width=220,height=200)

        Hotelbutton=Menubutton(self.window,text="Hotel",font=("times new roman",18,"bold"),bg="black",fg="gold",width=8,bd=2,relief=SUNKEN)
        #Hotelbutton.place(x=755,y=45)
        Hotelbutton.grid()
        Hotelbutton.menu=Menu(Hotelbutton,tearoff=0,font=("Arial Black",13,"bold"),bg="#fccb42",bd=5,relief=SUNKEN)
        Hotelbutton["menu"]=Hotelbutton.menu
        Hotelbutton.menu.add_command(label="RoomStatus",activebackground="black",activeforeground="gold",command=self.RoomStatus)
        Hotelbutton.menu.add_separator()
        Hotelbutton.menu.add_command(label="CustomerDetail's",activebackground="black",activeforeground="gold",command=self.CustomerDetails)
        Hotelbutton.menu.add_separator()
        Hotelbutton.menu.add_command(label="RecentBill",activebackground="black",activeforeground="gold",command=self.HotelBillGeneration)
        Hotelbutton.menu.add_separator()
        Hotelbutton.menu.add_command(label="CustomerHistory",activebackground="black",activeforeground="gold",command=self.CustomerHistory)
        Hotelbutton.menu.add_separator()
        Hotelbutton.menu.add_command(label="BillRecord's",activebackground="black",activeforeground="gold",command=self.HotelBillRecord)
        Hotelbutton.menu.add_separator()
        Hotelbutton.menu.add_command(label="Help?..",activebackground="black",activeforeground="gold",command=self.HotelHelp)
        Hotelbutton.place(x=755,y=45)

        Restobutton=Menubutton(self.window,text="Restorant",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=2,relief=SUNKEN)
        #Restobutton.place(x=880,y=45)
        Restobutton.grid()
        Restobutton.menu=Menu(Restobutton,tearoff=0,font=("Arial Black",13,"bold"),bg="#fccb42",bd=5,relief=SUNKEN)
        Restobutton["menu"]=Restobutton.menu
        Restobutton.menu.add_command(label="FoodItem's",activebackground="black",activeforeground="gold",command=self.ItemAndPrice)
        Restobutton.menu.add_separator()
        Restobutton.menu.add_command(label="FoodBillGeneration",activebackground="black",activeforeground="gold",command=self.BillGeneration)
        Restobutton.menu.add_separator()
        Restobutton.menu.add_command(label="BillRecord's",activebackground="black",activeforeground="gold",command=self.FoodBillRecord)
        Restobutton.menu.add_separator()
        Restobutton.menu.add_command(label="Help?..",activebackground="black",activeforeground="gold",command=self.RestoHelp)
        Restobutton.place(x=880,y=45)

        Admin=Menubutton(self.window,text="Admin",font=("times new roman",18,"bold"),bg="black",fg="gold",width=8,bd=2,relief=SUNKEN)
        #Admin.place(x=1005,y=45)
        Admin.grid()
        Admin.menu=Menu(Admin,tearoff=0,font=("Arial Black",13,"bold"),bg="#fccb42",bd=5,relief=SUNKEN)
        Admin["menu"]=Admin.menu
        Admin.menu.add_command(label="Staff Registration",activebackground="black",activeforeground="gold",command=self.LoginRegistration)
        Admin.menu.add_separator()
        Admin.menu.add_command(label="Help?..",activebackground="black",activeforeground="gold",command=self.AdminHelp)
        Admin.place(x=1005,y=45)

        logout=Button(self.window,text="LogOut",font=("times new roman",14,"bold"),bg="black",fg="gold",width=9,bd=2,relief=SUNKEN,command=self.destory)
        logout.place(x=1130,y=45)

        hotelname=Label(self.window,text="V & V Hotel and Restorant",font=("ALGERIAN",25,"bold"),fg="green")
        hotelname.place(x=25,y=40)

        hotelthought=Label(self.window,text="we serve love and respect.",font=("times new roman",12,"bold"),fg="black")
        hotelthought.place(x=515,y=60)

    def destory(self):
        self.window.destroy()

    def RoomStatus(self):
        self.new_window=Toplevel(self.window)
        self.app=RoomAllotmentStatus(self.new_window)

    def CustomerDetails(self):
        self.new_window=Toplevel(self.window)
        self.app=CustomerDetails(self.new_window)

    def HotelBillGeneration(self):
        self.new_window=Toplevel(self.window)
        self.app=HotelBillGeneration(self.new_window)

    def CustomerHistory(self):
        self.new_window=Toplevel(self.window)
        self.app=CustomerHistory(self.new_window)

    def HotelBillRecord(self):
        self.new_window=Toplevel(self.window)
        self.app=HotelBillRecord(self.new_window)

    def ItemAndPrice(self):
        self.new_window=Toplevel(self.window)
        self.app=ItemAndPrice(self.new_window)

    def BillGeneration(self):
        self.new_window=Toplevel(self.window)
        self.app=BillGeneration(self.new_window)

    def FoodBillRecord(self):
        self.new_window=Toplevel(self.window)
        self.app=FoodBillRecord(self.new_window)

    def LoginRegistration(self):
        self.new_window=Toplevel(self.window)
        self.app=LoginRegistration(self.new_window)

    def HotelHelp(self):
        self.new_window=Toplevel(self.window)
        self.app=HelpH(self.new_window)

    def RestoHelp(self):
        self.new_window=Toplevel(self.window)
        self.app=HelpR(self.new_window)

    def AdminHelp(self):
        self.new_window=Toplevel(self.window)
        self.app=HelpA(self.new_window)
        



if __name__=="__main__":
    window=Tk()
    obj=MainPage(window)
    window.mainloop()
