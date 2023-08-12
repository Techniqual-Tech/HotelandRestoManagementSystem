from tkinter import *
from RoomAllocate import RoomAllocation
from RoomDeallocate import Deallocation
import mysql.connector
import time

class RoomAllotmentStatus:
    def __init__(self,window):
        self.window=window
        self.window.title("Room Status")
        self.window.geometry("1280x725+0+0")
        self.window.configure(bg="#99bdf7")

        Headinglabel=Label(self.window,text="Room-Status",font=("times new roman",19,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=85)
        Headinglabel.place(x=0,y=0)

        #Floor lables
        self.FloorLabel(1,50)
        self.FloorLabel(2,120)
        self.FloorLabel(3,190)
        self.FloorLabel(4,260)
        self.FloorLabel(5,330)
        self.FloorLabel(6,400)
        self.FloorLabel(7,470)
        self.FloorLabel(8,540)
        self.FloorLabel(9,610)


        #global
        global button101,button102,button103,button104,button105,button106,button107,button108,button109,button110,button111
        global button201,button202,button203,button204,button205,button206,button207,button208,button209,button210,button211
        global button301,button302,button303,button304,button305,button306,button307,button308,button309,button310,button311
        global button401,button402,button403,button404,button405,button406,button407,button408,button409,button410,button411
        global button501,button502,button503,button504,button505,button506,button507,button508,button509,button510,button511
        global button601,button602,button603,button604,button605,button606,button607,button608,button609,button610,button611
        global button701,button702,button703,button704,button705,button706,button707,button708,button709,button710,button711
        global button801,button802,button803,button804,button805,button806,button807,button808,button809,button810,button811
        global button901,button902,button903,button904,button905,button906,button907,button908,button909,button910,button911

        #Floortype Button
        #for First floor
        button101=Button(self.window,text="101/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(101,1,"1RK",1),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button101.place(x=130,y=57)

        button102=Button(self.window,text="102/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(102,1,"1RK",2),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button102.place(x=230,y=57)

        button103=Button(self.window,text="103/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(103,1,"1RK",3),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button103.place(x=330,y=57)

        button104=Button(self.window,text="104/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(104,1,"1RK",4),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button104.place(x=430,y=57)

        dashlabel=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel.place(x=525,y=62)

        button105=Button(self.window,text="105/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(105,1,"1BHK",5),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button105.place(x=545,y=57)

        button106=Button(self.window,text="106/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(106,1,"1BHK",6),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button106.place(x=645,y=57)

        button107=Button(self.window,text="107/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(107,1,"1BHK",7),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button107.place(x=745,y=57)

        button108=Button(self.window,text="108/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(108,1,"1BHK",8),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button108.place(x=845,y=57)

        dashlabel1=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel1.place(x=940,y=62)

        button109=Button(self.window,text="109/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(109,1,"2BHK",9),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button109.place(x=960,y=57)

        button110=Button(self.window,text="110/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(110,1,"2BHK",10),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button110.place(x=1060,y=57)

        dashlabel2=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel2.place(x=1155,y=62)

        button111=Button(self.window,text="111/3BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(111,1,"3BHK",11),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button111.place(x=1175,y=57)

        #for Second floor
        button201=Button(self.window,text="201/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(201,2,"1RK",1),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button201.place(x=130,y=125)

        button202=Button(self.window,text="202/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(202,2,"1RK",2),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button202.place(x=230,y=125)

        button203=Button(self.window,text="203/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(203,2,"1RK",3),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button203.place(x=330,y=125)

        button204=Button(self.window,text="204/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(204,2,"1RK",4),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button204.place(x=430,y=125)

        dashlabel21=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel21.place(x=525,y=130)

        button205=Button(self.window,text="205/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(205,2,"1BHK",5),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button205.place(x=545,y=125)

        button206=Button(self.window,text="206/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(206,2,"1BHK",6),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button206.place(x=645,y=125)

        button207=Button(self.window,text="207/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(207,2,"1BHK",7),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button207.place(x=745,y=125)

        button208=Button(self.window,text="208/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(208,2,"1BHK",8),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button208.place(x=845,y=125)

        dashlabel22=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel22.place(x=940,y=130)

        button209=Button(self.window,text="209/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(209,2,"2BHK",9),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button209.place(x=960,y=125)

        button210=Button(self.window,text="210/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(210,2,"2BHK",10),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button210.place(x=1060,y=125)

        dashlabel23=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel23.place(x=1155,y=130)

        button211=Button(self.window,text="211/3BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(211,2,"3BHK",11),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button211.place(x=1175,y=125)

        #for Third floor
        button301=Button(self.window,text="301/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(301,3,"1RK",1),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button301.place(x=130,y=193)

        button302=Button(self.window,text="302/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(302,3,"1RK",2),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button302.place(x=230,y=193)

        button303=Button(self.window,text="303/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(303,3,"1RK",3),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button303.place(x=330,y=193)

        button304=Button(self.window,text="304/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(304,3,"1RK",4),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button304.place(x=430,y=193)

        dashlabel31=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel31.place(x=525,y=198)

        button305=Button(self.window,text="305/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(305,3,"1BHK",5),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button305.place(x=545,y=193)

        button306=Button(self.window,text="306/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(306,3,"1BHK",6),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button306.place(x=645,y=193)

        button307=Button(self.window,text="307/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(307,3,"1BHK",7),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button307.place(x=745,y=193)

        button308=Button(self.window,text="308/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(308,3,"1BHK",8),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button308.place(x=845,y=193)

        dashlabel32=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel32.place(x=940,y=198)

        button309=Button(self.window,text="309/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(309,3,"2BHK",9),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button309.place(x=960,y=193)

        button310=Button(self.window,text="310/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(310,3,"2BHK",10),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button310.place(x=1060,y=193)

        dashlabel33=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel33.place(x=1155,y=198)

        button311=Button(self.window,text="311/3BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(311,3,"3BHK",11),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button311.place(x=1175,y=193)

        #for Fourth floor
        button401=Button(self.window,text="401/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(401,4,"1RK",1),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button401.place(x=130,y=261)

        button402=Button(self.window,text="402/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(402,4,"1RK",2),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button402.place(x=230,y=261)

        button403=Button(self.window,text="403/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(403,4,"1RK",3),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button403.place(x=330,y=261)

        button404=Button(self.window,text="404/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(404,4,"1RK",4),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button404.place(x=430,y=261)

        dashlabel41=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel41.place(x=525,y=266)

        button405=Button(self.window,text="405/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(405,4,"1BHK",5),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button405.place(x=545,y=261)

        button406=Button(self.window,text="406/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(406,4,"1BHK",6),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button406.place(x=645,y=261)

        button407=Button(self.window,text="407/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(407,4,"1BHK",7),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button407.place(x=745,y=261)

        button408=Button(self.window,text="408/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(408,4,"1BHK",8),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button408.place(x=845,y=261)

        dashlabel42=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel42.place(x=940,y=266)

        button409=Button(self.window,text="409/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(409,4,"2BHK",9),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button409.place(x=960,y=261)

        button410=Button(self.window,text="410/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(410,4,"2BHK",10),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button410.place(x=1060,y=261)

        dashlabel43=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel43.place(x=1155,y=266)

        button411=Button(self.window,text="411/3BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(411,4,"3BHK",11),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button411.place(x=1175,y=261)

        #for Fifth floor
        button501=Button(self.window,text="501/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(501,5,"1RK",1),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button501.place(x=130,y=337)

        button502=Button(self.window,text="502/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(502,5,"1RK",2),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button502.place(x=230,y=337)

        button503=Button(self.window,text="503/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(503,5,"1RK",3),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button503.place(x=330,y=337)

        button504=Button(self.window,text="504/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(504,5,"1RK",4),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button504.place(x=430,y=337)

        dashlabel51=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel51.place(x=525,y=342)

        button505=Button(self.window,text="505/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(505,5,"1BHK",5),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button505.place(x=545,y=337)

        button506=Button(self.window,text="506/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(506,5,"1BHK",6),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button506.place(x=645,y=337)

        button507=Button(self.window,text="507/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(507,5,"1BHK",7),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button507.place(x=745,y=337)

        button508=Button(self.window,text="508/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(508,5,"1BHK",8),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button508.place(x=845,y=337)

        dashlabel52=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel52.place(x=940,y=342)

        button509=Button(self.window,text="509/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(509,5,"2BHK",9),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button509.place(x=960,y=337)

        button510=Button(self.window,text="510/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(510,5,"2BHK",10),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button510.place(x=1060,y=337)

        dashlabel53=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel53.place(x=1155,y=342)

        button511=Button(self.window,text="511/3BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(511,5,"3BHK",11),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button511.place(x=1175,y=337)

        #for Sixth floor
        button601=Button(self.window,text="601/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(601,6,"1RK",1),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button601.place(x=130,y=410)

        button602=Button(self.window,text="602/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(602,6,"1RK",2),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button602.place(x=230,y=410)

        button603=Button(self.window,text="603/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(603,6,"1RK",3),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button603.place(x=330,y=410)

        button604=Button(self.window,text="604/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(604,6,"1RK",4),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button604.place(x=430,y=410)

        dashlabel61=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel61.place(x=525,y=415)

        button605=Button(self.window,text="605/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(605,6,"1BHK",5),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button605.place(x=545,y=410)

        button606=Button(self.window,text="606/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(606,6,"1BHK",6),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button606.place(x=645,y=410)

        button607=Button(self.window,text="607/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(607,6,"1BHK",7),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button607.place(x=745,y=410)

        button608=Button(self.window,text="608/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(608,6,"1BHK",8),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button608.place(x=845,y=410)

        dashlabel62=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel62.place(x=940,y=415)

        button609=Button(self.window,text="609/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(609,6,"2BHK",9),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button609.place(x=960,y=410)

        button610=Button(self.window,text="610/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(610,6,"2BHK",10),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button610.place(x=1060,y=410)

        dashlabel63=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel63.place(x=1155,y=415)

        button611=Button(self.window,text="611/3BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(611,6,"3BHK",11),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button611.place(x=1175,y=410)

        #for Seventh floor
        button701=Button(self.window,text="701/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(701,7,"1RK",1),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button701.place(x=130,y=477)

        button702=Button(self.window,text="702/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(702,7,"1RK",2),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button702.place(x=230,y=477)

        button703=Button(self.window,text="703/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(703,7,"1RK",3),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button703.place(x=330,y=477)

        button704=Button(self.window,text="704/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(704,7,"1RK",4),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button704.place(x=430,y=477)

        dashlabel71=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel71.place(x=525,y=482)

        button705=Button(self.window,text="705/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(705,7,"1BHK",5),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button705.place(x=545,y=477)

        button706=Button(self.window,text="706/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(706,7,"1BHK",6),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button706.place(x=645,y=477)

        button707=Button(self.window,text="707/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(707,7,"1BHK",7),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button707.place(x=745,y=477)

        button708=Button(self.window,text="708/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(708,7,"1BHK",8),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button708.place(x=845,y=477)

        dashlabel72=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel72.place(x=940,y=482)

        button709=Button(self.window,text="709/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(709,7,"2BHK",9),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button709.place(x=960,y=477)

        button710=Button(self.window,text="710/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(710,7,"2BHK",10),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button710.place(x=1060,y=477)

        dashlabel73=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel73.place(x=1155,y=482)

        button711=Button(self.window,text="711/3BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(711,7,"3BHK",11),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button711.place(x=1175,y=477)

        #for Eight floor
        button801=Button(self.window,text="801/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(801,8,"1RK",1),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button801.place(x=130,y=547)

        button802=Button(self.window,text="802/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(802,8,"1RK",2),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button802.place(x=230,y=547)

        button803=Button(self.window,text="803/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(803,8,"1RK",3),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button803.place(x=330,y=547)

        button804=Button(self.window,text="804/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(804,8,"1RK",4),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button804.place(x=430,y=547)

        dashlabel81=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel81.place(x=525,y=552)

        button805=Button(self.window,text="805/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(805,8,"1BHK",5),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button805.place(x=545,y=547)

        button806=Button(self.window,text="806/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(806,8,"1BHK",6),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button806.place(x=645,y=547)

        button807=Button(self.window,text="807/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(807,8,"1BHK",7),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button807.place(x=745,y=547)

        button808=Button(self.window,text="808/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(808,8,"1BHK",8),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button808.place(x=845,y=547)

        dashlabel82=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel82.place(x=940,y=552)

        button809=Button(self.window,text="809/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(809,8,"2BHK",9),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button809.place(x=960,y=547)

        button810=Button(self.window,text="810/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(810,8,"2BHK",10),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button810.place(x=1060,y=547)

        dashlabel83=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel83.place(x=1155,y=552)

        button811=Button(self.window,text="811/3BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(811,8,"3BHK",11),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button811.place(x=1175,y=547)

        #for Nine floor
        button901=Button(self.window,text="901/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(901,9,"1RK",1),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button901.place(x=130,y=615)

        button902=Button(self.window,text="902/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(902,9,"1RK",2),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button902.place(x=230,y=615)

        button903=Button(self.window,text="903/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(903,9,"1RK",3),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button903.place(x=330,y=615)

        button904=Button(self.window,text="904/RK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(904,9,"1RK",4),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button904.place(x=430,y=615)

        dashlabel91=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel91.place(x=525,y=620)

        button905=Button(self.window,text="905/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(905,9,"1BHK",5),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button905.place(x=545,y=615)

        button906=Button(self.window,text="906/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(906,9,"1BHK",6),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button906.place(x=645,y=615)

        button907=Button(self.window,text="907/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(907,9,"1BHK",7),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button907.place(x=745,y=615)

        button908=Button(self.window,text="908/1BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(908,9,"1BHK",8),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button908.place(x=845,y=615)

        dashlabel92=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel92.place(x=940,y=620)

        button909=Button(self.window,text="909/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(909,9,"2BHK",9),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button909.place(x=960,y=615)

        button910=Button(self.window,text="910/2BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(910,9,"2BHK",10),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button910.place(x=1060,y=615)

        dashlabel93=Label(self.window,text="--",font=("Sans-serif",15,"bold"),bg="#99bdf7")
        dashlabel93.place(x=1155,y=620)

        button911=Button(self.window,text="911/3BHK",bg="green",bd=2,activebackground="green",command=lambda:self.Room_Allocate(911,9,"3BHK",11),highlightcolor="green",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=7)
        button911.place(x=1175,y=615)

        Update=Button(self.window,text="Update",command=self.changeStatus,bg="black",fg="yellow",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=13)
        Update.place(x=480,y=670)

        Destroy=Button(self.window,text="Back",command=self.Destroy,bg="black",fg="yellow",font=("Sans-serif",15,"bold"),height=1,relief=RIDGE,width=13)
        Destroy.place(x=680,y=670)

        self.changeStatus()

    def FloorLabel(self,floor,yaxis):
        a="Floor-{}".format(floor)
        floorLabel=Label(self.window,text=a,font=("Algerian",18,"bold"),bg="black",fg="white",height=2,bd=2,relief=RIDGE)
        floorLabel.place(x=2,y=yaxis)

    def Room_Allocate(self,RoomCode,FloorNo,RoomType,RoomNo):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("delete from temporaryroomnumberdeallocation")
        conn.commit()
        conn.close()
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select COUNT(*) from allocatedroomdetails" )
        for j in my_cursor:
            print(j[0])
        temp=0
        my_cursor.execute("select * from allocatedroomdetails")
        data=my_cursor.fetchall()#weak reference errror solution
        if data==[]:
            conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
            my_cursor=conn.cursor()
            my_cursor.execute("delete from temporaryroomnumber")
            my_cursor.execute("INSERT into temporaryroomnumber values({},{},'{}',{})".format(RoomCode,FloorNo,RoomType,RoomNo))
            conn.commit()
            conn.close()
            conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from temporaryroomnumber")
            for i in my_cursor: 
                print("data:",i)
        
            print("Your Room Number:",RoomCode)
            self.new_window=Toplevel(self.window)
            self.app=RoomAllocation(self.new_window)
        for i in data:
            print(i[14])
            if (RoomCode==i[14]):
                conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
                my_cursor=conn.cursor()
                #my_cursor.execute("delete from temporaryroomnumberdeallocation")#comment due to receipt page same query going to execute
                my_cursor.execute("INSERT into temporaryroomnumberdeallocation values({},{},'{}',{})".format(RoomCode,FloorNo,RoomType,RoomNo))
                conn.commit()
                conn.close()
                self.new_window=Toplevel(self.window)
                self.app=Deallocation(self.new_window)
            else:
                temp=temp+1
                if (temp==j[0]):
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
                    my_cursor=conn.cursor()
                    my_cursor.execute("delete from temporaryroomnumber")
                    my_cursor.execute("INSERT into temporaryroomnumber values({},{},'{}',{})".format(RoomCode,FloorNo,RoomType,RoomNo))
                    conn.commit()
                    conn.close()
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from temporaryroomnumber")
                    for i in my_cursor:
                        print("data:",i)
        
                    print("Your Room Number:",RoomCode)
                    self.new_window=Toplevel(self.window)
                    self.app=RoomAllocation(self.new_window)

    def changeStatus(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="hotelandrestoproject")
        my_cursor=conn.cursor()
        for i in [100,200,300,400,500,600,700,800,900]:
            for j in [1,2,3,4,5,6,7,8,9,10,11]:
                change="button"+"{}".format(i+j)
                globals()[change].configure(bg="green")
        my_cursor.execute("select * from allocatedroomdetails")
        for i in my_cursor:
            print(i[14])
            change="button"+"{}".format(i[14])
            globals()[change].configure(bg="red")#globals use to convert string into variable


    def Destroy(self):
        self.window.destroy()
        

        



if __name__=="__main__":
    window=Tk()
    obj=RoomAllotmentStatus(window)
    window.mainloop()
