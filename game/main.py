import pygame
import random
import math

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Backgrond
background = pygame.image.load('spaceshadow.png')

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('space.png')
pygame.display.set_icon(icon)

score = 0

#Player
playerImg = pygame.image.load('fuser.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png')) 
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(3)
    enemyY_change.append(40)

#bullet
bulletImg = pygame.image.load('bulletfeu.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10 
bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 42)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score : "+ str(score_value), True, (255,255,255))
    screen.blit(score,(x, y))

#Fire -> the bullet is currently moving
#Ready -> you can't see the bullet on the screen
def player(x,y):
    screen.blit(playerImg,(x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#Game Loop
running = True
while running:

     #RGB color
   # screen.fill((70,30,240))

    #Background
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    #if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        print("A keystoke is pressed")
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        if event.key == pygame.K_RSHIFT:
            if bullet_state is "ready":
                #Get the current cordinate of the spaceship
                bulletX = playerX
                fire_bullet(bulletX,bulletY)   

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
    # 5 = 5 + -0.1 -> 5 = 5 - 0.1  
    # 5 = 5 + 0.1    

    # Checking for boundaries of spaceship so it doesn't go out of bound
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    #enemy Movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]    
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

    #Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score)
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)


    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()