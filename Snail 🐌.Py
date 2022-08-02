import turtle
wn=turtle.Screen()
wn.bgcolor("#FFFFFF")
t=turtle.Pen()
t.pu()
t.speed(0)
t.pd()
t.color("#666f88")
t.width(3)
for i in range(40):
	t.left(20)
	t.circle(i*2)
turtle.mainloop()   