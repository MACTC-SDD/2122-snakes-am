import turtle
import time
import random

init_delay = 0.1
delay = init_delay
score = 0
high_score = 0

# Other options
food_padding = 30
border_padding = 10
game_width = 600
game_height = 400

# Create a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")

wn.setup(width=game_width, height=game_height)
wn.tracer(0)

# Head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "Stop"


# Food in the game
food = turtle.Turtle()

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, game_height/2-50)

# Assigning key directions
def goup():
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

def move():
    if head.direction == "up":
        head.sety(head.ycor()+20)
    if head.direction == "down":
        head.sety(head.ycor()-20)
    if head.direction == "left":
        head.setx(head.xcor()-20)
    if head.direction == "right":
        head.setx(head.xcor()+20)

def update_score():
    pen.clear()
    pen.write(f"Score : {score}  High Score : {high_score}", align="center",
            font=("candara",24,"bold"))

def lose_game():
    # This seems like bad practice but needed to assign to global vars
    global score
    global high_score
    global delay

    for segment in segments:
        segment.goto(9999,9999)
    
    segments.clear()

    head.goto(0,0)
    head.direction = "stop"
    score = 0
    delay = init_delay

    update_score()
    print ("lose game code")

def place_food(x=9999,y=9999):
    if x == 9999:
        x = random.randint(-(game_width/2-food_padding),game_width/2-food_padding)
    if y == 9999:
        y = random.randint(-(game_height/2-food_padding),game_height/2-food_padding)
 
    colors = random.choice(['red','green','black'])
    shapes = random.choice(['square','triangle','circle'])
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(x,y)

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

update_score()
place_food(0,100)
segments = []

# Main gameplay
while True:
    wn.update()

    # Check for too close to a wall
    if head.xcor() > game_width/2-border_padding \
        or head.xcor() < -(game_width/2-border_padding) \
        or head.ycor() > game_height/2-border_padding \
        or head.ycor() < -(game_height/2-border_padding):
        lose_game()

    # Check for food gathering
    if head.distance(food) < 20:
        place_food()

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        
        update_score()

    # Starting with newest segment, move each to position of previous segment
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # If we have more than one segment, move the first segment to current head 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check to see if head is too close to a segment
    for segment in segments:
        if segment.distance(head) < 20:
            lose_game()
            break

    time.sleep(delay)


wn.mainloop()
