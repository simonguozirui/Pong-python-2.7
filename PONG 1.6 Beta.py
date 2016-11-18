# pong: hit the ball with the paddle
#
# use the escape key to exit
#
# on the XO, the escape key is the top lefthand key,
# circle with an x in it.

#import pippy
import pygame
import sys
from pygame.locals import *
from random import *

# always need to init first thing
pygame.init()

# create the window and keep track of the surface
# for drawing into
screen = pygame.display.set_mode((720,480),0,32)
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
paddle_width = 20
paddle_length = 100
paddle_radius = paddle_length / 2
paddle_color = (250, 250, 250)
step = 6  # paddle moves 3 pixels at a go

# ball constants
ball_color = (250, 250, 250)
ball_radius = 25
ball_speed_1 = 3
ball_speed_2 = 4

bounce_time = 0

Background_Red = 0
Background_Green = 0
Background_Blue = 0

# game constants
fsize = 48

Title = 'INSTRUCTION'
To_play = 'Press SPACE to PLAY'
How_play_1 = 'Move the bar by'
How_play_2 = 'pressing UP & DOWN'
How_play_3 = 'Try to hit the ball'
To_quit = 'Press ESC to QUIT'

font = pygame.font.Font("Minecraft.ttf", fsize)

INSTRUCTION = font.render(Title, True, (250, 250, 250))
PLAY = font.render(To_play, True, (250, 250, 250))
Content_1 = font.render(How_play_1, True, (250, 250, 250))
Content_2 = font.render(How_play_2, True, (250, 250, 250))
Content_3 = font.render(How_play_3, True, (250, 250, 250))
QUIT = font.render(To_quit, True, (250, 250, 250))

while True: #pippy.pygame.next_frame():

    pygame.display.flip()
    random_background()
    screen.blit(INSTRUCTION, (185, 60))
    screen.blit(PLAY, (120, 145))
    screen.blit(Content_1, (170, 210))
    screen.blit(Content_2, (140, 260))
    screen.blit(Content_3, (170, 310))
    screen.blit(QUIT, (150, 380))
    pygame.time.delay(1500)
    # chill until a key is pressed
    for idle_event in pygame.event.get():
        if idle_event.type == QUIT:
            sys.exit()

        if idle_event.type == KEYDOWN:
            if idle_event.key == K_ESCAPE:
                sys.exit()

            if idle_event.key == 32:  # space key

                # play a game!

                # start the paddle in the center
                paddle_location = height / 2

                # number of balls to a game
                balls = 4



                while balls > 0:
                    
                    ball_position = [ball_radius, ball_radius]
                    ball_mvect = [randint(ball_speed_1, ball_speed_2), randint(ball_speed_1, ball_speed_2)]
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
                        
                        

                        Score = font.render("Score:", 1, (255,255,255))
                        screen.blit(Score, (280, 10))

                        Score_number = Score = font.render(str(bounce_time), 1, (255,255,255))
                        screen.blit(Score_number, (440, 10))

                        Life = font.render(str(balls + 1), 1, (255,255,255))
                        screen.blit(Life, (190, 10))

                
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
                        
                        screen.fill((Background_Red,Background_Green,Background_Blue))
                        # clear the screen


                        # update the ball
                        for i in range(2):
                            ball_position[i] = ball_position[i] + ball_mvect[i]

                            # bounce on top and left
                            if ball_position[i] < ball_radius:
                                ball_position[i] = ball_radius
                                ball_mvect[i] = -1 * ball_mvect[i]


                            # bounce on bottom
                            elif i == 1 \
                                and ball_position[i] >= ball_limit[i] - ball_radius:
                                ball_position[i] = ball_limit[i] - ball_radius - 1
                                ball_mvect[i] = -1 * ball_mvect[i]
                                ball_speed_1 = ball_speed_1 + 1
                                ball_speed_2 = ball_speed_2 + 1


                            elif i == 0 \
                                and ball_position[i] >= ball_limit[i] - ball_radius - paddle_width \
                                and ball_position[1] > paddle_location - paddle_radius \
                                and ball_position[1] < paddle_location + paddle_radius:
                                ball_position[i] = ball_limit[i] - ball_radius - paddle_width - 1
                                ball_mvect[i] = (-1) * ball_mvect[i]
                                step = step + 0.2
                                bounce_time = bounce_time + 1
                                Background_Red = randint(0,254)
                                Background_Green = randint(0,254)
                                Background_Blue = randint(0,254)
                                
                        # clear the screen

                                
                                
                               


                            



                               
