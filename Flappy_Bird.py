import pyttsx3 as py
from random import randint

"""

This game is a clone of the Famous mobile game 'Flappy Bird'.\n
In this game, The bird flaps and tries to evade the pipes.\n
The game is endless, once you reach certain scores, the game will speed up and get tougher!\n
To flap, you can 'click' or tap on 'spacebar' / 'Enter' / 'upward arrow' keys.\n
Enjoy the game! Press 'A' to play.

"""

WIDTH = 700 
HEIGHT = 600
game_over = False
score = 0
bird_crash = False
speak = False

bird = Actor("bird")
pole1 = Actor("pole1")
pole2 = Actor("pole2")
pole3 = Actor("pole3")
pole4 = Actor("pole4")
pole5 = Actor("pole5")
pole6 = Actor("pole6")

def reset_game():
    global bird, pole1, pole2, pole3, pole4,game_over,score, speak
    game_over = False
    score = 0
    speak = False

    bird.pos = 100, 120
    pole1.pos = 350, 520
    pole2.pos = 350, -20
    pole3.pos = 500, 500
    pole4.pos = 500, -50
    pole5.pos = 650, 600
    pole6.pos = 650, 50

reset_game()

def draw():
    global score
    screen.clear()

    if game_over:  
        score = int(score)     
        screen.fill("red")
        screen.draw.text(f"GAME OVER! Your Score is {score}!", color = "white", center = ((WIDTH/2)-10, (HEIGHT/2)-100), fontsize = (60))
        screen.draw.text("Press 'A' to Play Again. \n Press 'Escape' to exit.", color =  "white", center = (WIDTH/2, HEIGHT/2), fontsize = (40))

    else:
        screen.fill("lightblue")
        screen.blit("flappybg", (0, 0))
        bird.draw()
        pole1.draw()
        pole2.draw()
        pole3.draw()
        pole4.draw()
        pole5.draw()
        pole6.draw()
        screen.draw.text("Score: " + str(int(score)), color = "black", topleft = (10, 0))

def crash():
    global game_over
    game_over = True

def update():
    global bird_crash
    global game_over
    global score
    global speak

    a,b = pole1.pos
    c,d = pole2.pos
    e,f = pole3.pos
    g,h = pole4.pos
    i,j = pole5.pos
    k,l = pole6.pos

    if score < 107:
        pole1.pos = a - 2, b
        pole2.pos = c - 2, d
        pole3.pos = e - 2, f
        pole4.pos = g - 2, h
        pole5.pos = i - 2, j
        pole6.pos = k - 2, l

        x, y = bird.pos
        bird.pos = x, y + 2.5

        if keyboard.space or keyboard.RETURN or keyboard.up:
            bird.y = bird.y-4

    if pole1.x < 0:
        gap_y = randint(150, HEIGHT - 150)
        pole1.y = gap_y + 300
        pole2.y = gap_y - 300
        pole1.x = WIDTH + 350
        pole2.x = WIDTH + 350

    if pole3.x < -10:
        gap_y = randint(150, HEIGHT - 150)
        pole3.y = gap_y + 300
        pole4.y = gap_y - 300
        pole3.x = WIDTH + 500
        pole4.x = WIDTH + 500

    if pole5.x < -15:
        gap_y = randint(150, HEIGHT - 150)
        pole5.y = gap_y + 300
        pole6.y = gap_y - 300
        pole5.x = WIDTH + 650
        pole6.x = WIDTH + 650

    elif score >= 107:
        pole1.pos = a - 3, b
        pole2.pos = c - 3, d
        pole3.pos = e - 3, f
        pole4.pos = g - 3, h
        pole5.pos = i - 3, j
        pole6.pos = k - 3, l

        x, y = bird.pos
        bird.pos = x, y + 2.75

        if keyboard.space or keyboard.RETURN or keyboard.up:
           bird.y=bird.y-5

    if pole1.x < 0:
        gap_y = randint(150, HEIGHT - 150)
        pole1.y = gap_y + 275
        pole2.y = gap_y - 275
        pole1.x = WIDTH + 450
        pole2.x = WIDTH + 450

    if pole3.x < -10:
        gap_y = randint(150, HEIGHT - 150)
        pole3.y = gap_y + 275
        pole4.y = gap_y - 275
        pole3.x = WIDTH + 500
        pole4.x = WIDTH + 500

    if pole5.x < -15:
        gap_y = randint(150, HEIGHT - 150)
        pole5.y = gap_y + 275
        pole6.y = gap_y - 275
        pole5.x = WIDTH + 550
        pole6.x = WIDTH + 550

    elif score >= 210:
        pole1.pos = a - 4, b
        pole2.pos = c - 4, d
        pole3.pos = e - 4, f
        pole4.pos = g - 4, h
        pole5.pos = i - 4, j
        pole6.pos = k - 4, l

        x, y = bird.pos
        bird.pos = x, y + 3.25

        if keyboard.space or keyboard.RETURN or keyboard.up:
           bird.y = bird.y-6

    if pole1.x < 0:
        gap_y = randint(150, HEIGHT - 150)
        pole1.y = gap_y + 250
        pole2.y = gap_y - 250
        pole1.x = WIDTH + 350
        pole2.x = WIDTH + 350

    if pole3.x < -10:
        gap_y = randint(150, HEIGHT - 150)
        pole3.y = gap_y + 250
        pole4.y = gap_y - 250
        pole3.x = WIDTH + 400
        pole4.x = WIDTH + 400

    if pole5.x < -15:
        gap_y = randint(150, HEIGHT - 150)
        pole5.y = gap_y + 250
        pole6.y = gap_y - 250
        pole5.x = WIDTH + 450
        pole6.x = WIDTH + 450


    if pole1.pos and pole2.pos < bird.pos:
        score += 1/6.6

    if pole3.pos and pole4.pos < bird.pos:
        score += 1/6.6

    if pole5.pos and pole6.pos < bird.pos:
        score += 1/6.6

    if bird.y <= 0 or bird.y >= HEIGHT:
        crash()

    bird_crash = bird.colliderect(pole1) or bird.colliderect(pole2) or \
    bird.colliderect(pole3) or bird.colliderect(pole4) or \
    bird.colliderect(pole5) or bird.colliderect(pole6)

    if bird_crash:
        crash()
        
    if game_over and keyboard.a:
        reset_game()

    if game_over and not speak:
        voice()
        speak = True

def voice():
        engine=py.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(f"Game Over! Your score is {int(score)}")
        engine.runAndWait()
        return()

def on_key_down(key):
    if game_over and key == keys.ESCAPE:
        exit()