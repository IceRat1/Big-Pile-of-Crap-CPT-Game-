# Game where you control mario or luigi, shooting enemies coming from the top side of the screen. 
# Enemies get progressively harder (different types + increasing spawn rate)
# You can find better weapons and power-ups
# When a player dies, they are able to shoot fireballs from the grave to try and stop the other player
# Player with the most points when both players die is the winner

# To-do: 
# Finish enemies
# Add hit detection for both enemies + bullets, and enemies + players.
# Add power-up and weapons spawns. Integrate power-ups (HP up, speed up, fire rate up, 2x points, invincibility)
# Properly finish background and SFX
# Add music and sound effects

# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random

pygame.init()

WIDTH = 960
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

def drawbullet(x, y, bullettype):
    if bullettype == "normal":
        screen.blit(normalbullet, (x-10, y))
    if bullettype == "machine":
        screen.blit(machinebullet, (x-5,y))
    if bullettype == "shotgun" or bullettype == "shotgun1" or bullettype == "shotgun2":
        screen.blit(shotgunbullet, (x-7.5,y))
    if bullettype == "rocket":
        screen.blit(rocketbullet, (x-20, y))

def drawenemy(x,y,enemytype, direction):
    if enemytype == "goomba":
        screen.blit(goomba, (x-30, y))
    if enemytype == "koopa":
        screen.blit(koopa, (x-30, y))
    if enemytype == "shyguy" and direction == "right":
        screen.blit(shyguy, (x-30, y))
    if enemytype == "shyguy" and direction == "left":
        screen.blit(shyguyleft, (x-30, y))
    if enemytype == "boo":
        screen.blit(boo, (x-30, y))


        



ticks = 0

char1_x = 200
char1_y = 200
char1direction = "right"
char1_speed = 5
bullet1_speed = 5
bulletreload1 = 1
bullettype1 = "shotgun"

char2_x = 200
char2_y = 200
char2direction = "right"
char2_speed = 5
bullet2_speed = 5
bulletreload2 = 1
bullettype2 = "rocket"

bullets1 = [] #format: [x, y, bullettype]
bullets2 = [] #format: [x, y, bullettype]

bulletreloads = {"normal": 20, "machine": 5, "shotgun": 30, "rocket": 40}
bulletspeeds = {"normal": 15, "machine": 10, "shotgun": 10, "shotgun1": 10, "shotgun2": 10, "rocket": 5}
bulletdamages = {"normal": 10, "machine": 10, "shotgun": 10, "rocket": 10}

enemies = [] #format: [x, y, HP, enemytype, direction]

currentenemytypes = ["goomba", "goomba", "goomba", "goomba", "goomba"]

enemyhp = {"goomba": 10, "koopa": 30, "shyguy": 10, "bomb-omb": 15, "boo": 20, "bowser": 50}

enemyspawnchance = 35

