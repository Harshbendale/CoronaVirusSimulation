'''
Corona Virus Simulation
18-03-2020
@author: Harshal Bendale
'''

'''
Factors considered:
1. Time span of 600 units
2. Time needed to create vaccine is considered = 100 time units
3. Population of 100
4. Initially infected: 1 person out of 100
5. Gaussian distribution of immunity power of people in simulation
6. Mortality rate of Corona Virus



Factors in real life that are not considered:
1. Density distribution of population over the given area
2. Flow/movement of population according to places which are defined as public places f.e.:Bus stop, shopping mall, etc.
3. Effect of weather on virus spread
4. Age of the people
5. Minimum distance between two people in order to spread the virus. Here it is considered only on touch.
6. Time taken to mass produce vaccine, once it is developed
7. Time taken for the vaccine to reach the victim's place
8. Time taken to determine if a person is infected by the virus or not
9. Quarantine time period (and also fixing position) for certain time units
10. Time taken by the victim to recover based on his immunity to recover from virus infection
'''

#libraries:
import numpy as np
import turtle
from Person import *
#from ipywidgets import interact
#import ipywidgets as widgets

wn = turtle.Screen()
#wn.setup(1300,600)
wn.setup(0.85,0.78,30,30)
wn.screensize(600,400)
wn.bgcolor('black')
wn.title('Corona Virus Simulation')
wn.tracer(0)
tpen = turtle.Turtle()
tpen.penup()
tpen.hideturtle()
tpen.pen(fillcolor='black',pencolor='white')
#text_box.shape('square')
tpen.goto(330,250)
tpen.write("Corona Virus Simulation", move=False, align='center',font=("Georgia",20,"italic"))
tpen.goto(180,130)
tpen.write("Total Number of people:     100\nPeople not affected by Corona:\nPeople having Corona:\nPeople cured/now immmune to Corona:\nPeople alive:\nPeople dead:", move=False, align="left", font=("Arial", 13, "normal"))
tpen.goto(180,-90)
tpen.write("Factors considered for this simulation:\n1. Simulation time span of 600 time units\n2. Time needed to create vaccine is considered = 100 time units\n3. Population of 100\n4. Initially infected: 1 person out of 100\n5. Mortality rate of Corona Virus according to age of victim\n6. Age group of people: 20-90 with average age between 57-63\n7. Inverse proportionality of age with power to fight Corona\n8. Direct proportionality of immunity with power to fight Corona\n9. Gaussian distribution of immunity power of people in simulation",move=False, align="left", font=("Arial", 9, "normal"))
tpen.goto(185,-280)
tpen.write("@author: Harshal Bendale\nMasters Student, Data Engineering, Jacobs University Bremen",move=False, align="left", font=("Comic Sans MS", 8, "normal"))
totcircle = turtle.Turtle()
totcircle.shape('circle')
totcircle.penup()
totcircle.shapesize(0.8,0.8)
totcircle.color('gray')
totcircle.goto(365,236)
bcircle = turtle.Turtle()
bcircle.shape('circle')
bcircle.penup()
bcircle.shapesize(0.8,0.8)
bcircle.color('blue')
bcircle.goto(286,160)
gcircle = turtle.Turtle()
gcircle.shape('circle')
gcircle.penup()
gcircle.shapesize(0.8,0.8)
gcircle.color('green')
gcircle.goto(420,215)
rcircle = turtle.Turtle()
rcircle.shape('circle')
rcircle.penup()
rcircle.shapesize(0.8,0.8)
rcircle.color('red')
rcircle.goto(358,196)
vcircle = turtle.Turtle()
vcircle.shape('circle')
vcircle.penup()
vcircle.shapesize(0.8,0.8)
vcircle.color('violet')
vcircle.goto(480,178)

time_pen = turtle.Turtle()
time_pen.penup()
time_pen.hideturtle()
time_pen.goto(180,103)
time_pen.pen(fillcolor='black',pencolor='white')
time_pen.write("Total time: 600 time units", move=False, align="left", font=("Arial", 13, "normal"))
time_pen.goto(180,85)
time_pen.write("Vaccine discovered at time instance: 100 time units", move=False, align="left", font=("Arial", 13, "normal"))
time_pen.goto(180,65)
time_pen.write("Time Elapsed:", move=False, align="left", font=("Arial", 13, "normal"))
time_pen_running = turtle.Turtle()
time_pen_running.penup()
time_pen_running.pen(fillcolor='black',pencolor='white')
time_pen_running.hideturtle()
time_pen_running.goto(290,65)
time_pen_running.write('0', move=False, align="left", font=("Arial", 13, "normal"))

