import numpy as np
import pyglet
from pyglet.gl import *

def sgn(val):
	if val > 0:
		return 1
	elif val < 0:
		return -1
	else:
		return 0

def pangkat(p,q):
	return np.power(p,q)

#This function to sum the left side and rigth side
def hasil(kiri, kanan):
	return kiri+kanan

#This function to calculate the left side of '+'
def kanan(m2, angle, b, n3):
	return np.power(np.abs((np.sin((m2*angle)/4))/b), n3)

#This function to calculate the rigth side of '+'
def kiri(m1, angle, a, n2):
	return np.power(np.abs((np.cos((m1*angle)/4))/a), n2)

'''
Please be careful when editing x and y equation in below function, 
wrong variable placing can cause a headache.
I suffer headache for about 1 hour when creating this XD 
'''
#This one below is 2D Supershape
@win.event
def drawShape(m1, m2, a, b, n1, n2, n3):
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POINTS)
	pi = 180*12
	
	for angle in range(pi*100):
		angle = angle/100
		r = pangkat(hasil(kiri(m1, angle, a, n2), kanan(m2, angle, b, n3)), -1/n1)
		x = r * np.cos(angle)
		y = r * np.sin(angle)
		glVertex2f(x, y)
	glEnd()
	pyglet.app.run()

#It's kinda luck to find nice looking shape if you only use your feeling to fill the variable value

#I tried so many time to create one nice looking shape LOL haha

#Goodluck trying!!!

m1 = 2
m2 = 2
a = 1
b = 1
n1 = 0.3
n2 = 0.3
n3 = 0.3

drawShape(m1, m2, a, b, n1, n2, n3)
