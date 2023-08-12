from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
import datetime
from CustomersDetails import CustomerDetails

class RoomAllocation:
    def __init__(self,window):
        self.window=window
        self.window.title("RoomAllocation")
        self.window.geometry("1280x725+0+0")
        #self.window.configure(bg="#e8e7dc")

        #variable Declaration
        self.floorno=StringVar()
        self.roomcode=StringVar()
        self.floorno=StringVar()
        self.roomtype=StringVar()
        self.roomno=StringVar()
        self.customerref=StringVar()
        self.customername=StringVar()
        self.gender=StringVar()
        self.nationality=StringVar()
        self.mobile=StringVar()
        self.email=StringVar()
        self.idproof=StringVar()
        self.idnumber=StringVar()
        self.Relativenumber=StringVar()
        self.address=StringVar()
        self.pincode=StringVar()
        self.securityDep=StringVar()
        self.remark=StringVar()
        
        
        
        
        
        
        

        #function calling
        code=self.SelectedRoom()
        print(code)
        ref=self.CustomerRef()
        print(ref)
        

        Headinglabel=Label(self.window,text="Room-Allocation-Form",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)

        self.MainFramelabel=LabelFrame(self.window,text="Customer Detail's",font=("times new roman",19,"bold"),bd=4,width=1260,height=680)
        self.MainFramelabel.place(x=10,y=40)

        customerRef=Label(self.MainFramelabel,text="Customer Ref:-",font=("times new roman",15,"bold"))
        customerRef.place(x=10,y=10)

        customerRefE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.customerref)
        customerRefE.place(x=180,y=15)
        customerRefE.insert(0,ref+1)
        customerRefE.configure(state=DISABLED)

        customerName=Label(self.MainFramelabel,text="Customer Name:-",font=("times new roman",15,"bold"))
        customerName.place(x=10,y=60)

        customerNameE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.customername)
        customerNameE.place(x=180,y=65)

        customerGender=Label(self.MainFramelabel,text="Gender:-",font=("times new roman",15,"bold"))
        customerGender.place(x=10,y=110)

        combo_gender=ttk.Combobox(self.MainFramelabel,font=("arial",12,"bold"),width=27,state="readonly",textvariable=self.gender)
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.place(x=180,y=115)

        customerNationality=Label(self.MainFramelabel,text="Nationality:-",font=("times new roman",15,"bold"))
        customerNationality.place(x=10,y=160)

        customerNationalityE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.nationality)
        customerNationalityE.place(x=180,y=165)

        customerMobile=Label(self.MainFramelabel,text="Mobile:-",font=("times new roman",15,"bold"))
        customerMobile.place(x=10,y=210)

        customerMobileE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.mobile)
        customerMobileE.place(x=180,y=215)

        customerEmail=Label(self.MainFramelabel,text="Email:-",font=("times new roman",15,"bold"))
        customerEmail.place(x=10,y=260)

        customerEmailE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.email)
        customerEmailE.place(x=180,y=265)

        customerIdproof=Label(self.MainFramelabel,text="Identity Card:-",font=("times new roman",15,"bold"))
        customerIdproof.place(x=10,y=310)

        customerIdproofE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.idproof)
        customerIdproofE.place(x=180,y=315)

        customerIdNumber=Label(self.MainFramelabel,text="Identity Number:-",font=("times new roman",15,"bold"))
        customerIdNumber.place(x=10,y=360)

        customerIdNumberE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.idnumber)
        customerIdNumberE.place(x=180,y=365)

        customerRelative=Label(self.MainFramelabel,text="Relative Contact:-",font=("times new roman",15,"bold"))
        customerRelative.place(x=10,y=410)

        customerRelativeE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.Relativenumber)
        customerRelativeE.place(x=180,y=415)

        customerAddress=Label(self.MainFramelabel,text="Residence Addr:-",font=("times new roman",15,"bold"))
        customerAddress.place(x=10,y=460)

        customerAddresE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.address)
        customerAddresE.place(x=180,y=465)

        customerAddressPin=Label(self.MainFramelabel,text="Residence Pincode:-",font=("times new roman",14,"bold"))
        customerAddressPin.place(x=10,y=510)

        customerAddressPinE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.pincode)
        customerAddressPinE.place(x=180,y=515)

        HotelrestoLogo=Image.open(r"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\VandVHotelResto.png")
        HotelrestoLogo=HotelrestoLogo.resize((800,490))
        self.photoimgcr=ImageTk.PhotoImage(HotelrestoLogo)
        logoLabel=Label(self.MainFramelabel,image=self.photoimgcr,bd=2,relief=RIDGE)
        logoLabel.place(x=550,y=0,width=600,height=350)

        RoomFloor=Label(self.MainFramelabel,text="Floor No.:-",font=("times new roman",14,"bold"))
        RoomFloor.place(x=10,y=560)

        customerfloorno=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.floorno)
        customerfloorno.place(x=180,y=565)
        customerfloorno.insert(0,code[1])
        customerfloorno.configure(state=DISABLED)

        RoomType=Label(self.MainFramelabel,text="Room Type.:-",font=("times new roman",14,"bold"))
        RoomType.place(x=10,y=610)

        customerroomtype=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.roomtype)
        customerroomtype.place(x=180,y=615)
        customerroomtype.insert(0,code[2])
        customerroomtype.configure(state=DISABLED)

        RoomNum=Label(self.MainFramelabel,text="Room Number.:-",font=("times new roman",14,"bold"))
        RoomNum.place(x=630,y=360)

        customerroomtype=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.roomno)
        customerroomtype.place(x=780,y=360)
        customerroomtype.insert(0,code[3])
        customerroomtype.configure(state=DISABLED)

        customerRoomCode=Label(self.MainFramelabel,text="Room Code:-",font=("times new roman",14,"bold"))
        customerRoomCode.place(x=630,y=410)

        customerRoomCodeE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.roomcode)
        customerRoomCodeE.place(x=780,y=415)
        customerRoomCodeE.insert(0,code[0])
        customerRoomCodeE.configure(state=DISABLED)

        customerSecurityDep=Label(self.MainFramelabel,text="Security Deposite:-",font=("times new roman",13,"bold"))
        customerSecurityDep.place(x=630,y=460)

        customerSecE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.securityDep)
        customerSecE.place(x=780,y=465)

        customerRemark=Label(self.MainFramelabel,text="Remark:-",font=("times new roman",13,"bold"))
        customerRemark.place(x=630,y=510)

        customerRemarkE=Entry(self.MainFramelabel,font=("arial",13,"bold"),width=29,textvariable=self.remark)
        customerRemarkE.place(x=780,y=515)

        Allot=Button(self.MainFramelabel,font=("times new roman",16,"bold"),text="Allocate",fg="yellow",bg="black",width=8,command=self.Allocate)
        Allot.place(x=680,y=590)

        clearF=Button(self.MainFramelabel,font=("times new roman",16,"bold"),text="Clear",fg="yellow",bg="black",command=self.Clear)
        clearF.place(x=800,y=590)

        ShowStat=Button(self.MainFramelabel,font=("times new roman",16,"bold"),text="Customer's",fg="yellow",bg="black",command=self.CustomerDetails)
        ShowStat.place(x=880,y=590)

    def SelectedRoom(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from temporaryroomnumber")
        for i in my_cursor:
            print(i)
        return i

    def CustomerRef(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select COUNT(*) from customerhistory")
        for i in my_cursor:
            print("customer ref",i[0])
        return i[0]

    def Allocate(self):
        if (self.customername.get()=="" or self.gender.get()=="" or self.nationality.get()=="" or self.mobile.get()=="" or self.email.get()=="" or
             self.idproof.get()=="" or self.idnumber.get()=="" or self.Relativenumber.get()=="" or self.address.get()=="" or self.pincode.get()=="" or
             self.floorno.get()=="" or self.roomtype.get()=="" or self.roomno.get()=="" or self.roomcode.get()=="" or self.securityDep.get()=="" or
             self.remark.get()==""):
            messagebox.showinfo("Warning","All Field Are Required",parent=self.window)
        else:
            floorno=self.floorno.get()
            floorno=int(floorno)
            roomno=self.roomno.get()
            roomno=int(roomno)
            roomcode=self.roomcode.get()
            roomcode=int(roomcode)
        
            ref=self.CustomerRef()
            print(type(ref))
            current=datetime.datetime.now()
            print("current datetime:",current)
            current=str(current)
            conn=mysql.connector.connect(host="localhost",user="root",password="vicky@123//",database="hotelandrestoproject")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT into allocatedroomdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                   ref+1,
                                                                                                                                   self.customername.get(),
                                                                                                                                   self.gender.get(),
                                                                                                                                   self.nationality.get(),
                                                                                                                                   self.mobile.get(),
                                                                                                                                   self.email.get(),
                                                                                                                                   self.idproof.get(),
                                                                                                                                   self.idnumber.get(),
                                                                                                                                   self.Relativenumber.get(),
                                                                                                                                   self.address.get(),
                                                                                                                                   self.pincode.get(),
                                                                                                                                   floorno,
                                                                                                                                   self.roomtype.get(),
                                                                                                                                   roomno,
                                                                                                                                   roomcode,
                                                                                                                                   self.securityDep.get(),
                                                                                                                                   self.remark.get(),
                                                                                                                                   current,
                                                                                                                                   current
                                                                                                                                   ))
            conn.commit()
            conn.close()


            conn=mysql.connector.connect(host="localhost",user="root",password="vicky@123//",database="hotelandrestoproject")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT into customerhistory values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                               ref+1,
                                                                                               self.customername.get(),
                                                                                               self.mobile.get(),
                                                                                               self.address.get()+" "+self.pincode.get(),
                                                                                               self.idproof.get(),
                                                                                               self.idnumber.get(),
                                                                                               roomcode,
                                                                                               current,
                                                                                               current
                                                                                               ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Note!","Room Alloted to {} Successfully".format(self.customername.get()),parent=self.window)
            self.DestroyWindow()


    def DestroyWindow(self):
        self.window.destroy()

    def CustomerDetails(self):
        self.new_window=Toplevel(self.window)
        self.app=CustomerDetails(self.new_window)

    def Clear(self):
        self.customername.set("")
        self.nationality.set("")
        self.mobile.set("")
        self.email.set("")
        self.idproof.set("")
        self.idnumber.set("")
        self.Relativenumber.set("")
        self.address.set("")
        self.pincode.set("")
        self.securityDep.set("")
        self.remark.set("")
        


    

        
        

        



if __name__=="__main__":
    window=Tk()
    obj=RoomAllocation(window)
    window.mainloop()


#customer Ref Randome number#Room number code security dep remark#add,show databases;clear,
#Name of Cutomer
#Relative mobile number.
#gender(spinner)
#Nationality(spinner)
#pincode
#mobile
#email
#idprooof(spinner)
#enable filed if foreniner
#id number
#remark#
#security deposite#
#room(floor and type included)#
#address
#Same page allotmen sttus treeview
#room code validation

