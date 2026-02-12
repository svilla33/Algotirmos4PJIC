#Basicamente el programa es una pecera, cuando choca en los bordes rebota, 



import os
import random
import time

width = 80
height = 20
fps = 0.1

def clear():
	os.system("cls" if os.name== "nt" else "clear")

class Fish:
	def __init__(self):
		self.x = random.randint(0, width - 5)
		self.y = random.randint(0, height - 1)
		self.direction = random.choice([-1,1])
		self.speed = random.choice([1 ,1 ,1 ,2 ])

	def shape(self):
		if self.direction == 1:
			return "><((('>"
		else:
			return "<')))><"

	def move(self):
		self.x += self.direction * self.speed

		#Rebotar en bordes
		if self.x <= 0:
			self.direction = 1
		elif self.x >= width - len(self.shape()):
			self.direction = -1

		#movimiento vertial leve
		if random.random() < 0.2:
			self.y += random.choice([-1 ,1])
			self.y = max(0, min(height - 1, self.y))

fishes = [Fish() for _ in range(5)]

while  True:
	buffer = [[" " for _ in range(width)] for _ in range(height)]

	for fish in fishes:
		fish.move()
		shape = fish.shape()

		for i, ch in enumerate(shape):
			x = fish.x + i
			if 0 <= x < width:
				buffer[fish.y][x] = ch

	clear()

	for row in buffer:
		print("".join(row))

	time.sleep(fps)

