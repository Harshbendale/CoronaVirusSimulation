import numpy as np
import turtle
from math import *

class Person:
	def __init__(self):
		'''
		DOCSTRING:
		The ages and immunity list here is derived from Gaussian distribution. The ages are sorted and thus ascending,
		but one can see the gaussian distribution in the immune as it is not sorted.
		The ages considered are from 20 to 90.
		Considering the given scenario of ages and immunities, best possible power is (1/age)*immunity = 0.04668
		The worst possible power is = 0.0020002. Thus we are considering 0.003 as our threshold power to stay alive.
		The mortality rate of Corona virus is dependent on age according to the reference:
		"https://www.businessinsider.de/international/coronavirus-death-age-older-people-higher-risk-2020-2/?r=US&IR=T"
		'''
		ages = [20, 22, 23, 23, 23, 25, 26, 26, 27, 28, 28, 30, 30, 31, 31, 32, 32, 33, 34, 34, 36, 37, 37, 37, 37, 44, 44, 44, 45, 46, 47, 47, 48, 48, 48, 49, 50, 52, 52, 53, 53, 53, 54, 54, 54, 56, 57, 57, 57, 58, 59, 60, 60, 60, 61, 61, 61, 61, 62, 63, 64, 64, 64, 64, 67, 67, 67, 68, 69, 70, 70, 71, 71, 71, 72, 72, 72, 72, 73, 75, 77, 77, 79, 79, 80, 80, 81, 81, 82, 83, 84, 85, 86, 87, 87, 87, 88, 88, 88, 89, 89, 90]
		immunities = [0.18002174306102336, 0.203469094679261, 0.22892991893252546, 0.2564113632696939, 0.2858923881068971, 0.31732079127501545, 0.35061062764926815, 0.38564014308622546, 0.4222503380244532, 0.4602442675408985, 0.4993871711480854, 0.5394075072376268, 0.5799989441308117, 0.6208233327384809, 0.6615146556493747, 0.7016839150659776, 0.7409248885809977, 0.7788206486646053, 0.8149507103200271, 0.8488986430831712, 0.88025995975156, 0.90865008975156, 0.93371212200271, 0.93371212200271, 0.90865008975156, 0.8802599597515598, 0.848898643083171, 0.8149507103200269, 0.7788206486646051, 0.7409248885809975, 0.7016839150659773, 0.6615146556493745, 0.6208233327384806, 0.5799989441308114, 0.5394075072376264, 0.4993871711480851, 0.46024426754089814, 0.42225033802445294, 0.3856401430862252, 0.35061062764926787, 0.31732079127501517, 0.28589238810689693, 0.2564113632696937, 0.22892991893252526, 0.20346909467926078, 0.1800217430610231]
		self.circle = turtle.Turtle()
		self.circle.shape('circle')
		self.circle.shapesize(1,1)
		self.circle.color('green')
		self.circle.penup()
		self.x = np.random.randint(-525,125)
		self.y = np.random.randint(-275,275)
		self.pos = [self.x,self.y]
		self.circle.speed(0)
		self.circle.goto(self.x,self.y)
		self.dx = 0
		self.dy = 0

		#other attributes:
		self.alive = True
		self.corona = False
		self.cured = False
		self.immunity = np.random.choice(immunities)
		self.age = np.random.choice(ages)
		self.power = (1/(self.age))*(self.immunity)
		self.dp = 0
		if self.age <= 39: self.dp = 0.002
		if self.age <= 49 and self.age >=40: self.dp = 0.004
		if self.age <= 59 and self.age >=50: self.dp = 0.013
		if self.age <= 69 and self.age >=60: self.dp = 0.036
		if self.age <= 79 and self.age >=70: self.dp = 0.08
		if self.age <= 89 and self.age >=80: self.dp = 0.148

	def get_distance(self,p2x,p2y):
		summation = (self.circle.xcor() - p2x)**2 + (self.circle.ycor() - p2y)**2
		dist = sqrt(summation)
		return abs(dist)