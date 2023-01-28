import random
import time

import pygame
from pygame import mixer

pygame.init()
mixer.init()
mixer.music.load('destroyBreakSound.wav')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bar_Game")

ballMainScreenI = pygame.image.load('ballMainScreen.png')
ballMainScreenI = pygame.transform.scale(ballMainScreenI, (100, 100))
ballMainScreen = ballMainScreenI.get_rect()

ball = pygame.image.load('finalBall.png')
ball = pygame.transform.scale(ball, (20, 20))
ballCircle = ball.get_rect()
# the initial position of the ball
ballCircle.update(600, 400, ball.get_width(), ball.get_height())

curseI = pygame.image.load('curse.png')
curse = curseI.get_rect()
curse.update(200, 240, curseI.get_width(), curseI.get_height())

giftI = pygame.image.load('giftbox.png')
gift = giftI.get_rect()
gift.update(300, 240, giftI.get_width(), giftI.get_height())

speedForBall = [2, 2]
speedForBallInMainScreen = [5, 5]

barX = 600
barY = 500
barWidth = 150
bar = pygame.Rect(barX, barY, 150, 20)
barChangeX = 0

clock = pygame.time.Clock()
fps = 150
scoreCounter = 0
running = True
########################################################################################################################
# bricks of the main screen
# first row
b1 = pygame.Rect(1, 1, 100, 40)
b2 = pygame.Rect(101, 1, 100, 40)
b3 = pygame.Rect(201, 1, 100, 40)
b4 = pygame.Rect(301, 1, 100, 40)
b5 = pygame.Rect(401, 1, 100, 40)
b6 = pygame.Rect(501, 1, 100, 40)
b7 = pygame.Rect(601, 1, 100, 40)
b8 = pygame.Rect(701, 1, 100, 40)
# second row
b9 = pygame.Rect(1, 41, 100, 40)
b10 = pygame.Rect(101, 41, 100, 40)
b11 = pygame.Rect(201, 41, 100, 40)
b12 = pygame.Rect(301, 41, 100, 40)
b13 = pygame.Rect(401, 41, 100, 40)
b14 = pygame.Rect(501, 41, 100, 40)
b15 = pygame.Rect(601, 41, 100, 40)
b16 = pygame.Rect(701, 41, 100, 40)
# third row
b17 = pygame.Rect(1, 81, 100, 40)
b18 = pygame.Rect(101, 81, 100, 40)
b19 = pygame.Rect(201, 81, 100, 40)
b20 = pygame.Rect(301, 81, 100, 40)
b21 = pygame.Rect(401, 81, 100, 40)
b22 = pygame.Rect(501, 81, 100, 40)
b23 = pygame.Rect(601, 81, 100, 40)
b24 = pygame.Rect(701, 81, 100, 40)
# fourth row
b25 = pygame.Rect(1, 121, 100, 40)
b26 = pygame.Rect(101, 121, 100, 40)
b27 = pygame.Rect(201, 121, 100, 40)
b28 = pygame.Rect(301, 121, 100, 40)
b29 = pygame.Rect(401, 121, 100, 40)
b30 = pygame.Rect(501, 121, 100, 40)
b31 = pygame.Rect(601, 121, 100, 40)
b32 = pygame.Rect(701, 121, 100, 40)
# fifth row
b33 = pygame.Rect(1, 161, 100, 40)
b34 = pygame.Rect(101, 161, 100, 40)
b35 = pygame.Rect(201, 161, 100, 40)
b36 = pygame.Rect(301, 161, 100, 40)
b37 = pygame.Rect(401, 161, 100, 40)
b38 = pygame.Rect(501, 161, 100, 40)
b39 = pygame.Rect(601, 161, 100, 40)
b40 = pygame.Rect(701, 161, 100, 40)
# sixth row
b41 = pygame.Rect(1, 201, 100, 40)
b42 = pygame.Rect(101, 201, 100, 40)
b43 = pygame.Rect(201, 201, 100, 40)
b44 = pygame.Rect(301, 201, 100, 40)
b45 = pygame.Rect(401, 201, 100, 40)
b46 = pygame.Rect(501, 201, 100, 40)
b47 = pygame.Rect(601, 201, 100, 40)
b48 = pygame.Rect(701, 201, 100, 40)
# seventh row
b49 = pygame.Rect(1, 241, 100, 40)
b50 = pygame.Rect(101, 241, 100, 40)
b51 = pygame.Rect(201, 241, 100, 40)
b52 = pygame.Rect(301, 241, 100, 40)
b53 = pygame.Rect(401, 241, 100, 40)
b54 = pygame.Rect(501, 241, 100, 40)
b55 = pygame.Rect(601, 241, 100, 40)
b56 = pygame.Rect(701, 241, 100, 40)
# eighth row
b57 = pygame.Rect(1, 281, 100, 40)
b58 = pygame.Rect(101, 281, 100, 40)
b59 = pygame.Rect(201, 281, 100, 40)
b60 = pygame.Rect(301, 281, 100, 40)
b61 = pygame.Rect(401, 281, 100, 40)
b62 = pygame.Rect(501, 281, 100, 40)
b63 = pygame.Rect(601, 281, 100, 40)
b64 = pygame.Rect(701, 281, 100, 40)
# ninth row
b65 = pygame.Rect(1, 321, 100, 40)
b66 = pygame.Rect(101, 321, 100, 40)
b67 = pygame.Rect(201, 321, 100, 40)
b68 = pygame.Rect(301, 321, 100, 40)
b69 = pygame.Rect(401, 321, 100, 40)
b70 = pygame.Rect(501, 321, 100, 40)
b71 = pygame.Rect(601, 321, 100, 40)
b72 = pygame.Rect(701, 321, 100, 40)
# tenth row
b73 = pygame.Rect(1, 361, 100, 40)
b74 = pygame.Rect(101, 361, 100, 40)
b75 = pygame.Rect(201, 361, 100, 40)
b76 = pygame.Rect(301, 361, 100, 40)
b77 = pygame.Rect(401, 361, 100, 40)
b78 = pygame.Rect(501, 361, 100, 40)
b79 = pygame.Rect(601, 361, 100, 40)
b80 = pygame.Rect(701, 361, 100, 40)
# eleventh row
b81 = pygame.Rect(1, 401, 100, 40)
b82 = pygame.Rect(101, 401, 100, 40)
b83 = pygame.Rect(201, 401, 100, 40)
b84 = pygame.Rect(301, 401, 100, 40)
b85 = pygame.Rect(401, 401, 100, 40)
b86 = pygame.Rect(501, 401, 100, 40)
b87 = pygame.Rect(601, 401, 100, 40)
b88 = pygame.Rect(701, 401, 100, 40)
# twelfth  row
b89 = pygame.Rect(1, 441, 100, 40)
b90 = pygame.Rect(101, 441, 100, 40)
b91 = pygame.Rect(201, 441, 100, 40)
b92 = pygame.Rect(301, 441, 100, 40)
b93 = pygame.Rect(401, 441, 100, 40)
b94 = pygame.Rect(501, 441, 100, 40)
b95 = pygame.Rect(601, 441, 100, 40)
b96 = pygame.Rect(701, 441, 100, 40)
# thirteenth  row
b97 = pygame.Rect(1, 481, 100, 40)
b98 = pygame.Rect(101, 481, 100, 40)
b99 = pygame.Rect(201, 481, 100, 40)
b100 = pygame.Rect(301, 481, 100, 40)
b101 = pygame.Rect(401, 481, 100, 40)
b102 = pygame.Rect(501, 481, 100, 40)
b103 = pygame.Rect(601, 481, 100, 40)
b104 = pygame.Rect(701, 481, 100, 40)
# fourteenth  row
b105 = pygame.Rect(1, 521, 100, 40)
b106 = pygame.Rect(101, 521, 100, 40)
b107 = pygame.Rect(201, 521, 100, 40)
b108 = pygame.Rect(301, 521, 100, 40)
b109 = pygame.Rect(401, 521, 100, 40)
b110 = pygame.Rect(501, 521, 100, 40)
b111 = pygame.Rect(601, 521, 100, 40)
b112 = pygame.Rect(701, 521, 100, 40)
# fifteenth  row
b113 = pygame.Rect(1, 561, 100, 40)
b114 = pygame.Rect(101, 561, 100, 40)
b115 = pygame.Rect(201, 561, 100, 40)
b116 = pygame.Rect(301, 561, 100, 40)
b117 = pygame.Rect(401, 561, 100, 40)
b118 = pygame.Rect(501, 561, 100, 40)
b119 = pygame.Rect(601, 561, 100, 40)
b120 = pygame.Rect(701, 561, 100, 40)

