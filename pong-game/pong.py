import turtle

# Create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Set up game screen
turtle.setp(400, 300)
turtle.bgcolor("black")

# Left paddle (1)
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("purple")
paddle1.shapesize(stretch_wid=5, stretch_len=1) # Makes paddle wider
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0

# Right paddle (2)
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("green")
paddle2.shapesize(stretch_wid=5, stretch_len=1) # Makes paddle wider
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0

# Game rules
game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_points": 3,
    "ball_speed": 3
}

# Score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Helvetica", 24, "normal"))


# GAME MECHANICS

paddle1.sety(paddle1.ycor() + paddle1.dy)
paddle2.sety(paddle2.ycor() + paddle2.dy)
ball.setx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)

# Checks for game over conditions
if points["player1"] == game_rules["max_points"]:
    game_over = True
    winner = "player1"
elif points["player2"] == game_rules["max_points"]:
    game_over = True
    winner = "player2"

# Checks for ball collision with paddles
if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
    ball.setx(340)
    ball.dx *= -1
elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
    ball.setx(-340)
    ball.dx *= -1

# Check for ball going offscreen
if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    points["player1"] += 1
elif ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    points["player2"] += 1

# Check for ball colliding with top/bottom of screen
if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
elif ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

# Update score display
score_display.clear()
score_display.write("Player 1: {}  Player 2: {}".format(points["player1"], points["player2"]), align="center", font=("Helvetica", 24, "normal"))

# Logic to move paddles
def paddle1_up():
    paddle1.dy = 10
def paddle1_down():
    paddle1.dy = -10

def paddle2_up():
    paddle2.dy = 10
def paddle2_down():
    paddle2.dy = -10

# Keybindings
turtle.listen()
turtle.onkeypress(paddle1_up, "w")
turtle.onkeypress(paddle1_down, "s")
turtle.onkeypress(paddle2_up, "Up")
turtle.onkeypress(paddle2_down, "Down")

# Game over screen display
game_over_display = turtle.Turtle()
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)
game_over_display.write("Game over: {} wins!".format(winner), align="center", font=("Helvetica", 36, "normal"))