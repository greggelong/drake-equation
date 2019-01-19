import turtle
import random

wn = turtle.Screen()

r_stars = turtle.Turtle()
p_planets = turtle.Turtle()
n_planetwithlife=turtle.Turtle()
l_life=turtle.Turtle()
i_intellegent = turtle.Turtle()
c_communicate = turtle.Turtle()
L_civlength = turtle.Turtle()
N_discoverable = turtle.Turtle()


wn.setworldcoordinates(0,0,1000,1000)
turtle.tracer(1,0) #deflt tracer is (1,10) the second part is animation speed
wn.bgcolor("grey")


r_stars.color("yellow")
p_planets.color("brown")
n_planetwithlife.color("green")
l_life.color("purple")
i_intellegent.color("black")
c_communicate.color("white")
L_civlength.color("red")
N_discoverable.color("white")

N_discoverable.speed(0)
r_stars.pensize(5)
p_planets.pensize(5)
n_planetwithlife.pensize(5)
l_life.pensize(5)
i_intellegent.pensize(5)
c_communicate.pensize(5)
L_civlength.pensize(5)
N_discoverable.pensize(1)

N_discoverable.penup()
N_discoverable.shape("circle")
N_discoverable.ht()


def getRandDrake():
	print("*"*24)
	print("Random numbers for Drake")
	print("*"*24)
	print("(R), the average rate of star formations, in our galaxy is assumed to be 7 per year ")
	r_stars.goto(100,100)
	r_stars.begin_fill()
	r_stars.circle(35)
	r_stars.end_fill()
	
	
	p = random.randint(1,100)
	print("(p), the percentage of formed stars that have planets", str(p)+"%", p/100)
	p_planets.goto(200,200)
	p_planets.begin_fill()
	p_planets.circle(p)
	p_planets.end_fill()
	
	n= random.randint(0,50)
	print("(n)for stars that have planets, the average number of planets that can potentially support life is,",n)
	n_planetwithlife.goto(300,300)
	n_planetwithlife.begin_fill()
	n_planetwithlife.circle(n)
	n_planetwithlife.end_fill()
	
	l= random.randint(0,100)
	print("(l), the percentage of those planets that actually develop life,",str(l)+"%",l/100)
	l_life.goto(400,400)
	l_life.begin_fill()
	l_life.circle(l)
	l_life.end_fill()
	
	i = random.randint(0,100)
	print("(i), the percentage of planets bearing life on which intelligent,  life, has developed, ",str(i)+"%",i/100)
	i_intellegent.goto(500,500)
	i_intellegent.begin_fill()	
	i_intellegent.circle(i)
	i_intellegent.end_fill()
	
	c = random.randint(0,100)
	print("(c), the percentage of these civilizations that have developed communications, i.e., technologies that release detectable signs into space, ",str(c)+"%",c/100)
	c_communicate.goto(600,600)
	c_communicate.begin_fill()
	c_communicate.circle(c)
	c_communicate.end_fill()
	
	
	lenciv = random.randint(200,1000)
	print("(L), the length of time over which such civilizations release detectable signals, ",lenciv," years.")
	L_civlength.goto(700,700)
	L_civlength.begin_fill()
	L_civlength.circle(lenciv/10)
	L_civlength.end_fill()
	
	numDeCiv = 7*(p/100)*n*(l/1/100)*(i/100)*(c/100)*lenciv
	print("N =", numDeCiv)
	
	for aliens in range(int(numDeCiv)):
		x = random.randint(0,1000)
		y = random.randint(0,1000)
		N_discoverable.goto(x,y)
		#N_discoverable.stamp()  # used on pydroid
		N_discoverable.dot()
	return numDeCiv
	
getRandDrake()

wn.exitonclick()
