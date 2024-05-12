import random
import time
import pygame
from pygame import mixer

pygame.init()
mixer.init()
mixer.music.load('destroyBreakSound.wav')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bar_Game")
clock = pygame.time.Clock()

# Defining Game Variables
fps = 150
speed = [2, 2]
running = True
didTheyPressSpace = False
gameOverOrNot = False

font = pygame.font.Font('freesansbold.ttf', 64)

scoreCounter = 0
aGiftHasTouchedTheBar = False
cancelCollisionBetweenBallAndBricks = False
isItSLow = False
aCurseHasTouchedTheBar = False
flashyOrNot = False
flashyBarColors = ['black', 'red']

barSize = 150
barX = 600
barY = 500
bar = pygame.Rect(barX, barY, 150, 20)
start = time.perf_counter()  # constant
barChangeX = 0

ballMainScreenI = pygame.image.load('ballMainScreen.png')
ballMainScreenI = pygame.transform.scale(ballMainScreenI, (100, 100))
ballMainScreen = ballMainScreenI.get_rect()

ball = pygame.image.load('finalBall.png')
ball = pygame.transform.scale(ball, (15, 15))
ballCircle = ball.get_rect()
ballCircle.update(450, 300, ball.get_width(), ball.get_height())

curseI = pygame.image.load('curse.png')
curse = curseI.get_rect()
curse.update(700, 240, curseI.get_width(), curseI.get_height())

giftI = pygame.image.load('giftbox.png')
gift = giftI.get_rect()
gift.update(300, 240, giftI.get_width(), giftI.get_height())