tnot_affected = turtle.Turtle()
tnot_affected.penup()
tnot_affected.hideturtle()
tnot_affected.pen(fillcolor='black',pencolor='white')
tnot_affected.goto(433,206)
tnot_affected.write('100', move=False, align="left", font=("Arial", 13, "normal"))

thaving_corona = turtle.Turtle()
thaving_corona.penup()
thaving_corona.hideturtle()
thaving_corona.pen(fillcolor='black',pencolor='white')
thaving_corona.goto(375,187)
thaving_corona.write('1',move=False, align="left", font=("Arial", 13, "normal"))

tcured = turtle.Turtle()
tcured.penup()
tcured.hideturtle()
tcured.pen(fillcolor='black',pencolor='white')
tcured.goto(495,168)
tcured.write('0',move=False, align="left", font=("Arial", 13, "normal"))

talive = turtle.Turtle()
talive.penup()
talive.hideturtle()
talive.pen(fillcolor='black',pencolor='white')
talive.goto(300,150)
talive.write('100',move=False, align="left", font=("Arial", 13, "normal"))

tdead = turtle.Turtle()
tdead.penup()
tdead.hideturtle()
tdead.pen(fillcolor='black',pencolor='white')
tdead.goto(300,130)
tdead.write('0',move=False, align="left", font=("Arial", 13, "normal"))

#for graph:
total_graph = turtle.Turtle()
total_graph.shape('circle')
total_graph.shapesize(0.2,0.2)
total_graph.color('gray')
total_graph.penup()
total_graph_coor=[180,-100]
total_graph.goto(total_graph_coor[0],total_graph_coor[1])
total_graph.pendown()

alive_graph = turtle.Turtle()
alive_graph.shape('circle')
alive_graph.shapesize(0.2,0.2)
alive_graph.color('blue')
alive_graph.penup()
alive_graph_coor=[180,-100]
alive_graph.goto(alive_graph_coor[0],alive_graph_coor[1])
alive_graph.pendown()

not_affected_graph = turtle.Turtle()
not_affected_graph.shape('circle')
not_affected_graph.shapesize(0.2,0.2)
not_affected_graph.color('green')
not_affected_graph.penup()
not_affected_graph_coor=[180,-99.5]
not_affected_graph.goto(not_affected_graph_coor[0],not_affected_graph_coor[1])
not_affected_graph.pendown()

having_corona_graph = turtle.Turtle()
having_corona_graph.shape('circle')
having_corona_graph.shapesize(0.2,0.2)
having_corona_graph.color('red')
having_corona_graph.penup()
having_corona_graph_coor=[180,-240]
having_corona_graph.goto(having_corona_graph_coor[0],having_corona_graph_coor[1])
having_corona_graph.pendown()

cured_graph = turtle.Turtle()
cured_graph.shape('circle')
cured_graph.shapesize(0.2,0.2)
cured_graph.color('violet')
cured_graph.penup()
cured_graph_coor=[180,-240]
cured_graph.goto(cured_graph_coor[0],cured_graph_coor[1])
cured_graph.pendown()

persons = []
for i in range(100):
	p = Person()
	xyscale = [-2,-1,-0.5,0.5,1,2]
	p.dx = np.random.choice(xyscale)
	p.dy = np.random.choice(xyscale)
	if i == 0:
		p.circle.color('red')
		p.corona = True
		p.dx = np.random.choice([-2,2])
		p.dy = np.random.choice([-2,2])
		p.circle.goto(-225,0)
	persons.append(p)

