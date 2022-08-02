import turtle
turtle.bgcolor("#ffdd9a")
t=turtle.Pen()
t.width(1)
t.speed(0)
for i in range(106):
	if i%2==0:
		t.color("#0e1e52")
		t.width(3)
	else:
		t.color("#0e1e52")
	t.left(109)
	t.forward(i*3)
turtle.mainloop()