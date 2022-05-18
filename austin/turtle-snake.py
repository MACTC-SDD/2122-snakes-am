from asyncore import loop
from fileinput import close
from tracemalloc import stop
import turtle
import time
import random
import os
import pygame

delay = 0.1
score = 0
high_score = 0
quitting = False
p = os.path.dirname(os.path.abspath(__file__))

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game: Zelda CDI Edition")
wn.bgcolor("blue")
#Background
wn.bgpic(f"{p}/morshu2.gif")


# the width and height can be put as user's choice
wn.setup(width=1920, height=1080)
wn.tracer(0)

# Music
pygame.mixer.init()
dinner = pygame.mixer.Sound (f"{p}/dinner.ogg")
femur = pygame.mixer.Sound (f"{p}/femur.ogg")
hungry = pygame.mixer.Sound (f"{p}/hungry.ogg")
pygame.mixer.music.load(f"{p}/zeldatheme.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# head of the snake
head = turtle.Turtle()
pygame.mixer.Sound.play(hungry)
wn.register_shape (f"{p}/CDILink.gif")
head.shape(f"{p}/CDILink.gif")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"


# food in the game
food = turtle.Turtle()
wn.register_shape (f"{p}/octorok.gif")
colors = random.choice(['blue'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(f"{p}/octorok.gif")
food.color(colors)
food.penup()
food.goto(0, 100)


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-680, 440)
pen.write("Score : 0 High Score : 0", align="center",
		font=("candara", 25, "bold"))

# Main Menu
menu = turtle.Turtle()
wn.register_shape (f"{p}/Main Menu.gif")
menu.shape(f"{p}/Main Menu.gif")
menu.penup()
menu.color("black")
menu.goto(0, 0)
		
# assigning key directions
def group():
	if head.direction != "down":
		head.direction = "up"


def godown():
	if head.direction != "up":
		head.direction = "down"


def goleft():
	if head.direction != "right":
		head.direction = "left"


def goright():
	if head.direction != "left":
		head.direction = "right"

def goquit():
	global quitting
	if head.direction == "Stop":
		print('quitting')
		quitting = True


def move():
	if head.direction != "Stop":
		hide_menu()
	if head.direction == "up":
		y = head.ycor()
		head.sety(y+60)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y-60)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x-60)
	if head.direction == "right":
		x = head.xcor()
		head.setx(x+60)

def show_menu():
	menu.goto(0, 0)

def hide_menu():
	menu.goto(5000, 5000)

wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

wn.onkeypress(group, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")

wn.onkeypress(goquit, "Escape")

segments = []
# Display Main Menu

# Main Gameplay
while True and not quitting:
	wn.update()
	if head.xcor() > 930 or head.xcor() < -939 or head.ycor() > 479.7 or head.ycor() < -479.7:
		pygame.mixer.Sound.play(femur)
		show_menu()
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "Stop"
		colors = random.choice(['red', 'blue', 'green'])
		shapes = random.choice(['square', 'circle'])
		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		score = 0
		delay = 0.1
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("candara", 25, "bold"))
	if head.distance(food) < 60:
		x = random.randint(-930, 920)
		y = random.randint(-470, 470)
		food.goto(x, y)

		# Adding segment
		new_segment = turtle.Turtle()
		wn.register_shape (f"{p}/heart.gif")
		pygame.mixer.Sound.play(dinner)
		new_segment.speed(0)
		new_segment.shape(f"{p}/heart.gif")
		new_segment.color("orange") # tail colour
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		score += 10
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("candara", 25, "bold"))
	# Checking for head collisions with body segments
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)
	move()
	for segment in segments:
		if segment.distance(head) < 60:
			pygame.mixer.Sound.play(femur)
			show_menu()
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"
			colors = random.choice(['red', 'blue', 'green'])
			shapes = random.choice(['square', 'circle'])
			for segment in segments:
				segment.goto(1000, 1000)
			segments.clear()
			score = 0
			delay = 0.1
			pen.clear()
			pen.write("Score : {} High Score : {} ".format(
				score, high_score), align="center", font=("candara", 25, "bold"))
	time.sleep(delay)



