import math 

class constants:
	WIDTH = 200
	HEIGHT = 200

class Line:
	def __init__(self):
		self.m=0
		self.b=0
		self.theta=0
		self.r=0


def detect_slope_intercept(image):

	# accessing the image using "image[y][x]"
	# where 0 <= y < constants.WIDTH and 0 <= x < constants.HEIGHT 
	# setting line.m and line.b to be 0 initially 

	line = Line()
	line.m = 0
	line.b = 0

	m_values = []
	start = -10
	while start <= 10:
		m_values.append(start)
		start += 0.01

	# dictionary to store the voting 
	dict = {}
	for y in range(constants.HEIGHT):
		for x in range(constants.WIDTH):
			if image[y][x] == 0:
				for m in m_values: # looping through possible m values between -10 to 10
					b = round(-m*x + y)
					if b > -1000 and b < 1000:
						# if this m,b is not in the dictionary, add it. if it is, then increase the value by 1
						if (m,b) in dict.keys():
							dict[(m,b)] += 1
						else:
							dict[(m,b)] = 1
	
	max_votes = 0

	for (m,b) in dict.keys():
		if dict[(m,b)] > max_votes:
			max_votes = dict[(m,b)]
			line.m = m
			line.b = b

	return line

def detect_circles(image, radius=30):

	# accessing the image using "image[y][x]"
	# where 0 <= y < constants.WIDTH and 0 <= x < constants.HEIGHT 

	count = 0 # number of circles found 

	dict = {}

	for y in range(200):
		for x in range(200):
			if image[y][x] == 0:
				for a in range(200):
					if radius**2 - (x-a)**2 >= 0:
						b = round(y - math.sqrt(radius**2 - (x-a)**2))
						
						if (a,b) in dict.keys():
							dict[(a,b)] += 1
						else:
							dict[(a,b)] = 1
	
	for (a,b) in dict.keys():
		if dict[(a,b)] >= 37:
			count += 1

	return count
				