import tkinter
from random import*
import random
canvas = tkinter.Canvas(height=500,width=1000,bg='white')
canvas.pack()

#zmrzlina
'''
canvas.create_oval(100,32,120,52,fill='red') #cerveny kopcek
canvas.create_oval(95,40,115,60,fill='yellow') #zlty kopcek
canvas.create_oval(105,40,125,60,fill='green') #zeleny kopcek
canvas.create_rectangle(95,52,125,62,fill='white') #biely obdlznik
canvas.create_line(95,62,110,102,125,62) #kornutok
'''

#strom s ceresnou
'''
def strom():
    canvas.create_rectangle(110,100,135,200,fill='black')
    canvas.create_oval(75,25,175,125,fill='green')
    canvas.create_oval(150,80,165,95,fill='red')
    canvas.create_oval(130,80,145,95,fill='red')
    canvas.create_line(137,80,147.5,65,157,80,width=3)
strom()
'''

#uloha3
'''
def balon():
    canvas.create_oval(75,75,125,125,fill='blue')
    canvas.create_line(75,100,100,170,125,100,width=2)
    canvas.create_rectangle(85,170,115,185,fill='red')
balon()
'''

#ciarovy kod
'''
def ciar_kod():
    x = 50
    y = 30
    for i in range(20):
        hrubka = randrange(1,9)
        canvas.create_line(x,y,x,y+200,width=hrubka)
        x+=10
        print('Hrubka ciary ', i+1,' je ', hrubka)
ciar_kod()
'''

#uloha 5 2 obrazky
'''
#obrazok1
x=0
for i in range(2):
    canvas.create_line(x+10,50,60,10)
    x+=100
canvas.create_rectangle(10,50,110,150,fill='green')
canvas.create_rectangle(30,60,50,80,fill='blue')
canvas.create_rectangle(70,60,90,80,fill='blue')
canvas.create_rectangle(30,90,50,110,fill='blue')
canvas.create_rectangle(70,90,90,110,fill='blue')
canvas.create_rectangle(43,120,77,150,fill='black')
canvas.create_rectangle(110,100,250,150,fill='orange')
canvas.create_rectangle(130,110,150,130,fill='blue')
canvas.create_rectangle(170,110,190,130,fill='blue')
canvas.create_rectangle(220,120,240,150,fill='black')
y=0
for i in range(2):
    canvas.create_oval(y+260,50,y+310,100,fill='darkgreen')
    canvas.create_line(y+285,100,y+285,150,fill='brown',width=5)
    y+=60
#obrazok5
canvas.create_rectangle(0,200,500,400,fill='skyblue',outline='')
canvas.create_oval(200,230,470,500,fill='yellow')
canvas.create_rectangle(0,400,500,500,fill='lightgreen',outline='')
canvas.create_rectangle(0,400,500,400)
canvas.create_rectangle(30,390,80,460,fill='brown')
canvas.create_oval(10,300,110,400,fill='darkgreen')
canvas.create_oval(130,333,160,360,fill='black')
canvas.create_line(145,360,145,410,fill='black',width=5)
canvas.create_line(125,370,165,370,fill='black',width=5)
canvas.create_line(145,410,120,430,fill='black',width=5)
canvas.create_line(145,410,170,430,fill='black',width=5)
'''

#uloha 6
'''
#a
x=0
y=0
for i in range(8):
    canvas.create_oval(x+70,10,x+100,40,fill=random.choice(('yellow','green','blue','pink','red','lightblue','purple','darkgreen')))
    x+=25
    canvas.create_line(y+85,40,170,90)
    y+=25
#b
x=0
y=0
for i in range(8):
    canvas.create_oval(x+70,90,x+100,110,fill=random.choice(('yellow','green','blue','pink','red','lightblue','purple','darkgreen')))
    x+=25
    canvas.create_line(y+85,90,170,50)
    y+=25
'''