youWon = font.render('You Won', True, 'red')
textRectYouWon = youWon.get_rect()
textRectYouWon.center = (800 // 2, 200)

gameOver = font.render('Game Over',True, 'red')
textRectGameOver = gameOver.get_rect()
textRectGameOver.center = (800 // 2, 200)

brickBreaker = font.render('Brick Breaker', True, 'black', 'sky blue')
textRectForbrickBreaker = brickBreaker.get_rect()
textRectForbrickBreaker.center = (800 // 2, 200)

startGame = font.render('Press Space To Start', True, 'black', 'sky blue')
textRectForStartGame = startGame.get_rect()
textRectForStartGame.center = (800 // 2, 400)

# Creating and rendering bricks in Main Screen
def createBricksInMain():
    brickInMain = []
    for i in range(15): #column
        for j in range(8): #row
            brick = pygame.Rect(j * 100 + 1, i * 40 + 1, 100, 40)
            brickInMain.append(brick)
    return brickInMain

randomColorMainScreen = [(0, 0, 255)
    , (0, 0, 240)
    , (0, 0, 230)
    , (0, 0, 220)
    , (0, 0, 210)
    , (0, 0, 200)
    , (0, 0, 190)
    , (0, 0, 180)
]

bricksInMain = createBricksInMain()

def brickPainterInMain():
    for brick in bricksInMain:
        pygame.draw.rect(screen, randomColorMainScreen[random.randint(0, 7)], brick)

            
def brickCollisionDetectorInMain():
    for brick in bricksInMain:
        if brick.clip(ballMainScreen):
            pygame.draw.rect(screen, randomColor[random.randint(0, 9)], brick)
                        
# Creating and rendering bricks in Game Screen
def createBricksInGame():
    bricks = []
    for i in range(7): #col
        for j in range(8): #row
            brick = pygame.Rect(j * 100 + 1, i * 40 + 1, 95, 30)
            bricks.append(brick)
    return bricks

randomColor = ['blue', 'yellow', 'green', 'cyan', 'grey', 'orange', 'brown', 'white', 'purple', 'pink']
# how about choosing the way the bricks are arranged
# sugar collector game
bricks = createBricksInGame()

def brickPainter():
    colorIndexer = 0
    for brick in bricks:
        pygame.draw.rect(screen, randomColor[colorIndexer], brick)
        colorIndexer += 1
        if colorIndexer == 9:
            colorIndexer = 0

# The Bar Movement System
def barMovement(x, y, flashyOrNotArgs):
    if flashyOrNotArgs: # [red , black]
        global barSize
        barSize = 150 // 2
        pygame.draw.rect(screen, random.choice(flashyBarColors), bar, 1)
        bar.update(x, y, barSize, 10)
    else:
        pygame.draw.rect(screen, 'red', bar)
        bar.update(x, y, barSize, 10)

# The Reward and Punishment System
def giftSlider():
    if gift.y != 600:
        gift.update(gift.x, gift.y + 1, 10, 10)
    else:
        gift.y = 240
        gift.x = random.randint(50, 750)

def gifted():
    if bar.colliderect(gift):
        global aGiftHasTouchedTheBar
        aGiftHasTouchedTheBar = True
        global cancelCollisionBetweenBallAndBricks
        cancelCollisionBetweenBallAndBricks = True
        # global enlargeBar
        print('gift')

def curseSlider():
    if curse.y != 600:
        curse.update(curse.x, curse.y + 1, 10, 10)
    else:
        curse.y = 260
        curse.x = random.randint(50, 750)

def cursed():
    if bar.colliderect(curse):
        global aCurseHasTouchedTheBar
        aCurseHasTouchedTheBar = True
        print('curse')
        global fps
        fps = 20
        global isItSLow
        isItSLow = True
        global flashyOrNot
        flashyOrNot = True

# The Collision Detection System
def didTheBallHitTheBar():  # if the ball hit the bar or bricks
    # the bouncing direction of the ball is determined according to the real break out
    if bar.colliderect(ballCircle):
        if bar.topleft[0] <= ballCircle.centerx <= bar.midtop[0] - 30:  # how about from left to 3/4 the bar
            # left side of the bar
            speed[0] = -2 
            speed[1] = -speed[1]
            print(bar.topleft[0])
            # print('X-->  ', speed[0])
        elif bar.midtop[0] + 30 <= ballCircle.centerx <= bar.topright[0]:
            # left side of the bar
            speed[0] = 2
            speed[1] = -speed[1]
            print(bar.topleft[0])
            # print('X-->  ', speed[0])
        elif bar.midtop[0] - 30 <= ballCircle.centerx <= bar.midtop[0] + 30:
            speed[0] = 0
            speed[1] = -speed[1]
            # print('X-->  ', speed[0])

def iWouldLikeToDeleteSomeBricksCuzOfCollision():
    for index, brick in enumerate(bricks):
        if brick.colliderect(ballCircle):
            mixer.music.play()
            del bricks[index]
            global scoreCounter
            scoreCounter += 1
            if not cancelCollisionBetweenBallAndBricks:
                speed[1] = -speed[1]  # if it really hit the brick reverse the direction of the ball

# Resetting the Game
def restartGame():
    global bricks, scoreCounter, gameOverOrNot, ballCircle , bar ,timeLimit
    scoreCounter = 0
    gameOverOrNot = False
    screen.fill((0, 0, 0))
    ballCircle.update(450, 300, ball.get_width(), ball.get_height())
    bar = pygame.Rect(barX, barY, 150, 20)
    bricks = createBricksInGame()
    timeLimit = 0;

# The Main Loop
while running:
    if not didTheyPressSpace:
        clock.tick(150)
        screen.fill((0, 0, 0))
        brickPainterInMain()
        brickCollisionDetectorInMain()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    didTheyPressSpace = True
                    barChangeX = 0
      
        if ballMainScreen.left < 0 or ballMainScreen.right > 800:
            speed[0] = -speed[0]

        if ballMainScreen.top < 0 or ballMainScreen.bottom > 600:
            speed[1] = -speed[1]

        ballMainScreen = ballMainScreen.move(speed)
        screen.blit(ballMainScreenI, ballMainScreen)
        screen.blit(brickBreaker, textRectForbrickBreaker)
        screen.blit(startGame, textRectForStartGame)
    else: # In Game                                               
        end = time.perf_counter()
        timeLimit = end - start
        if aCurseHasTouchedTheBar and timeLimit > 6:
            print(timeLimit)
            fps = 150
            isItSLow = False
            flashyOrNot = False
            # mixer.music.stop()
            aCurseHasTouchedTheBar = False
            barSize = 150
            start = end
        if aGiftHasTouchedTheBar and timeLimit > 4:
            cancelCollisionBetweenBallAndBricks = False
            aGiftHasTouchedTheBar = False
            # enlargeBar = True
            start = end

        clock.tick(fps)
        screen.fill((0, 0, 0))
        brickPainter()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not aCurseHasTouchedTheBar:
                if event.key == pygame.K_LEFT:
                    barChangeX = -5
                if event.key == pygame.K_RIGHT:
                    barChangeX = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    barChangeX = 0
            elif event.type == pygame.KEYDOWN and aCurseHasTouchedTheBar:
                if event.key == pygame.K_LEFT:
                    barChangeX = +5
                if event.key == pygame.K_RIGHT:
                    barChangeX = -5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        barChangeX = 0
            elif event.type == pygame.KEYDOWN and gameOverOrNot:
                if event.key == pygame.K_r:
                    restartGame()
        barX += barChangeX
        # Preventing the bar from going out of the screen
        if barSize == 150:
            if barX <= 5:
                barX = 5
            elif barX >= 645:
                barX = 645
        else: # bar is cursed and its size is reduced
            if barX <= 5:
                barX = 5
            elif barX >= 720:
                barX = 720

        if ballCircle.left < 0 or ballCircle.right > 800:
            speed[0] = -speed[0]

        if ballCircle.top < 0:
            speed[1] = -speed[1]

        if not gameOverOrNot:
            iWouldLikeToDeleteSomeBricksCuzOfCollision()
            curseSlider()
            cursed()
            giftSlider()
            gifted()
            didTheBallHitTheBar()

        font = pygame.font.Font('freesansbold.ttf', 20)
        textVar = 'Score ' + str(scoreCounter)
        score = font.render(str(textVar), True, (255, 0, 0, 255))
        textRectScore = score.get_rect()
        textRectScore.center = (41, 590)

        ballCircle = ballCircle.move(speed)
        screen.blit(ball, ballCircle)

        # You Win??
        if len(bricks) == 0:
            screen.fill('black')
            screen.blit(youWon, textRectYouWon)
            gameOverOrNot = True
        # Game Over??
        if ballCircle.bottom > 600 :
            gameOverOrNot = True
            screen.fill('black')
            screen.blit(gameOver, textRectGameOver)

        screen.blit(score, textRectScore)
        if not aGiftHasTouchedTheBar and ballCircle.bottom < 600 and not gameOverOrNot and len(bricks) != 0:
            screen.blit(giftI, gift)
        if not aCurseHasTouchedTheBar and ballCircle.bottom < 600 and not gameOverOrNot and len(bricks) != 0:
            screen.blit(curseI, curse)
        if not gameOverOrNot and len(bricks) != 0:
            barMovement(barX, barY, flashyOrNot)
    pygame.display.update()