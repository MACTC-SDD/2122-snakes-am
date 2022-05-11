import os
import math
import random
from re import L
import turtle
import time
import pygame
#from playsound import playsound
from tkinter import PhotoImage

p = os.path.dirname(os.path.abspath(__file__))

# Game enhancement options
# Elapsed Time - Kelsey
# Boost - Julius
# Audio (Effects) - Jayden, Nolan, Aiden
# Background Music - Julius
# Explosions - Alex
# Gradient - Luciel
# Real-time boundary adjustment - Nolan
# Food alignment - De'Antae
# Disable resize - Colling
BG_IMG = True       # Set background image
HEAD_IMG = True     # Set snake head image
SHOW_STATS = False   # Show statistics by default (toggle with '1')
TAIL_GRADIENT = True # Set tail gradient base on starting color
RND_TAIL_SHAPE = False # Pick a random shape for tail
SCORE_METHOD = "progressive" # Pick from progressive or standard
BG_MUSIC = True     # Play background music (toggle with '2')
SOUND_EFFECTS = True # Play sound effects on eating/dying
EXPLODE = True      # Show Explosing effect
CLEAR_HS = False     # Reset high score when launching
ALIGN_FOOD = True   # Make food line up with snake
DISABLE_RESIZE = True # Disable window resizing

# TODO: Enhancements to add
GET_CONFIG = False  # Gather config settings at start
BOOST = False       # Use space bar booster


# Other game options
food_padding = 30
border_padding = 10
game_width = 800
game_height = 600
init_delay = 0.1
show_stats = SHOW_STATS
segments_level = 6
segment_offset = 24

# Colors
BLUE = (0.15, 0.1, 0.7)
ORANGE = (1.0, 0.65, 0.0)
WHITE = (1.0, 1.0, 1.0)
GREEN = (0.15, 1.0, 0.15)
RED = (1.0, 0.15, 0.15)

level_colors = [ORANGE, GREEN, RED, WHITE, BLUE, WHITE, RED, GREEN, ORANGE]
all_colors = ['red','green','black']
shapes = ["classic", "arrow", "turtle", "circle", "square", "triangle"]


# Init variables
config_file = {}
delay = init_delay

score = 0
tail_color = ORANGE
tail_shape = "square"
if RND_TAIL_SHAPE:
    tail_shape = random.choice(shapes)

start_time = time.time()

# If bg music is Off, set as paused
music_paused = not BG_MUSIC

# Stat variables
stat_food = 0
stat_food_max = 0
stat_length = 0
stat_length_max = 0
stat_etime = 0
stat_etime_max = 0
stat_tick_count = 0

# Create a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
if BG_IMG:
    wn.bgpic(f"{p}/images/desert.gif")
wn.setup(width=game_width, height=game_height)
wn.tracer(0)

if DISABLE_RESIZE:
    root = wn._root
    root.resizable(False, False)

# Init audio
pygame.mixer.init()
pygame.mixer.music.load(f"{p}/sounds/tumbleweed.mp3")
food_sounds = []
food_sounds.append(pygame.mixer.Sound(f"{p}/sounds/bell.wav"))
food_sounds.append(pygame.mixer.Sound(f"{p}/sounds/whip-crack-1.wav"))

hiss_sounds = []
for i in range(0,4):
    hiss_sounds.append(pygame.mixer.Sound(f"{p}/sounds/hiss{i}.wav"))

dead_sound = pygame.mixer.Sound(f"{p}/sounds/dead.wav")

# Start music
if BG_MUSIC:
    pygame.mixer.music.play(-1) # If number of times = -1, keep playing

# Create title
title_images = []
for i in range(1,9):
    t = PhotoImage(file=f"{p}/images/title{i}.png")
    title_images.append(t)
    wn.addshape(f"title_image{i}", turtle.Shape("image", t))

title = turtle.Turtle()
title.penup()
title.hideturtle()

# Head of the snake
head = turtle.Turtle()
head.shape("arrow")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"
if HEAD_IMG:
    wn.addshape(f"{p}/images/snake-head-down.gif")
    wn.addshape(f"{p}/images/snake-head-up.gif")
    wn.addshape(f"{p}/images/snake-head-left.gif")
    wn.addshape(f"{p}/images/snake-head-right.gif")
    head.shape(f"{p}/images/snake-head-up.gif")

