import numpy as np
import matplotlib.pyplot as plt

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
#This one below is superellipse
def draw(a,b,n,t):
	na = 2/n
	titikx = []
	titiky = []
	for teta in range(360):
		x = (pangkat(np.abs(np.cos(teta)),na)) * a * sgn(np.cos(teta))
		y = (pangkat(np.abs(np.sin(teta)),na)) * b * sgn(np.sin(teta))
		titikx.append(x)
		titiky.append(y)
		plt.plot(titikx,titiky)
	plt.axis([-3, 3, -3, 3])
	
	plt.savefig('plot'+str(t)+'.png')
	plt.gcf().clear()

#This one below is 2D Supershape
def drawShape(m1, m2, a, b, n1, n2, n3, t):
	titikx = []
	titiky = []
	for angle in range(360):
		r = pangkat(hasil(kiri(m1, angle, a, n2), kanan(m2, angle, b, n3)), 1/n1)
		x = r * np.cos(angle)
		y = r * np.sin(angle)
		titikx.append(x)
		titiky.append(y)
		plt.plot(titikx, titiky)
	plt.axis([-7, 7, -7, 7])
	#plt.show()
	plt.savefig('plot'+str(t)+'.png')
	plt.gcf().clear()

#It's kinda luck to find nice looking shape if you only use your feeling to fill the variable value

#I tried so many time to create one nice looking shape LOL haha

#Goodluck trying!!!

m1 = 3
m2 = 10
a = 6
b = 9
n1 = 10
n2 = 5
n3 = 1
t = 1

for n in range(50):
	#n1 = n+1
	#m1 = n+1
	m2 = n+2
	drawShape(m1, m2, a, b, n1, n2, n3,t)
	t+=1

'''
for n in range(100):
	if n < 2:
		pass
	else:
		n=n/10
		draw(a,b,n,t)
		t+=1
'''