randomColorMainScreen = [(0, 0, 255)
    , (0, 0, 240)
    , (0, 0, 230)
    , (0, 0, 220)
    , (0, 0, 210)
    , (0, 0, 200)
    , (0, 0, 190)
    , (0, 0, 180)]

bricksInMain = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20,
                b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38,
                b39, b40, b41, b42, b43, b44, b45, b46, b47, b48, b49, b50, b51, b52, b53, b54, b55, b56,
                b57, b58, b59, b60, b61, b62, b63, b64, b65, b66, b67, b68, b69, b70, b71, b72, b73, b74,
                b75, b76, b77, b78, b79, b80, b81, b82, b83, b84, b85, b86, b87, b88, b89, b90, b91, b92,
                b93, b94, b95, b96, b97, b98, b99, b100, b101, b102, b103, b104, b105, b106, b107, b108,
                b109, b110, b111, b112, b113, b114, b115, b116, b117, b118, b119, b120]
########################################################################################################################
# bricks of the game
# first row
brick00 = pygame.Rect(1, 1, 100, 40)
brick01 = pygame.Rect(101, 1, 100, 40)
brick02 = pygame.Rect(201, 1, 100, 40)
brick03 = pygame.Rect(301, 1, 100, 40)
brick04 = pygame.Rect(401, 1, 100, 40)
brick05 = pygame.Rect(501, 1, 100, 40)
brick06 = pygame.Rect(601, 1, 100, 40)
brick07 = pygame.Rect(701, 1, 100, 40)
# second row
brick10 = pygame.Rect(1, 41, 100, 40)
brick11 = pygame.Rect(101, 41, 100, 40)
brick12 = pygame.Rect(201, 41, 100, 40)
brick13 = pygame.Rect(301, 41, 100, 40)
brick14 = pygame.Rect(401, 41, 100, 40)
brick15 = pygame.Rect(501, 41, 100, 40)
brick16 = pygame.Rect(601, 41, 100, 40)
brick17 = pygame.Rect(701, 41, 100, 40)
# third row
brick20 = pygame.Rect(1, 81, 100, 40)
brick21 = pygame.Rect(101, 81, 100, 40)
brick22 = pygame.Rect(201, 81, 100, 40)
brick23 = pygame.Rect(301, 81, 100, 40)
brick24 = pygame.Rect(401, 81, 100, 40)
brick25 = pygame.Rect(501, 81, 100, 40)
brick26 = pygame.Rect(601, 81, 100, 40)
brick27 = pygame.Rect(701, 81, 100, 40)
# fourth row
brick30 = pygame.Rect(1, 121, 100, 40)
brick31 = pygame.Rect(101, 121, 100, 40)
brick32 = pygame.Rect(201, 121, 100, 40)
brick33 = pygame.Rect(301, 121, 100, 40)
brick34 = pygame.Rect(401, 121, 100, 40)
brick35 = pygame.Rect(501, 121, 100, 40)
brick36 = pygame.Rect(601, 121, 100, 40)
brick37 = pygame.Rect(701, 121, 100, 40)
# fifth row
brick40 = pygame.Rect(1, 161, 100, 40)
brick41 = pygame.Rect(101, 161, 100, 40)
brick42 = pygame.Rect(201, 161, 100, 40)
brick43 = pygame.Rect(301, 161, 100, 40)
brick44 = pygame.Rect(401, 161, 100, 40)
brick45 = pygame.Rect(501, 161, 100, 40)
brick46 = pygame.Rect(601, 161, 100, 40)
brick47 = pygame.Rect(701, 161, 100, 40)
# sixth row
brick50 = pygame.Rect(1, 201, 100, 40)
brick51 = pygame.Rect(101, 201, 100, 40)
brick52 = pygame.Rect(201, 201, 100, 40)
brick53 = pygame.Rect(301, 201, 100, 40)
brick54 = pygame.Rect(401, 201, 100, 40)
brick55 = pygame.Rect(501, 201, 100, 40)
brick56 = pygame.Rect(601, 201, 100, 40)
brick57 = pygame.Rect(701, 201, 100, 40)

