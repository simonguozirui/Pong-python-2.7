# pong: hit the ball with the paddle
#
# use the escape key to exit
#
# on the XO, the escape key is the top lefthand key,
# circle with an x in it.

#import pippy
import pygame
import sys
import pygame.mixer
from pygame.locals import *
from random import *



# always need to init first thing
pygame.init()

# create the window and keep track of the surface
# for drawing INTRO
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen=pygame.display.set_mode((720,480),0,32)

#if idle_event.key == K_F:
 #  screen01 = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#else:
 #  screen=pygame.display.set_mode((720,480),0,32)




# ask for screen's width and height
size = width, height = screen.get_size()

# turn off the cursor
pygame.mouse.set_visible(True)

# turn on key repeating (repeat 40 times per second)
pygame.key.set_repeat(25, 25)

def random_background():

    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    bgcolor = (red,green,blue)
    screen.fill(bgcolor)
    return bgcolor


# paddle constants
paddle_speed = 4
paddle_width = 30
paddle_length = 130
paddle_radius = paddle_length / 2
paddle_color = (250, 250, 250)
step = paddle_speed  # paddle moves 3 pixels at a go

# ball constants


#ball_color = (250, 250, 250)

def random_ballcolor():

    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    ball_color = (red,green,blue)
    return ball_color


ball_radius = 20

img = pygame.image.load('LOGO.png')
screen.blit(img,(0,0))
pygame.time.delay(2000)
# game constants
fsize = 30
msg = 'Press \'g\' to start game, Press \'p\' to pause game'

font = pygame.font.Font(None, fsize)
text = font.render(msg, True, (250, 250, 250))
textRect = text.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery

while True:#replace "while pippy.pygame.next_frame():" with "while True:" 
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    ball_color = (red,green,blue)
    # display msg
    random_background()
    pygame.time.delay(2000)
    screen.blit(text, textRect)
    pygame.display.flip()

    # chill until a key is pressed
    for idle_event in pygame.event.get():
        if idle_event.type == QUIT:
            sys.exit()

        if idle_event.type == KEYDOWN:
            if idle_event.key == K_ESCAPE:
                sys.exit()

            if idle_event.key == 103:  # g key
                #if idle_event.key == 112:  # P key
                    #while True:
                        #event = pygame.event.wait()
                            #if idle_event.key == 112:  # P key
                               # break
                #else :
                # play a game!
                screen.fill((0,0,0))

                
                # start the paddle in the center
                paddle_location = height / 2

                # number of balls to a game
                balls = 5

                while balls > 0:
                    

                    ball_position = [ball_radius, ball_radius]
                    ball_mvect = [randint(3, 5), randint(3, 5)]
                    ball_limit = size
                    balls = balls - 1

                    while ball_position[0] + ball_radius < ball_limit[0]:  # in play

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                sys.exit()

                            elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    sys.exit()
                                elif event.key == 273 \
                                    or event.key == 265 \
                                    or event.key == 264:  # up
                                    paddle_location = paddle_location - step
                                elif event.key == 274 \
                                    or event.key == 259 \
                                    or event.key == 258:  # down
                                    paddle_location = paddle_location + step

                        # make sure the paddle is in-bounds
                        if paddle_location - paddle_radius < 0:
                            paddle_location = paddle_radius
                        elif paddle_location + paddle_radius >= height:
                            paddle_location = height - 1 - paddle_radius

                        # clear the screen
                        screen.fill((0,0,0))


                        # draw the paddle on the right side of the screen
                        pygame.draw.line(screen,
                                        paddle_color,
                                        (width - paddle_width, paddle_location -
                                        paddle_radius),
                                        (width - paddle_width,
                                        paddle_location + paddle_radius),
                                        paddle_width)

                        # draw the ball
                        pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

                        # draw the unused balls
                        for i in range(balls):
                            pygame.draw.circle(screen, ball_color,
                                 (int(round(30 + i * ball_radius * 2.4)), 30),
                                 ball_radius)

                        # update the display
                        pygame.display.flip()

                        # update the ball
                        for i in range(2):
                            ball_position[i] = ball_position[i] + ball_mvect[i]
                        

                            # bounce on top and left
                            if ball_position[i] < ball_radius:
                                ball_position[i] = ball_radius
                                ball_mvect[i] = -1 * ball_mvect[i]

                                #pygame.mixer.music.load('Bounce.mp3')
                                #pygame.mixer.music.play(0)
                            # bounce on bottom
                            elif i == 1 \
                                and ball_position[i] >= ball_limit[i] - ball_radius:
                                ball_position[i] = ball_limit[i] - ball_radius - 1
                                ball_mvect[i] = -1 * ball_mvect[i]
                            elif i == 0 \
                                and ball_position[i] >= ball_limit[i] - ball_radius - paddle_width \
                                and ball_position[1] > paddle_location - paddle_radius \
                                and ball_position[1] < paddle_location + paddle_radius:
                                
                                ball_position[i] = ball_limit[i] - ball_radius - paddle_width - 1
                                ball_mvect[i] = (-1) * ball_mvect[i]
                                
                                paddle_speed = paddle_speed + 10


                                


