from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import datetime
from HotelBillGeneration import HotelBillGeneration
class Deallocation:
    def __init__(self,window):
        self.window=window
        self.window.title("RoomDeallocate")
        self.window.geometry("849x600+0+0")
        self.window.configure(bg="black")

        data=self.FetchAllotedData()
        print("data",data[0])
        #variable declaration
        self.Cref=StringVar()
        self.CName=StringVar()
        self.CMobile=StringVar()
        self.CRoomCode=StringVar()
        self.CRoomType=StringVar()
        self.CSecDep=StringVar()
        self.CRemark=StringVar()
        self.CInTime=StringVar()
        self.COutTime=StringVar()

        Headinglabel=Label(self.window,text="Deallocation",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=56)
        Headinglabel.place(x=0,y=0)

        self.MainFrame=Frame(self.window,bg="white",width="849",height="550",bd=2,relief=RIDGE)
        self.MainFrame.place(x=0,y=40)

        Cref=Label(self.window,text="Customer Ref:-",font=("times new roman",19,"bold"),bg="white")
        Cref.place(x=30,y=80)


        CrefE=Entry(self.window,font=("times new roman",16,"bold"),relief=RIDGE,bd=2,bg="white",width=30,textvariable=self.Cref)
        CrefE.place(x=225,y=85)
        CrefE.insert(0,data[0])
        CrefE.configure(state=DISABLED)

        CustomerName=Label(self.window,text="Customer Name:-",font=("times new roman",19,"bold"),bg="white")
        CustomerName.place(x=30,y=130)

        CustomerNameE=Entry(self.window,font=("times new roman",16,"bold"),relief=RIDGE,bd=2,bg="white",width=30,textvariable=self.CName)
        CustomerNameE.place(x=225,y=135)
        CustomerNameE.insert(0,data[1])
        CustomerNameE.configure(state=DISABLED)

        Mobile=Label(self.window,text="Mobile No.:-",font=("times new roman",19,"bold"),bg="white")
        Mobile.place(x=30,y=180)

        MobileE=Entry(self.window,font=("times new roman",16,"bold"),relief=RIDGE,bd=2,bg="white",width=30,textvariable=self.CMobile)
        MobileE.place(x=225,y=185)
        MobileE.insert(0,data[2])
        MobileE.configure(state=DISABLED)

        Roomcode=Label(self.window,text="Room Code:-",font=("times new roman",19,"bold"),bg="white")
        Roomcode.place(x=30,y=230)

        RoomcodeE=Entry(self.window,font=("times new roman",16,"bold"),relief=RIDGE,bd=2,bg="white",width=30,textvariable=self.CRoomCode)
        RoomcodeE.place(x=225,y=235)
        RoomcodeE.insert(0,data[3])
        RoomcodeE.configure(state=DISABLED)

        RoomType=Label(self.window,text="Room Type:-",font=("times new roman",19,"bold"),bg="white")
        RoomType.place(x=30,y=280)

        RoomTypeE=Entry(self.window,font=("times new roman",16,"bold"),relief=RIDGE,bd=2,bg="white",width=30,textvariable=self.CRoomType)
        RoomTypeE.place(x=225,y=285)
        RoomTypeE.insert(0,data[4])
        RoomTypeE.configure(state=DISABLED)

        SecDep=Label(self.window,text="Security Deposite:-",font=("times new roman",17,"bold"),bg="white")
        SecDep.place(x=30,y=330)

        SecDepE=Entry(self.window,font=("times new roman",16,"bold"),relief=RIDGE,bd=2,bg="white",width=30,textvariable=self.CSecDep)
        SecDepE.place(x=225,y=335)
        SecDepE.insert(0,data[5])
        SecDepE.configure(state=DISABLED)

        Remark=Label(self.window,text="Remark:-",font=("times new roman",19,"bold"),bg="white")
        Remark.place(x=30,y=380)

        RemarkE=Entry(self.window,font=("times new roman",16,"bold"),relief=RIDGE,bd=2,bg="white",width=30,textvariable=self.CRemark)
        RemarkE.place(x=225,y=385)
        RemarkE.insert(0,data[6])
        RemarkE.configure(state=DISABLED)

        InTime=Label(self.window,text="In DateTime:-",font=("times new roman",19,"bold"),bg="white")
        InTime.place(x=30,y=430)

        InTimeE=Entry(self.window,font=("times new roman",16,"bold"),relief=RIDGE,bd=2,bg="white",width=30,textvariable=self.CInTime)
        InTimeE.place(x=225,y=435)
        InTimeE.insert(0,data[7])
        InTimeE.configure(state=DISABLED)

        OutTime=Label(self.window,text="Out DateTime:-",font=("times new roman",19,"bold"),bg="white")
        OutTime.place(x=30,y=480)

        current=datetime.datetime.now()
        OutTimeE=Entry(self.window,font=("times new roman",16,"bold"),relief=RIDGE,bd=2,bg="white",width=30,textvariable=self.COutTime)
        OutTimeE.place(x=225,y=485)
        OutTimeE.insert(0,current)
        OutTimeE.configure(state=DISABLED)

        Key=Image.open(r"D:\Vicky_All_Program\python\Hotel&RestorantManagementSystem\ReturnKey.png")
        Key=Key.resize((490,490))
        self.photoimgcr=ImageTk.PhotoImage(Key)
        KeyLabel=Label(self.MainFrame,image=self.photoimgcr,bd=0,relief=RIDGE,bg="white")
        KeyLabel.place(x=600,y=100,width=200,height=350)

        returnlabel=Label(self.MainFrame,text="Return",font=("Cooper black",30,"bold"),bg="white",fg="#fcdf03")
        returnlabel.place(x=620,y=55)

        global Dallocate
        Dallocate=Button(self.MainFrame,text="Deallocate",font=("times new roman",16,"bold"),bg="black",fg="yellow",command=lambda:self.Deallocation(current,data[0]))
        Dallocate.place(x=260,y=500)

        cancelDallo=Button(self.MainFrame,text="Cancel",font=("times new roman",16,"bold"),bg="black",fg="yellow",width=9,command=lambda:self.Destroy())
        cancelDallo.place(x=400,y=500)

    def FetchAllotedData(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from temporaryroomnumberdeallocation")
        for i in my_cursor:
            print(i[0])
        my_cursor.execute("select * from allocatedroomdetails where RoomCode={}".format(i[0]))
        for j in my_cursor:#NO DATA ASSOCIATED WITH J IS NORMAL NOT CONSIDR ERROR BCOZ THIS PAGE WILL ONLY OPEN AFTER ALLOCATION.
            print(j[0],j[1],j[4],j[14],j[12],j[15],j[16],j[17],j[18])
            
        return j[0],j[1],j[4],j[14],j[12],j[15],j[16],j[17],j[18]

    def Deallocation(self,current,Cref):
        conn=mysql.connector.connect(host="localhost",user="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE customerhistory SET OutDateTime='{}' Where CustomerRef='{}'".format(current,Cref))
        my_cursor.execute("delete from allocatedroomdetails where CustomerRef='{}'".format(Cref))
        conn.commit()
        conn.close()
        Dallocate.configure(state=DISABLED)
        self.new_window=Toplevel(self.window)
        self.app=HotelBillGeneration(self.new_window)
        #self.Destroy()

    def Destroy(self):
        self.window.destroy()
        
        



        

        



if __name__=="__main__":
    window=Tk()
    obj=Deallocation(window)
    window.mainloop()