randomColor = ['blue', 'yellow', 'green', 'cyan', 'grey', 'orange', 'brown', 'white', 'purple', 'pink']

bricks = [brick00, brick01, brick02, brick03, brick04, brick05, brick06, brick07
    , brick10, brick11, brick12, brick13, brick14, brick15, brick16, brick17
    , brick20, brick21, brick22, brick23, brick24, brick25, brick26, brick27
    , brick30, brick31, brick32, brick33, brick34, brick35, brick36, brick37
    , brick40, brick41, brick42, brick43, brick44, brick45, brick46, brick47
    , brick50, brick51, brick52, brick53, brick54, brick55, brick56, brick57]


def brickPainterForMain():
    colorIndexer = 0
    for brick in bricksInMain:
        pygame.draw.rect(screen, randomColorMainScreen[random.randint(0, 7)], brick, 0)
        colorIndexer += 1
        if colorIndexer == 8:  # resetting it to zero
            colorIndexer = 0


def brickCollisionDetector():
    for brick in bricksInMain:
        if brick.clip(ballMainScreen):
            pygame.draw.rect(screen, randomColor[random.randint(0, 9)], brick)


def giftSlider():
    if gift.y != 600:
        gift.update(gift.x, gift.y + 1, 10, 10)
    else:
        gift.y = 240
        gift.x = random.randint(50, 750)