# Food in the game
food = turtle.Turtle()

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, game_height/2-50)

statpen = turtle.Turtle()
statpen.speed(0)
statpen.shape("square")
statpen.color("white")
statpen.penup()
statpen.hideturtle()
statpen.goto(-game_width/2+20,-game_height/2+50)

### Functions

# Setup / Load config file
def init_config_file():
    # Load defaults into map
    # This takes care of missing entries + init creation
    config_file['high_score'] = 0
    config_file['total_plays'] = 0
    config_file['total_segs'] = 0
    
    if os.path.exists(f'{p}/snake.cfg'):
        with open(f'{p}/snake.cfg') as f:
            lines = f.readlines()
            for l in lines:
                kvp = l.split('=')
                try:
                    # Silly, but if we can convert it to int, do so
                    kvp[1] = int(kvp[1])
                except: pass
                config_file[kvp[0]] = kvp[1]
    else:
        save_config()

    if CLEAR_HS:
        config_file['high_score'] = 0

def save_config():
    with open(f'{p}/snake.cfg', 'w') as f:        
        for k in config_file:
            f.write(f'{k}={config_file[k]}\n')

# Assigning key directions
def goup():
    if head.direction == "stop":
        title_off()
        start_time = time.time()
    if head.direction != "down" and head.direction != "up":
        head.shape(f"{p}/images/snake-head-up.gif")
        head.direction = "up"

def godown():
    if head.direction == "stop":
        title_off()
        start_time = time.time()
    if head.direction != "up" and head.direction != "down":
        head.shape(f"{p}/images/snake-head-down.gif")
        head.direction = "down"

def goleft():
    if head.direction == "stop":
        title_off()
        start_time = time.time()
    if head.direction != "right" and head.direction != "left":
        head.shape(f"{p}/images/snake-head-left.gif")
        head.direction = "left"

def goright():
    if head.direction == "stop":
        title_off()
        start_time = time.time()
    if head.direction != "left" and head.direction != "right":
        head.shape(f"{p}/images/snake-head-right.gif")
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor()+segment_offset)
    if head.direction == "down":
        head.sety(head.ycor()-segment_offset)
    if head.direction == "left":
        head.setx(head.xcor()-segment_offset)
    if head.direction == "right":
        head.setx(head.xcor()+segment_offset)

def title_off():
    for i in range(1,9):
        title.shape(f'title_image{i}')
        wn.update()
        time.sleep(.05)

    title.goto(9999,9999)
    wn.update()

def title_show():
    title.goto(0,100)
    title.showturtle()
    wn.update()

    for i in range(8,0,-1):
        title.shape(f'title_image{i}')
        wn.update
        time.sleep(.05)

def toggle_stats():
    global show_stats
    show_stats = not show_stats
    update_stats()

def toggle_music():
    global music_paused
    music_paused = not music_paused

    if music_paused == True:
        pygame.mixer.music.pause()
    else:
        # In case we unpause but never started
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.unpause()
        else: 
            pygame.mixer.music.play()

def update_score():
    pen.clear()
    pen.write(f"Score : {score}  High Score : {config_file['high_score']}", align="center",
            font=("candara",24,"bold"))

def update_stats():
    statpen.clear()
    if show_stats:
        statpen.write(f"Length: {stat_length}  Time: {round(stat_etime,2)}\nMax Len: {stat_length_max}  Max Time: {round(stat_etime_max,2)}\nTotal Plays: {config_file['total_plays']}",
            align="left", font=("candara",16,"normal"))

def lose_game():
    # This seems like bad practice but needed to assign to global vars
    global score
    global delay
    global stat_etime
    global config_file

    if SOUND_EFFECTS:
        pygame.mixer.Sound.play(dead_sound)

    if EXPLODE:
        for i in range(0,15):
            for segment in segments:
                segment.goto(segment.xcor() + segment.losex, segment.ycor() + segment.losey)
                #segment.color('red')
                #segment.shape('circle')
                segment.color(random.choice(all_colors))
                segment.shape(random.choice(shapes))
            
            wn.update()
            time.sleep(.1)
        
    for segment in segments:
            segment.goto(9999,9999)
    
    config_file['total_plays'] += 1
    config_file['total_segs'] += len(segments)
    save_config()

    segments.clear()


    head.goto(0,0)
    head.direction = "stop"
    score = 0
    stat_food = 0
    stat_length = 0
    stat_etime = 0

    delay = init_delay

    update_score()
    update_stats()
    title_show()

    # Make music restart?

