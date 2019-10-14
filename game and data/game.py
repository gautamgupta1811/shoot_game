import random
import pygame
from pygame.locals import *
import time
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))

#white = 255, 255, 255
#red = 255, 0, 0
#yellow = 255, 255, 0

gunPointer = pygame.image.load('aim_pointer.png')
gunPointerWidth = gunPointer.get_width()
gunPointerHeight = gunPointer.get_height()

gun = pygame.image.load("gun.png")
gunWidth = gun.get_width()
gunHeight = gun.get_height()
gunY = height - gunHeight

zombie1 = pygame.image.load("zombie_1.gif")
zombie2 = pygame.image.load("zombie_2.png")
zombie3 = pygame.image.load("zombie_3.png")
zombie4 = pygame.image.load("zombie_4.png")
zombies = [zombie1, zombie2, zombie3, zombie4]

gunFire = pygame.mixer.Sound("gun fire.wav")
winSound = pygame.mixer.Sound("Ta Da.wav")



def homescreen():
    background = pygame.image.load("home_background.jpg")
    background = pygame.transform.scale(background,(width,height))
    #bg_sound = pygame.mixer.Sound("creepy-background.wav")
    #bg_sound.play()
    screen.blit(background, (0, 0))
    font = pygame.font.Font("font_1.ttf", 80)
    font1 = pygame.font.Font("font_1.ttf", 30)
    text1 = font1.render("KILL ATLEAST 20 ZOMBIES FOR NEXT LEVEL ", True, yellow)
    text2 = font1.render("USE MOUSE TO CONTROL THE GUN", True, yellow)
    text = font.render("PRESS SPACE TO START THE GAME", True, yellow)
    screen.blit(text, (50,10))
    screen.blit(text1, (50, 90))
    screen.blit(text2, (50, 130))
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bg_sound.stop()
                    level1()

            pygame.display.update()
def timer(seconds):


    font = pygame.font.Font("font_1.ttf", 30)
    if seconds > 0:
        text = font.render("Time Left: {}".format(seconds), True, yellow)
    else:
        text = font.render("Time Left: 0", True, yellow)
    screen.blit(text, (400, 10))



def score(counter):
    font = pygame.font.Font("font_1.ttf",30)
    text = font.render("Score: {}".format(counter), True, yellow)
    screen.blit(text, (10, 10))


def bloodPatch(posx, posy):
    bloodPatchImg = pygame.image.load("zombie_blood.png")
    bloodWidth = bloodPatchImg.get_width()
    bloodHeight = bloodPatchImg.get_height()
    while True:
        screen.blit(bloodPatchImg, (posx - bloodWidth/2, posy-bloodHeight/2))
        pygame.display.update()
        time.sleep(0.1)
        break


def nextLevel():
    winSound.play()
    font = pygame.font.Font("font_1.ttf", 100)
    text = font.render("LEVEL COMPLETED", True, yellow)
    screen.blit(text, (width/2 - 400, height/2-50))
    pygame.display.update()
    time.sleep(5)


def win():
    winSound.play()
    font = pygame.font.Font("font_1.ttf", 100)
    text = font.render("YOU WIN", True, yellow)
    screen.blit(text, (width / 2, height / 2 - 50))
    pygame.display.update()
    time.sleep(5)

def gameover():
        gameover_sound = pygame.mixer.Sound("music_1.wav")
        gameover_sound.play()
        font = pygame.font.Font("font_1.ttf", 100)
        text = font.render("Game Over", True, yellow)
        screen.blit(text, (width/2 - 200, height/2-50))
        pygame.display.update()
        time.sleep(5)


def level3():

    zombiesList =[]
    zombiesX = []
    zombiesY = []
    zombies_rect = []

    for i in range(2):
        zombiesImages = random.choice(zombies)
        zombiesList.append(zombiesImages)
        zombieWidth = zombiesImages.get_width()
        zombieHeight = zombiesImages.get_height()
        zombieX = random.randint(0, width - zombieWidth)
        zombiesX.append(zombieX)
        zombieY = random.randint(0, height - zombieHeight)
        zombiesY.append(zombieY)
        zombie_rect = pygame.Rect(zombiesX[i], zombiesY[i], zombieWidth, zombieHeight)
        zombies_rect.append((zombie_rect))




    background = pygame.image.load("final war.jpg")
    background = pygame.transform.scale(background, (width, height))

    count = 0

    pygame.time.set_timer(USEREVENT, 1000)
    seconds = 20
    while True:
        screen.fill(white)
        posX, posY = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        for i in range(2):
            screen.blit(zombiesList[i], (zombiesX[i], zombiesY[i]))

        screen.blit(gun, (posX, gunY))
        screen.blit(gunPointer, (posX - gunPointerWidth / 2, posY - gunPointerHeight / 2))
        gunPointer_rect = pygame.Rect(posX - gunPointerWidth / 2, posY - gunPointerHeight / 2, gunPointerWidth,
                                      gunPointerHeight)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                gunFire.play()


                for i in range(2):
                    if gunPointer_rect.colliderect(zombies_rect[i]):
                        bloodPatch(zombiesX[i] + zombieWidth / 2, zombiesY[i] + zombieHeight / 2)

                        del zombiesList[i]
                        zombiesImages = random.choice(zombies)
                        zombiesList.append(zombiesImages)
                        zombieWidth = zombiesImages.get_width()
                        zombieHeight = zombiesImages.get_height()
                        del zombiesX[i]
                        zombieX = random.randint(0, width - zombieWidth)
                        zombiesX.append(zombieX)
                        del zombiesY[i]
                        zombieY = random.randint(0, height - zombieHeight)
                        zombiesY.append(zombieY)
                        del zombies_rect[i]
                        zombie_rect = pygame.Rect(zombiesX[i], zombiesY[i], zombieWidth, zombieHeight)
                        zombies_rect.append((zombie_rect))
                        count += 1





        score(count)
        timer(seconds)
        if seconds < 0:
            if count > 20:
                win()
                homescreen()
            else:
                gameover()
                homescreen()
        pygame.display.update()