aGiftHasTouchedTheBar = False
cancelCollisionBetweenBarAndBricks = False


def gifted():
    if bar.colliderect(gift):
        global aGiftHasTouchedTheBar
        aGiftHasTouchedTheBar = True
        global cancelCollisionBetweenBarAndBricks
        cancelCollisionBetweenBarAndBricks = True


def curseSlider():
    if curse.y != 600:
        curse.update(curse.x, curse.y + 1, 10, 10)
    else:
        curse.y = 260
        curse.x = random.randint(50, 750)


flashyOrNot = False
isItSLow = False
aCurseHasTouchedTheBar = False


def cursed():
    if bar.colliderect(curse):
        global aCurseHasTouchedTheBar
        aCurseHasTouchedTheBar = True
        global fps
        fps = 20
        global isItSLow
        isItSLow = True
        global flashyOrNot
        flashyOrNot = True


def iWouldLikeToDeleteSomeBricksCuzOfCollision():
    for index, brick in enumerate(bricks):
        if brick.colliderect(ballCircle):
            mixer.music.play()
            del bricks[index]
            global scoreCounter
            scoreCounter += 1
            if not cancelCollisionBetweenBarAndBricks:
                speedForBall[1] = -speedForBall[1]  # if it really hit the brick reverse the direction of the ball


def brickPainterForGame():
    colorIndexer = 0
    for brick in bricks:
        pygame.draw.rect(screen, randomColor[colorIndexer], brick, 0)
        colorIndexer += 1
        if colorIndexer == 9:
            colorIndexer = 0


flashyBarColors = ['black', 'red']


def barMovement(x, flashyOrNotArgs):
    if flashyOrNotArgs:
        global barWidth
        barWidth = 150 // 2
        pygame.draw.rect(screen, random.choice(flashyBarColors), bar, 1)
        bar.update(x, 500, barWidth, 10)
    else:
        pygame.draw.rect(screen, 'red', bar)
        bar.update(x, 500, barWidth, 10)


def didTheBallHitTheBar():  # if the ball hit the bar or bricks
    # the bouncing direction of the ball is determined according to the real break out
    if bar.colliderect(ballCircle):
        if bar.topleft[0] <= ballCircle.centerx <= bar.midtop[0] - 30:
            # left side of the bar
            speedForBall[0] = -2
            speedForBall[1] = -speedForBall[1]
        elif bar.midtop[0] + 30 <= ballCircle.centerx <= bar.topright[0]:
            # left side of the bar
            speedForBall[0] = 2
            speedForBall[1] = -speedForBall[1]
        elif bar.midtop[0] - 30 <= ballCircle.centerx <= bar.midtop[0] + 30:
            # the middle portion of the bar reflects the ball Vertically
            speedForBall[0] = 0
            speedForBall[1] = -speedForBall[1]