def place_food(x=9999,y=9999):
    if x == 9999:
        x = random.randint(-(int(wn.window_width()/2)-food_padding),int(wn.window_width()/2)-food_padding)
    if y == 9999:
        y = random.randint(-(int(wn.window_height()/2)-food_padding),int(wn.window_height()/2)-food_padding)
 
    if ALIGN_FOOD:
        x = int(x/segment_offset) * segment_offset
        y = int(y/segment_offset) * segment_offset

    colors = random.choice(all_colors)
    shapes = random.choice(['square','triangle','circle'])
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(x,y)

# Main program
init_config_file()

# Bind keypresses
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "s")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "a")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "d")
wn.onkeypress(goright, "Right")
wn.onkeypress(toggle_stats, "1")
wn.onkeypress(toggle_music, "2")

title_show()
update_score()
update_stats()
place_food(0,100)
segments = []

# Main gameplay
while True:
    wn.update()

    # Check for too close to a wall
    if head.xcor() > wn.window_width()/2-border_padding \
        or head.xcor() < -(wn.window_width()/2-border_padding) \
        or head.ycor() > wn.window_height()/2-border_padding \
        or head.ycor() < -(wn.window_height()/2-border_padding):
        lose_game()

    # Check for food gathering
    if head.distance(food) < 20:
        if SOUND_EFFECTS:
            pygame.mixer.Sound.play(random.choice(food_sounds))
        place_food()

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed = 0
        new_segment.shape(tail_shape)
        new_segment.color(tail_color)
        new_segment.penup()
        new_segment.losex = random.randint(-20,20)
        new_segment.losey = random.randint(-20,20)
        segments.append(new_segment)
        delay = max(delay - 0.002, .001)

        # Change tail color based on level
        if len(segments) % segments_level == 0:
            tail_color = level_colors[min(int(len(segments) / segments_level),len(level_colors)-1)]

        if SCORE_METHOD == "progressive":
            score += 10 + len(segments)
        else:
            # Classic
            score += 10

        if score > config_file['high_score']:
            config_file['high_score'] = score
            save_config()
        
        stat_food += 1
        stat_length = len(segments)

        if stat_food > stat_food_max:
            stat_food_max = stat_food

        if stat_length > stat_length_max:
            stat_length_max = stat_length


        update_score()
        #update_stats()

    # Starting with newest segment, move each to position of previous segment
    for index in range(len(segments)-1, -1, -1):
        x = head.xcor()
        y = head.ycor()

        if index > 0:
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()

        segments[index].goto(x,y)
        if TAIL_GRADIENT:
            r = max(.1,tail_color[0]-(index*.02))
            g = max(.1,tail_color[1]-(index*.02))
            b = max(.1,tail_color[2]-(index*.02))
            segments[index].color(r,g,b)
        else:
            segments[index].color(tail_color)

    # Move head to the front
    head.forward(0)
    
    move()

    # Check to see if head is too close to a segment
    for segment in segments:
        if segment.distance(head) < 20:
            lose_game()
            break

    if head.direction != "stop":
        stat_etime = time.time() - start_time
        if stat_etime > stat_etime_max:
            stat_etime_max = stat_etime
        
        if stat_tick_count % 10 == 0:
            update_stats()
    else:
        start_time = time.time()
    
    # Hiss now and then
    if SOUND_EFFECTS and stat_tick_count % random.randint(15,30) == 0:
        pygame.mixer.Sound.play(random.choice(hiss_sounds))

    time.sleep(delay)
    stat_tick_count += 1
wn.mainloop()


'''
Notes:
Ideas - 
  Keep top 5 scores and allow initials to be entered
  Death screen 
  Boost
'''