#uloha 7
'''
#prvyobrazok
for i in range(100):
    canvas.create_line(10,random.randrange(300),310,random.randrange(300),width=random.randrange(5),fill=random.choice(("yellow","blue","green","pink","red","purple")))
'''
'''
#druhyobrazok
for i in range(100):
    canvas.create_line(random.randrange(300),0,random.randrange(300),500,width=random.randrange(5),fill=random.choice(("yellow","blue","green","pink","red","purple")))
'''
'''
#tretiobrazok
for i in range(100):
    canvas.create_line(150, 150,random.randrange(500),random.randrange(500),width=random.randrange(5),fill=random.choice(("yellow","blue","green","pink","red","purple")))
'''    
#uloha 8
'''
x=800
y=random.randint(0,150)
y1=random.randint(250,400)
def mesiac(x,y):
    canvas.create_oval(x,y,x+100,y+100,fill="yellow",outline="")
    canvas.create_oval(x+35,y,x+100,y+100,fill="white",outline="")
def odrazmesiaca(x,y):
    canvas.create_oval(x,y,x+100,y+100,fill="yellow",outline="")
    canvas.create_oval(x+35,y,x+100,y+100,fill="darkblue",outline="")

canvas.create_oval(20,200,220,400,fill="brown",outline="")
canvas.create_rectangle(0,250,1001,501,fill="darkblue")
canvas.create_line(120,200,120,25,fill="black",width=5)
canvas.create_rectangle(120,25,300,125,fill="lime",outline="black",width=5)
canvas.create_oval(185,45,235,100,fill="yellow",outline="")
canvas.create_oval(202,45,240,100,fill="lime",outline="")
canvas.create_line(250,200,500,200,450,260,300,260,250,200,width=5)
canvas.create_line(375,200,375,75,410,150,375,170,width=5)
mesiac(x,y)
odrazmesiaca(x,y1)
'''

#uloha 9
'''
x=0
for i in range(2):
    canvas.create_line(10+x,150,50+x,250)
    x=x+30
y=0
x=0
for i in range(19):
    canvas.create_line(5+x,155+y,55+x,155+y)
    y=y+5
    x=x+2
    

for i in range(2):
    canvas.create_line(45+x,250,100+x,150)
    x=x+30
y=0
x=0
for i in range(19):
    canvas.create_line(125-x,155+y,175-x,155+y)
    y=y+5
    x=x+3
'''

#uloha 10
#a
'''
x = 10
for i in range(20):
    canvas.create_line(x,50,500,450,width=3)
    x+=50
'''
#b
'''
x = 10
for i in range(20):
    canvas.create_line(10,10,x,500,width=3,fill='green')
    x+=50
'''
#c
'''
x = 10
for i in range(20):
    canvas.create_line(x,0,990,490,width=3,fill='blue')
    x+=50
'''

#uloha 11
'''
for i in range(20):
    polomer = randrange(50,100)
    x = randrange(150,850)
    farba = random.choice(('yellow','green','blue','pink','red','lightblue','purple','darkgreen'))
    canvas.create_oval(x-polomer,250-polomer,x+polomer,250+polomer,fill='',width=3,outline=farba)
'''

#uloha 12
'''
for i in range(1,1000,10):
    if i < 500:
        canvas.create_line(0,i,1000,i)
    canvas.create_line(i,0,i,500)
'''

#ulohy 13 a 14
'''
for i in range(1,1001):
    y=randrange(10,40)
    canvas.create_line(i,0,i,y,fill='green')
    canvas.create_line(i,500,i,500-y,fill='green')
N_pocet=randrange(1,20)
def mlaka():
    for j in range(1,N_pocet):
        x=randrange(20,80)
        x1=randrange(20,980)
        y1=randrange(152,350)
        canvas.create_oval(x1-x,y1-x,x1+x,y1+x,fill='blue',outline='blue')
mlaka()
Yr=randrange(45,200)
canvas.create_line(0,Yr,1000,Yr,fill='brown',width=4)
canvas.create_line(0,Yr+50,1000,Yr+50,fill='brown',width=4)
for i1 in range(1,1001, 100):
    canvas.create_line(i1,Yr,i1,Yr+50,fill='brown',width=4)
'''

#ulohy 15 az 19
'''
x=10
y=10
def muchotravka():
    canvas.create_oval(100, 300, 180, 380, fill="red", outline="")
    canvas.create_rectangle(0, 330, 200, 400, fill="white", outline="")
    canvas.create_rectangle(130, 330, 150, 410, fill="brown", outline="")
    canvas.create_oval(130, 400, 150, 420, fill="brown", outline="")
    canvas.create_oval(125, 305, 130,310, fill="white", outline="red")
    canvas.create_oval(110, 320, 115, 325,fill="white", outline="red")
    canvas.create_oval(135, 320, 140, 325, fill="white", outline="red")
    canvas.create_oval(150, 310, 160, 320, fill="white", outline="red")
def trava():
    canvas.create_rectangle(0,480,1000,500,fill='green',outline='')
    for i in range(100):
        canvas.create_line(i*10,460,i*10,500,fill='green',width=2)
def slnko():
    for i in range(40):
        canvas.create_line(0,0,randrange(200),randrange(200),fill='yellow',width=3)

def mlaka():
    global x,y
    for i in range(20):
        canvas.create_oval(700-x,330-y,700+x,330+y, outline='blue')
        x+=5
        y+=5
    
def pozemky():
    x=700
    y=0
    for i in range(3):
           y+=55
           x=700
           for j in range(5):
                a=random.randrange(50)
                canvas.create_rectangle(x,y,x+a,y+a)
                x+=50
muchotravka()
trava()
slnko()
pozemky()
mlaka()
'''
