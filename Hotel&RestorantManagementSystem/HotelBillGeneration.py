from tkinter import *
import datetime
import mysql.connector
from tkinter import ttk,messagebox
import time

class HotelBillGeneration:
    def __init__(self,window):
        self.window=window
        self.window.title("HotelBillGeneration")
        self.window.geometry("1280x725+0+0")
        #self.window.configure(bg="#e8e7dc")#room sttus block delete query,

        #calling
        cdata=self.customerdetail()

        #varible declaration
        self.cref=StringVar()
        self.name=StringVar()
        self.phone=StringVar()
        self.email=StringVar()
        self.address=StringVar()
        self.mode=StringVar()
        self.Nationality=StringVar()
        self.days=StringVar()
        self.date=StringVar()
        self.roomno=StringVar()
        self.roomtype=StringVar()
        self.price=StringVar()
        self.checkin=StringVar()
        self.checkout=StringVar()
        self.chg=StringVar()
        self.gst=StringVar()
        self.ttotal=StringVar()

        current=datetime.datetime.now()
        date="{}-{}-{}".format(current.year,current.month,current.day)
        print(date)
        

        Headinglabel=Label(self.window,text="Hotel Receipt",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)

        Billto=Label(self.window,text="Bill To:-",font=("times new roman",25,"bold"))
        Billto.place(x=5,y=45)

        ReceptNo=Label(self.window,text="Receipt No.:-",font=("times new roman",21,"bold"))
        ReceptNo.place(x=95,y=80)

        ReceipEnt=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.cref)
        ReceipEnt.place(x=295,y=85)
        ReceipEnt.insert(0,cdata[0])
        ReceipEnt.configure(state=DISABLED)

        Name=Label(self.window,text="Name:-",font=("times new roman",21,"bold"))
        Name.place(x=95,y=130)

        NameE=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.name)
        NameE.place(x=295,y=135)
        NameE.insert(0,cdata[1])
        NameE.configure(state=DISABLED)

        Phone=Label(self.window,text="Phone No.:-",font=("times new roman",21,"bold"))
        Phone.place(x=95,y=180)

        PhoneEnt=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.phone)
        PhoneEnt.place(x=295,y=185)
        PhoneEnt.insert(0,cdata[2])
        PhoneEnt.configure(state=DISABLED)

        Email=Label(self.window,text="Email:-",font=("times new roman",21,"bold"))
        Email.place(x=95,y=230)

        EmailEnt=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.email)
        EmailEnt.place(x=295,y=235)

        Address=Label(self.window,text="Address:-",font=("times new roman",21,"bold"))
        Address.place(x=95,y=280)

        AddEnt=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.address)
        AddEnt.place(x=295,y=285)
        AddEnt.insert(0,cdata[3])
        AddEnt.configure(state=DISABLED)

        Nationality=Label(self.window,text="Nationality:-",font=("times new roman",21,"bold"))
        Nationality.place(x=95,y=330)

        NationalityEnt=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.Nationality)
        NationalityEnt.place(x=295,y=335)

        Mode=Label(self.window,text="Payment Mode:-",font=("times new roman",20,"bold"))
        Mode.place(x=95,y=380)

        ModeEnt=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.mode)
        ModeEnt.place(x=295,y=385)

        Days=Label(self.window,text="No.Of Day's:-",font=("times new roman",21,"bold"))
        Days.place(x=95,y=430)

        DaysEnt=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.days)
        DaysEnt.place(x=295,y=435)


        Date=Label(self.window,text="Date:-",font=("times new roman",21,"bold"))
        Date.place(x=700,y=80)

        DateEnt=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.date)
        DateEnt.place(x=900,y=85)
        DateEnt.insert(0,date)
        DateEnt.configure(state=DISABLED)

        Room=Label(self.window,text="Room No.:-",font=("times new roman",21,"bold"))
        Room.place(x=700,y=130)

        RoomE=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.roomno)
        RoomE.place(x=900,y=135)
        RoomE.insert(0,cdata[6])
        RoomE.configure(state=DISABLED)

        Type=Label(self.window,text="Room Type:-",font=("times new roman",21,"bold"))
        Type.place(x=700,y=180)

        combo_roomtyp=ttk.Combobox(self.window,font=("arial",12,"bold"),width=27,state="readonly",textvariable=self.roomtype)
        combo_roomtyp["value"]=("Rk","1BHK","2BHK","3BHK")
        combo_roomtyp.current(0)
        combo_roomtyp.place(x=900,y=185)

        priceday=Label(self.window,text="Price/Day:-",font=("times new roman",21,"bold"))
        priceday.place(x=700,y=230)

        pricedayEnt=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.price)
        pricedayEnt.place(x=900,y=235)

        CheckIn=Label(self.window,text="CheckIn:-",font=("times new roman",21,"bold"))
        CheckIn.place(x=700,y=280)

        CheckInE=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.checkin)
        CheckInE.place(x=900,y=285)
        CheckInE.insert(0,cdata[7])
        CheckInE.configure(state=DISABLED)

        CheckO=Label(self.window,text="CheckOut:-",font=("times new roman",21,"bold"))
        CheckO.place(x=700,y=330)

        CheckOE=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.checkout)
        CheckOE.place(x=900,y=335)
        CheckOE.insert(0,cdata[8])
        CheckOE.configure(state=DISABLED)

        Chrg=Label(self.window,text="Charges(Rs):-",font=("times new roman",20,"bold"))
        Chrg.place(x=700,y=380)

        ChrgE=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.chg)
        ChrgE.place(x=900,y=385)

        Gst=Label(self.window,text="Gst(%):-",font=("times new roman",21,"bold"))
        Gst.place(x=700,y=430)

        GstE=Entry(self.window,font=("times new roman",16,"bold"),width=25,textvariable=self.gst)
        GstE.place(x=900,y=435)

        total=Label(self.window,text="Total:-",font=("times new roman",21,"bold"))
        total.place(x=550,y=500)

        Cal=Button(self.window,text="Calculate",font=("times new roman",18,"bold"),bg="black",fg="yellow",command=self.Total)
        Cal.place(x=450,y=600)

        global Bill
        Bill=Button(self.window,text="Bill",font=("times new roman",18,"bold"),bg="black",fg="yellow",command=self.Receipt,width=8,state=DISABLED )
        Bill.place(x=600,y=600)

        

        

        #self.Receipt()
    def Total(self):
        a=self.days.get()
        b=self.price.get()
        c=self.chg.get()
        d=self.gst.get()
        if a=="" or b=="" or c=="" or d=="" or self.email.get()=="" or self.Nationality.get()=="" or self.mode.get()=="":
            messagebox.showinfo("Warning","Each Field Should Required")
        else:
            try:
                a=int(a)
                b=int(b)
                c=int(c)
                self.total=(a*b+c)
                d=int(d)
                self.total=self.total*d/100 +self.total
                totalE=Label(self.window,font=("times new roman",21,"bold"),text=self.total)
                totalE.place(x=650,y=500)
                Bill.configure(state=NORMAL)
                return self.total
            except:
                self.Clear()
                messagebox.showinfo("Warning","Required Field Value should be in Numeric",parent=self.window)

    def Receipt(self):
        conn=mysql.connector.connect(user="root",host="localhost",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from temporaryroomnumberdeallocation")
        for i in my_cursor:
            print("Roomcode",i[0])
        my_cursor.execute("select COUNT(*) from customerhistory")
        for j in my_cursor:
            print("No. of record in db:",j[0])
        my_cursor.execute("select * from customerhistory where Roomcode={} and CustomerRef={}".format(i[0],j[0]))
        for k in my_cursor:
            print(k)
        Name=self.FileNaming()

        current=datetime.datetime.now()
        dates="{}-{}-{}".format(current.year,current.month,current.day)
        
        email=self.email.get()
        date=dates
        days=self.days.get()
        roomtype=self.roomtype.get()
        price=self.price.get()
        gst=self.gst.get()
        chrg=self.chg.get()
        mode=self.mode.get()
        total=round(self.Total())

        a="-"
        b=" "

        #length
        Rclen=len(str(k[0]))
        i1=b*(47-Rclen)
        Nmlen=len(k[1])
        i2=b*(53-Nmlen)
        Phlen=len(k[2])
        i3=b*(48-Phlen)
        Emlen=len(email)
        i4=b*(52-Emlen)
        Adlen=len(k[3])
        i5=b*(50-Adlen)
        Dtlen=len(date)
        i6=b*(53-Dtlen)
        Inlen=len(k[7])
        i7=b*(49-Inlen)
        Otlen=len(k[8])
        i8=b*(48-Otlen)
        Ndlen=len(days)
        i9=b*(47-Ndlen)
        Rtlen=len(roomtype)
        i10=b*(48-Rtlen)
        Rnlen=len(str(k[6]))
        i11=b*(46-Rnlen)
        Pclen=len(price)
        i12=b*(44-Pclen)
        Gtlen=len(gst)
        i13=b*(51-Gtlen)
        Cglen=len(chrg)
        i14=b*(34-Cglen)
        Mdlen=len(mode)
        i15=b*(45-Mdlen)
        Ttlen=len(str(total))
        i16=b*(52-Ttlen)
        
        f=open(f"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\HotelBillFolder\{Name}","a")
        heading="""
                |**************************************************************|
                |                           V & V                              |
                |                    Hotel and Restorant                       |
                |         Ghansoli Navi Mumbai ,Near Dmart Chinchali           |
                |                    Shop no.406 -400701                       |
                |     Phone No.:8451096034  GSTIN:-ASDFEX88897FNDUDJG3F        |
                |   Invoice No.:123454645DFD     Invoice Date:-12/12/2012      |
                |**************************************************************|
                |                                                              |
                |BILL TO:-                                                     |
                |                                                              |
                |   RECEIPT NO:-{}{}|
                |                                                              |
                |   NAME:-{}{}|
                |                                                              |
                |   PHONE NO.:-{}{}|
                |                                                              |
                |   EMAIL:-{}{}|
                |                                                              |
                |   ADDRESS:-{}{}|
                |                                                              |
                |   DATE:-{}{}|
                |                                                              |
                |   CHECK IN:-{}{}|
                |                                                              |
                |   CHECK OUT:-{}{}|
                |                                                              |
                |   NO.OF DAYS:-{}{}|
                |                                                              |
                |   ROOM TYPE:-{}{}|
                |                                                              |
                |   ROOM NUMBER:-{}{}|
                |                                                              |
                |   PRICE PER DAY:-{}{}|
                |                                                              |
                |   GST(%):-{}{}|
                |                                                              | 
                |   Premium Service Charges:-{}{}|  
                |                                                              | 
                |   PAYMENT MODE:-{}{}|
                |                                                              |
                |   TOTAL:-{}{}|
                |                                                              |
                |                                                              |
                |                                                              |
                |                                                              |
                |  Cashier SIGN                               Customer SIGN    |
                |                                                              |
                |                                                              |
                |                !!!THANK YOU VISIT AGAIN!!!                   |
                |**************************************************************|
                |----------------------------END-------------------------------|
                |**************************************************************|""".format(k[0],i1,k[1],i2,k[2],i3,email,i4,k[3],i5,date,i6,k[7],i7,k[8],i8,days,i9,roomtype,i10,k[6],i11,price,i12,gst,i13,chrg,i14,mode,i15,total,i16)
        f.write(heading)
        #conn=mysql.connector.connect(user="root",host="localhost",password="vicky@123//",database="hotelandrestoproject")
        #my_cursor=conn.cursor()
        #my_cursor.execute("delete from temporaryroomnumberdeallocation")
        #conn.commit()
        #conn.close()

        #print(heading)
        #time.sleep(1)
        self.billrecord(self.FileNaming(),total,dates)
        messagebox.showinfo("Warning","Receipt Generated Successfully",parent=self.window)
        self.Destroy()

    def FileNaming(self):
        current_time=datetime.datetime.now()
        print("year:",current_time.year,"\nMonth:",current_time.month,"\nDate:",current_time.day,"\nHour:",current_time.hour,"\nMinutes:",current_time.minute,"\nsecond:",current_time.second,"\nMicrosecond:",current_time.microsecond)
        Name="HotelBill"+str(current_time.year)+str(current_time.month)+str(current_time.day)+str(current_time.hour)+str(current_time.minute)+str(current_time.second)+str(current_time.microsecond)+".txt"
        print(Name)
        return Name

    def customerdetail(self):
        conn=mysql.connector.connect(user="root",host="localhost",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from temporaryroomnumberdeallocation")
        for i in my_cursor:
            print("Roomcode",i[0])
        my_cursor.execute("select COUNT(*) from customerhistory")
        for j in my_cursor:
            print("No. of record in db:",j[0])
        my_cursor.execute("select * from customerhistory where Roomcode={} and CustomerRef={}".format(i[0],j[0]))
        for k in my_cursor:
            print(k)
        return k

    def billrecord(self,Name,amount,datetime):
        conn=mysql.connector.connect(user="root",host="localhost",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select COUNT(*) from hotelbillrecord")
        for i in my_cursor:
            print(i[0])
        my_cursor.execute("INSERT into hotelbillrecord values(%s,%s,%s,%s)",(
                                                                             i[0]+1,
                                                                             Name,
                                                                             amount,
                                                                             datetime
                                                                             ))
        conn.commit()
        conn.close()

    def Clear(self):
        self.days.set("")
        self.price.set("")
        self.chg.set("")
        self.gst.set("")
        

    def Destroy(self):
        time.sleep(1)
        self.window.destroy()

        



if __name__=="__main__":
    window=Tk()
    obj=HotelBillGeneration(window)
    window.mainloop()
