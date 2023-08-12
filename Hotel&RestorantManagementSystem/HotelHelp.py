from tkinter import *

class HelpH:
    def __init__(self,window):
        self.window=window
        self.window.title("Help")
        self.window.geometry("1280x725+0+0")
        #self.window.configure(bg="#e8e7dc")

        Headinglabel=Label(self.window,text="May i Help You?",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)

        label=Label(self.window,text="# This Section Defines Things Related To Hotel Section.",font=("times new roman",18,"bold"))
        label.place(x=15,y=60)

        label=Label(self.window,text="# This Section Basicalling Consist Of RoomStatus,BillGeneration,CustomerDetails,RecentBill,CustomerHistory,BillHistory .",font=("times new roman",17,"bold"))
        label.place(x=15,y=100)

        label=Label(self.window,text="# RoomStatus Show The Availablity Of Room In Which Floor And What Kind.",font=("times new roman",18,"bold"))
        label.place(x=15,y=140)

        label=Label(self.window,text="# Green Show Avaiable And Red Show Unavaiable.",font=("times new roman",18,"bold"))
        label.place(x=15,y=180)

        label=Label(self.window,text="# Clicking On Green We Can Allocate The Room To Someone And Red To Deallocate.",font=("times new roman",18,"bold"))
        label.place(x=15,y=220)

        label=Label(self.window,text="# Deallocation Cause Bill Generation Along With It .",font=("times new roman",18,"bold"))
        label.place(x=15,y=260)

        label=Label(self.window,text="# If ByMistakely BillGeneration Cancell For That We Have Provided One Separate Section RecentBill To Bill Again.",font=("times new roman",17,"bold"))
        label.place(x=15,y=300)

        label=Label(self.window,text="# CustomerDetails Section Shows The Whole Information About The RoomAlloted Customer.",font=("times new roman",18,"bold"))
        label.place(x=15,y=340)

        label=Label(self.window,text="# CustomerHistory Show Only Relevant Information About The Past Customers .",font=("times new roman",18,"bold"))
        label.place(x=15,y=380)

        label=Label(self.window,text="# BillHistory Shows Only The Bill,Amount and Date of Generation.",font=("times new roman",18,"bold"))
        label.place(x=15,y=420)

        label=Label(self.window,text="# This Five Section Actully Consist Of Some More Section Which We Come To Know Only When We Enter To Any Section.",font=("times new roman",17,"bold"))
        label.place(x=15,y=460)

        



if __name__=="__main__":
    window=Tk()
    obj=HelpH(window)
    window.mainloop()