count_alive = 0
count_dead = 0
total_time = 600
time_unit = 0
hist_count_alive = [100,0]
hist_count_cured = [0,0]
hist_count_not_affected = [99,0]
hist_count_having_corona = [1,0]
while total_time != 0:
	wn.update()
	count_not_affected = 0
	count_having_corona = 0
	count_cured = 0
	total_time -= 1
	time_unit += 1
	time_pen_running.clear()
	time_pen_running.write(time_unit, move=False, align="left", font=("Arial", 13, "normal"))
	#for person in persons:
		
	if time_unit == 100:
		for doctor in persons:
			if doctor.alive == True and doctor.corona == False:
				doctor.circle.color('violet')
				doctor.cured = True
				if doctor.circle.xcor()>-225 and doctor.circle.ycor()>0:
					doctor.dx = -2
					doctor.dy = -2
				if doctor.circle.xcor()<-225 and doctor.circle.ycor()>0:
					doctor.dx = 2
					doctor.dy = -2
				if doctor.circle.xcor()<-225 and doctor.circle.ycor()<0:
					doctor.dx = 2
					doctor.dy = 2
				if doctor.circle.xcor()>-225 and doctor.circle.ycor()<0:
					doctor.dx = -2
					doctor.dy = 2
				#doctor.dx = np.random.choice([-2,2])
				#doctor.dy = np.random.choice([-2,2])
				count_cured += 1
				break
	for p in persons:
		if p.alive == True:
			if p.corona == True:
				p.power -= (p.dp)/1000
				if p.power <= 0:
					p.alive = False
					p.circle.color('black')
					p.circle.goto(600,400)
					count_dead += 1
			p.circle.sety(p.circle.ycor() + p.dy)
			p.circle.setx(p.circle.xcor() + p.dx)

			#check ball collision:
			for p2 in persons:
				if p2.alive == True:
					if p==p2: continue
					d = p.get_distance(p2.circle.xcor(),p2.circle.ycor())
					if d < 23:
						#spread of corona:
						if p.corona == True and p2.cured == False:
							p2.corona = True
							p2.circle.color('red')
						elif p2.corona == True and p.cured == False:
							p.corona = True
							p.circle.color('red')
						#curing of corona:
						if p.cured == True and p2.cured == False:
							p2.circle.color('violet')
							p2.corona = False
							p2.cured = True
							count_cured += 1
						elif p2.cured == True and p.cured == False:
							p.circle.color('violet')
							p.corona = False
							p.cured = True
							count_cured += 1

						#p1 to 4th and p2 to 1st:
						if p.dx>0 and p.dy<0 and p2.dx>0 and p2.dy>0:
							if (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dy *= -1
								p2.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dy *= -1
								p2.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dx *= -1
							elif (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p2.dx *= -1

						#p1 to 3rd and p2 to 2nd: 
						elif p.dx<0 and p.dy<0 and p2.dx<0 and p2.dy>0:
							if (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dy *= -1
								p2.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dy *= -1
								p2.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p2.dx *= -1
							elif (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								pass

						#p1 to 1st and p2 to 2nd:
						elif (p.dx>0 and p.dy>0 and p2.dx<0 and p2.dy>0):
							if (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p2.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dx *= -1
								p2.dx *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dx *= -1
								p2.dx *= -1
							elif (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dy *= -1

						#p1 to 4th and p2 to 3rd:
						elif (p.dx>0 and p.dy<0 and p2.dx<0 and p2.dy<0):
							if (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dx *= -1
								p2.dx *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dx *= -1
								p2.dx *= -1
							elif (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p2.dy *= -1

						#p1 to 1st and p2 also to 1st:
						elif p.dx>0 and p.dy>0 and p2.dx>0 and p2.dy>0:
							if (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p2.dx *= -1
								p2.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p2.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dx *= -1
								p.dy *= -1
							elif (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dy *= -1
								p2.dx *= -1

						#p1 to 2nd and p2 to 2nd:
						elif p.dx<0 and p.dy>0 and p2.dx<0 and p2.dy>0:
							if (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p2.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p2.dx *= -1
								p2.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dy *= -1
							elif (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dx *= -1
								p.dy *= -1

						#p1 to 3rd and p2 to 3rd:
						elif p.dx<0 and p.dy<0 and p2.dx<0 and p2.dy<0:
							if (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dx *= -1
								p.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p2.dx *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p2.dx *= -1
								p2.dy *= -1
							elif (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								pass

						#p1 to 4th and p2 to 4th:
						elif p.dx>0 and p.dy<0 and p2.dx>0 and p2.dy<0:
							if (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p2.dx *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dx *= -1
								p.dy *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p2.dy *= -1
							elif (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p2.dx *= -1
								p2.dy *= -1

						#head on collosions:
						#p1 to 1st and p2 to 3rd:
						elif p.dx>0 and p.dy>0 and p2.dx<0 and p2.dy<0:
							if (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								pass
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dx *= -1
								p2.dx *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dx *= -1
								p.dy *= -1
								p2.dx *= -1
								p2.dy *= -1
							elif (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dy *= -1
								p2.dy *= -1

						#p1 to 2nd and p2 to 4th:
						elif p.dx<0 and p.dy>0 and p2.dx>0 and p2.dy<0:
							if (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								p.dx *= -1
								p2.dx *= -1
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()>p2.circle.ycor()):
								pass
							elif (p.circle.xcor()<p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dy *= -1
								p2.dy *= -1
							elif (p.circle.xcor()>p2.circle.xcor() and p.circle.ycor()<p2.circle.ycor()):
								p.dx *= -1
								p.dy *= -1
								p2.dx *= -1
								p2.dy *= -1
						

				#check box borders:
				if ((p.circle.ycor() < -275) or (p.circle.ycor() > 275)) and (p.alive==True):
					p.dy *= -1
					if p.circle.ycor() < -275:
						p.circle.sety(-275)
					if p.circle.ycor() > 275:
						p.circle.sety(275)
				if ((p.circle.xcor() < -525) or (p.circle.xcor() > 125)) and (p.alive==True):
					p.dx *= -1
					if p.circle.xcor() < -525:
						p.circle.setx(-525)
					if p.circle.xcor() > 125:
						p.circle.setx(125)
		if p.circle.color()[0] == 'red':
			count_having_corona += 1
		if p.circle.color()[0] == 'green':
			count_not_affected += 1
		if p.circle.color()[0] == 'violet':
			count_cured += 1


	count_not_affected = 100 - count_dead - count_cured -count_having_corona
	count_alive = 100 - count_dead
	tnot_affected.clear()
	tnot_affected.write(count_not_affected, move=False, align="left", font=("Arial", 13, "normal"))
	thaving_corona.clear()
	thaving_corona.write(count_having_corona, move=False, align="left", font=("Arial", 13, "normal"))
	tcured.clear()
	tcured.write(count_cured, move=False, align="left", font=("Arial", 13, "normal"))
	talive.clear()
	talive.write(count_alive, move=False, align="left", font=("Arial", 13, "normal"))
	tdead.clear()
	tdead.write(count_dead, move=False, align="left", font=("Arial", 13, "normal"))

	#for graph:
	#for y-coordinates:
	hist_count_alive[1] = count_alive
	hist_count_not_affected[1] = count_not_affected
	hist_count_having_corona[1] = count_having_corona
	hist_count_cured[1] = count_cured

	#for x-coordinates:
	total_graph_coor[0] += (1/2)
	alive_graph_coor[0] += (1/2)
	not_affected_graph_coor[0] += (1/2)
	having_corona_graph_coor[0] += (1/2)
	cured_graph_coor[0] += (1/2)

	#for y-coordinates:
	alive_graph_coor[1] += (hist_count_alive[1]-hist_count_alive[0])*1.4
	not_affected_graph_coor[1] += (hist_count_not_affected[1]-hist_count_not_affected[0])*1.4
	having_corona_graph_coor[1] += (hist_count_having_corona[1]-hist_count_having_corona[0])*1.4
	cured_graph_coor[1] += (hist_count_cured[1]-hist_count_cured[0])*1.4
	#cured_graph_coor[1] += (1/4.3)

	hist_count_alive[0] = hist_count_alive[1]
	hist_count_not_affected[0] = hist_count_not_affected[1]
	hist_count_having_corona[0] = hist_count_having_corona[1]
	hist_count_cured[0] = hist_count_cured[1]

	total_graph.goto(total_graph_coor[0],total_graph_coor[1])
	alive_graph.goto(alive_graph_coor[0],alive_graph_coor[1])
	not_affected_graph.goto(not_affected_graph_coor[0],not_affected_graph_coor[1])
	having_corona_graph.goto(having_corona_graph_coor[0],having_corona_graph_coor[1])
	cured_graph.goto(cured_graph_coor[0],cured_graph_coor[1])


wn.mainloop()