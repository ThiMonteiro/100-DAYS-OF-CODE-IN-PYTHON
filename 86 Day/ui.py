import time
from turtle import Turtle
import random

FONT = ("Courier", 52, "normal")
FONT2 = ("Courier", 32, "normal")
ALIGNMENT = 'center'
COLOR = "white"
COLOR_LIST = ['light blue', 'royal blue',
			'light steel blue', 'steel blue',
			'light cyan', 'light sky blue',
			'violet', 'salmon', 'tomato',
			'sandy brown', 'purple', 'deep pink',
			'medium sea green', 'khaki']


class UI(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.color(random.choice(COLOR_LIST))
		self.header()

	def header(self):
		self.clear()
		self.goto(x=0, y=-150)
		self.write('Breakout', align=ALIGNMENT, font=FONT)
		self.goto(x=0, y=-180)
		self.write('Press Space to PAUSE or RESUME the Game',
				align=ALIGNMENT, font=('Calibri', 14, 'normal'))

	def change_color(self):
		self.clear()
		self.color(random.choice(COLOR_LIST))
		self.header()

	def paused_status(self):
		self.clear()
		self.change_color()
		time.sleep(0.5)

	def game_over(self, win):
		self.clear()
		if win == True:
			self.write('You Cleared the Game', align='center', font=FONT)
		else:
			self.write("Game is Over", align='center', font=FONT)
