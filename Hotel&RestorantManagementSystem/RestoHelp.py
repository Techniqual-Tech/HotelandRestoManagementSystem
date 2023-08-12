from tkinter import *

class HelpR:
    def __init__(self,window):
        self.window=window
        self.window.title("Help")
        self.window.geometry("1280x725+0+0")
        #self.window.configure(bg="#e8e7dc")

        Headinglabel=Label(self.window,text="May i Help You?",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)

        label=Label(self.window,text="# This Section Defines Things Related To Restorant Section.",font=("times new roman",18,"bold"))
        label.place(x=15,y=60)

        label=Label(self.window,text="# This Section Basicalling Consist Of Item's Entry And Bill Generation .",font=("times new roman",18,"bold"))
        label.place(x=15,y=100)

        label=Label(self.window,text="# In Item's Entry We Can Enter Item Along With It's Price.",font=("times new roman",18,"bold"))
        label.place(x=15,y=140)

        label=Label(self.window,text="# We Also Able to Update The Item's Price and Remove Item's From the List.",font=("times new roman",18,"bold"))
        label.place(x=15,y=180)

        label=Label(self.window,text="# In Bill Section We Just Have to Click on List Item It will Automaticalling Get Added Into The Bill list.",font=("times new roman",18,"bold"))
        label.place(x=15,y=220)

        label=Label(self.window,text="# During Bill First Time Only We Have To Provide The GST After That Gst Entry Field Get Disabled .",font=("times new roman",18,"bold"))
        label.place(x=15,y=260)

        label=Label(self.window,text="# And Every Time We Have to Pick Item From List And Provide The Quantity Only.",font=("times new roman",18,"bold"))
        label.place(x=15,y=300)

        label=Label(self.window,text="# We Can Update Or Delete Item From The Bill List.",font=("times new roman",18,"bold"))
        label.place(x=15,y=340)

        label=Label(self.window,text="# Then Click Calculate Then  Bill .",font=("times new roman",18,"bold"))
        label.place(x=15,y=380)

        label=Label(self.window,text="# Bill Generated In Form Of .txt File Which We Can Print and Gives To Customer.",font=("times new roman",18,"bold"))
        label.place(x=15,y=420)

        label=Label(self.window,text="# We Can Also Check The Bill History Along Bill,Amount and Dates.",font=("times new roman",18,"bold"))
        label.place(x=15,y=460)

        



if __name__=="__main__":
    window=Tk()
    obj=HelpR(window)
    window.mainloop()
