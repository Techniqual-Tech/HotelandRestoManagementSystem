from tkinter import *

class HelpA:
    def __init__(self,window):
        self.window=window
        self.window.title("Help")
        self.window.geometry("1280x725+0+0")
        #self.window.configure(bg="#e8e7dc")

        Headinglabel=Label(self.window,text="May i Help You?",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)

        label=Label(self.window,text="# This Section Defines Authorization Of Staff's.",font=("times new roman",18,"bold"))
        label.place(x=15,y=60)

        label=Label(self.window,text="# Here We Can Create The UserName And Password .",font=("times new roman",18,"bold"))
        label.place(x=15,y=100)

        label=Label(self.window,text="# Security Question Helpful During Username Deletion and Forgot Password.",font=("times new roman",18,"bold"))
        label.place(x=15,y=140)

        label=Label(self.window,text="# Username We Can Remove By Entering Username,Password and Security Answer.",font=("times new roman",18,"bold"))
        label.place(x=15,y=180)

        label=Label(self.window,text="# Each Activity Carries Under The Present of Higher Authorities.",font=("times new roman",18,"bold"))
        label.place(x=15,y=220)

        label=Label(self.window,text="# Created Username And Password We Can use to Login this Hotel and Restorant Portal .",font=("times new roman",18,"bold"))
        label.place(x=15,y=260)

        



if __name__=="__main__":
    window=Tk()
    obj=HelpA(window)
    window.mainloop()
