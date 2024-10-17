# customSnake.py by Johnathon Wilt for programming I final project
# Custom snake game, snake does not grow like traditional game but instead snake gets faster each time it eats the apple
from graphics import *
import random
import time

# Creates the starting window
def makeWin():
    win = GraphWin("Modified Snake Game", 700, 600)
    win.setBackground("black")
    scoreboard = Rectangle(Point(0, 600), Point(700, 550))
    scoreboard.setFill("purple")
    scoreboard.draw(win)
    return win

# Refreshes the new score, will be called every time apple eaten
def updateScore(win, score):
    if score < 10:
        scoreText = Text(Point(600, 578), f"SCORE: 00{score}")
    elif score > 9 and score < 100:
        scoreText = Text(Point(600, 578), f"SCORE: 0{score}")
    elif score > 99:
        scoreText = Text(Point(600, 578), f"SCORE: {score}")
        
    scoreText.setSize(20)
    scoreText.draw(win)

    return scoreText

# Creates a new apple 20 pixels wide/tall; Generates x and y coordinates and ensures they are divisible by 20 using %
def drawApple(win, score):
    appleX = random.randint(0, 680)
    appleY = random.randint(0, 530)
    while appleX % 20 != 0:
        appleX = random.randint(0, 680)

    while appleY % 20 != 0:
        appleY = random.randint(0, 530)

    apple = Rectangle(Point(appleX, appleY), Point(appleX + 20, appleY + 20))
    apple.setFill("red")
    apple.draw(win)

    return appleX, appleY

# Draws the snake cube
def drawHead(win):
    head = Rectangle(Point(320, 240), Point(340, 260))
    head.setFill("green")
    head.draw(win)
    headX = 320
    headY = 240
    return headX, headY

# Moves the snake
def moveSnake(win, direction, headX, headY):
    # oldHead erases the previous block
    oldHead = Rectangle(Point(headX, headY), Point(headX + 20, headY + 20))
    oldHead.setFill("black")
    oldHead.draw(win)

    # Moves head position 20 pixels in whichever direction
    if direction == "Right":
        headX += 20
    elif direction == "Left":
        headX -= 20     
    elif direction == "Up":
        headY -= 20     
    else:
        headY += 20

    # Draws head
    head = Rectangle(Point(headX, headY), Point(headX + 20, headY + 20))
    head.setFill("green")
    head.draw(win)
    return headX, headY

def main():
    win = makeWin()
    score = 0
    speed = 0.1

    # Set up starting function
    startText = Text(Point(350, 578), f"CLICK TO START")
    startText.setSize(20)
    startText.draw(win)
    startText = win.getMouse()
    # For some reason, could not figure out how to undraw startText. So I made this "cover"
    cover = Rectangle(Point(0, 600), Point(700, 550)) 
    cover.setFill("purple")
    cover.draw(win)

    # Create scoring
    scoreText = updateScore(win, score)
    # Create head of snake
    headX, headY = drawHead(win)
    # Draw apple
    locAppleX, locAppleY = drawApple(win, score)
    direction = "Right"  # Initial direction

    while True:
        # Checks which key is being pressed, snake responds
        key = win.checkKey()
        if key in ["Right", "Left", "Up", "Down"]:
            direction = key

        headX, headY = moveSnake(win, direction, headX, headY)
        time.sleep(speed)  
        
        # Checking if snake has hit wall, if so = death
        if headX < 0 or headX > 680 or headY < 0 or headY > 525:
            gameover = Text(Point(340, 265), "GAME OVER")
            gameover.setSize(30)
            gameover.setTextColor("white")
            gameover.draw(win)
            break
        
        # Checking if snake head is touching apple, if so = score + 10
        if headX == locAppleX and headY == locAppleY:
            score += 10
            scoreText.undraw()
            scoreText = updateScore(win, score)
            locAppleX, locAppleY = drawApple(win, score)
            speed = speed / 1.15
            
    win.getMouse()
    win.close()

main()