font = pygame.font.Font('freesansbold.ttf', 64)
youWon = font.render('You Won', True, 'red')
textRectYouWon = youWon.get_rect()
textRectYouWon.center = (800 // 2, 200)

gameOver = font.render('Game Over', True, 'red')
textRectGameOver = gameOver.get_rect()
textRectGameOver.center = (800 // 2, 200)

brickBreaker = font.render('Brick Breaker', True, 'black', 'sky blue')
textRectForbrickBreaker = brickBreaker.get_rect()
textRectForbrickBreaker.center = (800 // 2, 200)

startGame = font.render('Press Space To Start', True, 'black', 'sky blue')
textRectForStartGame = startGame.get_rect()
textRectForStartGame.center = (800 // 2, 400)

didTheyPressSpace = False
gameOverorNot = False
start = time.perf_counter()

while running:
    screen.fill('black')
    clock.tick(fps)

    if not didTheyPressSpace:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    didTheyPressSpace = True

        # if the bigball in main screen did hit the borders reverse its direction
        if ballMainScreen.left < 0 or ballMainScreen.right > 800:
            speedForBallInMainScreen[0] = -speedForBallInMainScreen[0]

        if ballMainScreen.top < 0 or ballMainScreen.bottom > 600:
            speedForBallInMainScreen[1] = -speedForBallInMainScreen[1]

        brickPainterForMain()
        brickCollisionDetector()

        ballMainScreen = ballMainScreen.move(speedForBallInMainScreen)
        screen.blit(ballMainScreenI, ballMainScreen)
        screen.blit(brickBreaker, textRectForbrickBreaker)
        screen.blit(startGame, textRectForStartGame)
    else:
        end = time.perf_counter()
        timeLimit = end - start
        if aCurseHasTouchedTheBar and timeLimit > 6:
            fps = 150  # resetting fps to its original value after the curse has ended
            isItSLow = False
            flashyOrNot = False
            aCurseHasTouchedTheBar = False
            barWidth = 150
            start = end
        if aGiftHasTouchedTheBar and timeLimit > 4:
            cancelCollisionBetweenBarAndBricks = False
            aGiftHasTouchedTheBar = False
            start = end

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not aCurseHasTouchedTheBar:
                if event.key == pygame.K_LEFT:
                    barChangeX = -5
                if event.key == pygame.K_RIGHT:
                    barChangeX = 5
            #     reverse the direction of movement of the bar as a curse has occured
            elif event.type == pygame.KEYDOWN and aCurseHasTouchedTheBar:
                if event.key == pygame.K_LEFT:
                    barChangeX = +5
                if event.key == pygame.K_RIGHT:
                    barChangeX = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    barChangeX = 0

        barX += barChangeX
        if barWidth == 150:
            if barX <= 5:
                barX = 5
            elif barX >= 645:
                barX = 645
        else:  # when the bar is cursed it's width decreases thus it requires another border bar check
            if barX <= 5:
                barX = 5
            elif barX >= 720:
                barX = 720

        if ballCircle.left < 0 or ballCircle.right > 800:
            speedForBall[0] = -speedForBall[0]

        if ballCircle.top < 0:
            speedForBall[1] = -speedForBall[1]

        brickPainterForGame()
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

        ballCircle = ballCircle.move(speedForBall)
        screen.blit(ball, ballCircle)

        # You Win??
        if len(bricks) == 0:
            screen.fill('black')
            screen.blit(youWon, textRectYouWon)

        # Game Over??
        if ballCircle.bottom > 600 and len(bricks) != 0:
            gameOverorNot = True
            screen.fill('black')
            screen.blit(gameOver, textRectGameOver)

        screen.blit(score, textRectScore)
        if not aGiftHasTouchedTheBar and ballCircle.bottom < 600 and not gameOverorNot and len(bricks) != 0:
            screen.blit(giftI, gift)
        if not aCurseHasTouchedTheBar and ballCircle.bottom < 600 and not gameOverorNot and len(bricks) != 0:
            screen.blit(curseI, curse)
        if not gameOverorNot and len(bricks) != 0:
            barMovement(barX, flashyOrNot)
    pygame.display.update()