def level2():

    zombiesImages = random.choice(zombies)
    zombieWidth = zombiesImages.get_width()
    zombieHeight = zombiesImages.get_height()
    zombieX = random.randint(0, width - zombieWidth)
    zombieY = random.randint(0, height - zombieHeight)


    background = pygame.image.load("level_2.jpg")
    background = pygame.transform.scale(background, (width, height))


    pygame.time.set_timer(USEREVENT, 1000)


    flag = True

    seconds = 20
    count = 0

    while True:
        flag1 = True
        screen.fill(white)
        posX, posY = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        screen.blit(zombiesImages, (zombieX, zombieY))
        zombie_rect = pygame.Rect(zombieX, zombieY, zombieWidth, zombieHeight)
        screen.blit(gun, (posX, gunY))
        screen.blit(gunPointer, (posX - gunPointerWidth / 2, posY - gunPointerHeight / 2))
        gunPointer_rect = pygame.Rect(posX - gunPointerWidth / 2, posY - gunPointerHeight / 2, gunPointerWidth,
                                      gunPointerHeight)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                gunFire.play()
                if gunPointer_rect.colliderect(zombie_rect):
                        if flag == True:
                            zombieY = zombieY - 75
                            bloodPatch(zombieX + zombieWidth / 2, zombieY + zombieHeight / 2)
                            count += 1
                            flag = False
                            flag1 = False
                        if flag1 == True:
                            bloodPatch(zombieX + zombieWidth / 2, zombieY + zombieHeight / 2)
                            zombiesImages = random.choice(zombies)
                            zombieWidth = zombiesImages.get_width()
                            zombieHeight = zombiesImages.get_height()
                            zombieX = random.randint(0, width - zombieWidth)
                            zombieY = random.randint(0, height - zombieHeight)
                            count += 1
                            flag = True




        score(count)
        timer(seconds)
        if seconds < 0:
            if count > 20:
                nextLevel()
                level3()
            else:
                gameover()
                homescreen()
        pygame.display.update()




def level1():

    zombiesImages = random.choice(zombies)
    zombieWidth = zombiesImages.get_width()
    zombieHeight = zombiesImages.get_height()
    zombieX = random.randint(0, width - zombieWidth)
    zombieY = random.randint(0, height - zombieHeight)



    background = pygame.image.load("level_1.png")
    gunFire = pygame.mixer.Sound("gun fire.wav")
    count = 0

    pygame.time.set_timer(USEREVENT, 1000)
    seconds = 20
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                gunFire.play()
                if gunPointer_rect.colliderect(zombie_rect):
                    bloodPatch(zombieX+zombieWidth/2, zombieY+zombieHeight/2)
                    zombiesImages = random.choice(zombies)
                    zombieWidth = zombiesImages.get_width()
                    zombieHeight = zombiesImages.get_height()
                    zombieX = random.randint(0, width - zombieWidth)
                    zombieY = random.randint(0, height - zombieHeight)
                    count += 1


        screen.fill(white)
        posX, posY = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        screen.blit(zombiesImages, (zombieX, zombieY))
        zombie_rect = pygame.Rect(zombieX, zombieY, zombieWidth, zombieHeight)
        screen.blit(gun, (posX, gunY))
        screen.blit(gunPointer, (posX - gunPointerWidth / 2, posY - gunPointerHeight / 2))
        gunPointer_rect = pygame.Rect(posX - gunPointerWidth / 2, posY - gunPointerHeight / 2, gunPointerWidth, gunPointerHeight)
        score(count)
        timer(seconds)
        if seconds < 0:
            if count > 20:
                nextLevel()
                level2()

            else:
                gameover()
                homescreen()



        pygame.display.update()
homescreen()
