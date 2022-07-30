"""
Hello for evey one :) ... 
I wanna share with u this amazing drawing 
'circle art' with turtle lib ...
Try it yourself in your python IDE and 
tell us what you think. If you enjoyed it,
don't forget to share repo with your friends
 please ;)
"""

# insta : @_moha_wb


import turtle

#background
wn=turtle.Screen()
wn.bgcolor("#ffdd9a") 

#editing pen of drawing
t=turtle.Pen()
t.speed(0)
t.color("#0e1e52")
t.width(3)

#starting drawing
for i in range(18):
	t.left(20)
	for j in range(50,60,2):
		t.circle(j*2)

turtle.mainloop()   
