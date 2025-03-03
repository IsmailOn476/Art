from turtle import *


t= Turtle()
t.shape('turtle')
t.color('#075487')
t.speed(0)
bgcolor('black')

t.pu()
t.rt(90)
t.fd(100)
t.pd()
t.lt(90)

#pixel

def p(c):
    t.color(c)
    t.begin_fill()
    for i in range(4):
        t.fd(10)
        t.lt(90)
    t.fd(10)
    t.end_fill()

w= '#d6d6d6'
b= '#075487'
lb= '#91dad9'
tl= '#30b186'
dg= '#207738'
lg='#63c42f'
dlg='#37a334'
s= '#4875c4'

#Earth Globe

#first line
p('#075487')

p('#075487')
for count in range(3):
    p('#d6d6d6')
p('#075487')

#second line
t.pu()
t.bk(60)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(-20)
t.pd()

for i in range(2):
    p('#075487')

p('#d6d6d6')

for i in range(2):
    p('#075487')
    
for i in range(3):
    p('#30b186')
p(dg)
p(dg)
    

#third line
t.pu()
t.bk(100)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(-20)
t.pd()

for i in range(8):
    p('#075487')
    
p(tl)
for i in range(2):
    p('#207738')
    
p(w)
p(dg)
p(dg)

#line 4
t.pu()
t.bk(140)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(-10)
t.pd()

for i in range(10):
    p(b)
for i in range(3):
    p(dg)
p(w)
p(dg)
p(dg)

#line 5
t.pu()
t.bk(160)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(-10)
t.pd()

for i in range(4):
    p(b)
for i in range(4):
    p(lb)
p(b)
p(b)
p(lg)
p(lg)
for i in range(4):
    p(dlg)
p(dg)
p(dg)

#line 6
t.pu()
t.bk(180)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(-10)
t.pd()

for i in range(4):
    p(b)
for i in range(5):
    p(w)
p(lb)
p(s)
for i in range(4):
    p(lg)
p(dlg)
for i in range(4):
    p(dlg)


done()