marioimg = pygame.image.load("mario.png")
mario = pygame.transform.scale(marioimg, (80, 120))
luigiimg = pygame.image.load("luigi.png")
luigi = pygame.transform.scale(luigiimg, (80, 120))
normalbulletimg = pygame.image.load("fireball.png")
normalbullet = pygame.transform.scale(normalbulletimg, (20, 20))
machinebulletimg = pygame.image.load("machinebullet.png")
machinebullet = pygame.transform.scale(machinebulletimg, (10, 20))
shotgunimg = pygame.image.load("shotgun.png")
shotgunbullet = pygame.transform.scale(shotgunimg, (15, 15))
rocketimg = pygame.image.load("bulletbill.png")
rocketbullet = pygame.transform.scale(rocketimg, (60, 40))
rocketbullet = pygame.transform.rotate(rocketbullet, 90)
goombaimg = pygame.image.load("goomba.png")
goomba = pygame.transform.scale(goombaimg, (60,60))
koopaimg = pygame.image.load("koopa.png")
koopa = pygame.transform.scale(koopaimg, (60,80))
booimg = pygame.image.load("boo.png")
boo = pygame.transform.scale(booimg, (60,60))
shyguyimg = pygame.image.load("shyguy.png")
shyguy = pygame.transform.scale(shyguyimg, (60,60))
shyguyleft = pygame.transform.flip(shyguy, True, False)


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] == True and char1_x > 0:
        char1_x -= char1_speed
        if char1direction == "right":
            mario = pygame.transform.flip(mario, True, False)
            char1direction = "left"
    if keys[pygame.K_d] == True and char1_x < WIDTH:
        char1_x += char1_speed
        if char1direction == "left":
            mario = pygame.transform.flip(mario, True, False)
            char1direction = "right"
    if keys[pygame.K_w] == True and char1_y > 0:
        char1_y -= char1_speed
    if keys[pygame.K_s] == True and char1_y < HEIGHT:
        char1_y += char1_speed
    if keys[pygame.K_LEFT] == True and char2_x > 0:
        char2_x -= char2_speed
        if char2direction == "right":
            luigi = pygame.transform.flip(luigi, True, False)
            char2direction = "left"
    if keys[pygame.K_RIGHT] == True and char2_x < WIDTH:
        char2_x += char2_speed
        if char2direction == "left":
            luigi = pygame.transform.flip(luigi, True, False)
            char2direction = "right"
    if keys[pygame.K_UP] == True and char2_y > 0:
        char2_y -= char2_speed
    if keys[pygame.K_DOWN] == True and char2_y < HEIGHT:
        char2_y += char2_speed
                

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    ticks += 1
    bulletreload1 -= 1
    bulletreload2 -= 1

    if bulletreload1 == 0:
        bullets1.append([char1_x, char1_y, bullettype1])
        bulletreload1 = bulletreloads[bullettype1]
        if bullettype1 == "shotgun":
            bullets1.append([char1_x + 10, char1_y, "shotgun1"])
            bullets1.append([char1_x - 10, char1_y, "shotgun2"])

    if bulletreload2 == 0:
        bullets2.append([char2_x, char2_y, bullettype2])
        bulletreload2 = bulletreloads[bullettype2]
        if bullettype2 == "shotgun":
            bullets2.append([char2_x + 10, char2_y, "shotgun1"])
            bullets2.append([char2_x - 10, char2_y, "shotgun2"])
    

    if ticks == 300:
        currentenemytypes.append("koopa")
        enemyspawnchance = 40
    elif ticks == 600:
        currentenemytypes.extend(["koopa","koopa"])
        enemyspawnchance = 35
    elif ticks == 900:
        currentenemytypes.extend(["koopa", "koopa" "shyguy"])
        enemyspawnchance = 30
    elif ticks == 1200:
        currentenemytypes.extend(["koopa", "shyguy", "shyguy"])
        enemyspawnchance = 25
    elif ticks == 1500:
        currentenemytypes.extend(["shyguy", "shyguy", "boo"])
        enemyspawnchance = 20
    elif ticks == 1800:
        currentenemytypes.extend(["shyguy", "boo", "boo"])
        enemyspawnchance = 15
    elif ticks == 2100:
        currentenemytypes.extend(["boo","boo", "bomb-omb"])
        enemyspawnchance = 10
    elif ticks == 2400:
        currentenemytypes.extend(["boo", "bomb-omb","bomb-omb"])
    elif ticks == 2700:
        currentenemytypes.extend(["bomb-omb", "bomb-omb", "bowser"])
    elif ticks == 3000:
        currentenemytypes.extend(["bomb-omb", "bowser", "bowser", "bowser"])
    elif ticks == 4000:
        currentenemytypes.extend(["bowser","bowser","bowser"])
    elif ticks == 5400:
        currentenemytypes = ["bowser"]

    if random.randrange(0,enemyspawnchance + len(enemies)*2) == 0:
        enemytype = currentenemytypes[random.randrange(0,len(currentenemytypes))]
        enemies.append([random.randrange(0,WIDTH), 0, enemyhp[enemytype], enemytype, random.choice(["left", "right"])])



    # DRAWING

    screen.fill((255, 255, 255))

    

    # pygame.draw.circle(screen, (0, 0, 255), (char1_x, char1_y), 30)
    # pygame.draw.circle(screen, (0, 255, 0), (char2_x, char2_y), 30)

    for bullet in bullets1:
        #format: [x, y, bullettype]
        drawbullet(bullet[0], bullet[1], bullet[2])
        bullet[1] -= bulletspeeds[bullet[2]]
        if bullet[2] == "shotgun1":
            bullet[0] += 1
        elif bullet[2] == "shotgun2":
            bullet[0] -= 1
        if bullet[1] < 0:
            bullets1.remove(bullet)


    for bullet in bullets2:
        #format: [x, y, bullettype]
        drawbullet(bullet[0], bullet[1], bullet[2])
        bullet[1] -= bulletspeeds[bullet[2]]
        if bullet[2] == "shotgun1":
            bullet[0] += 1
        elif bullet[2] == "shotgun2":
            bullet[0] -= 1
        if bullet[1] < -100:
            bullets2.remove(bullet)
    screen.blit(mario, (char1_x-40, char1_y))
    screen.blit(luigi, (char2_x-40, char2_y))

    for enemy in enemies:
        #format: [x, y, hp, enemytype, direction (if enemy moves left to right)]
        drawenemy(enemy[0], enemy[1], enemy[3], enemy[4])
        if enemy[3] == "goomba":
            enemy[1] += 3
        elif enemy[3] == "koopa":
            enemy[1] += (20-(enemy[2]//2))
        elif enemy[3] == "shyguy":
            enemy[1] += 2
            if enemy[4] == "right":
                enemy[0] += 3
                if enemy[0] > WIDTH:
                    enemy[4] = "left"
            elif enemy[4] == "left":
                enemy[0] -= 3
                if enemy[0] < 0:
                    enemy[4] = "right"

            # runs in the same direction as a player
        elif enemy[3] == "boo":
            enemy[1] += 2
            enemy[0] += random.randrange(-20,20)


        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
    print(ticks)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
