# PONG V2.0: hit the ball with the paddle
# By Simon Guo & Jesse Zhao
# Wed, Jan 13, 2016
# computer science project

import pygame
import sys
import string
import pygame.mixer
from pygame.locals import *
from random import *

# always need to init first thing
pygame.init()

#set score output document
fileOut = open("Score.txt","w")

# create a 720p window
screen = pygame.display.set_mode((720,480),0,32)
# ask for screen's width and height
size = width, height = screen.get_size()

# turn on the cursor, so you can control your mouse to close tab
pygame.mouse.set_visible(True)

# turn on key repeating (repeat 40 times per second)
pygame.key.set_repeat(25, 25)

#define function random_background
def random_background():
    #use RGB color
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    bgcolor = (red,green,blue)
    screen.fill(bgcolor)
    return bgcolor

# paddle constants
paddle_width = 22
paddle_length = 100
paddle_radius = paddle_length / 2
paddle_color = (250, 250, 250)
step = 8  # paddle moves 8 pixels at a go

# ball constants
ball_color = (250, 250, 250)
ball_radius = 25
ball_speed_1 = 3
ball_speed_2 = 4
bounce_time = 0 # the time the ball bounce 

#starting value for RGB value for the colorful screen in the game 
Background_Red = 0 
Background_Green = 0
Background_Blue = 0

#font constants
fsize = 48
font = pygame.font.Font("Minecraft.ttf", fsize)

#text information
Title = 'INSTRUCTION'
To_play = 'Press SPACE to PLAY'
How_play_1 = 'Move the bar by'
How_play_2 = 'pressing UP & DOWN'
How_play_3 = 'Try to hit the ball'
To_quit = 'Press ESC to QUIT'

INSTRUCTION = font.render(Title, True, (250, 250, 250))
PLAY = font.render(To_play, True, (250, 250, 250))
Content_1 = font.render(How_play_1, True, (250, 250, 250))
Content_2 = font.render(How_play_2, True, (250, 250, 250))
Content_3 = font.render(How_play_3, True, (250, 250, 250))
QUIT = font.render(To_quit, True, (250, 250, 250))

pygame.mixer.music.load('Ball_Bounce-Popup_Pixels-172648817.wav')

def get_key():
  while True:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  if len(message) != 0:
    screen.blit(font.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 300, (screen.get_height() / 2) - 70))
  pygame.display.flip()

def ask(screen, question):
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while True:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      pygame.display.flip() #refresh 
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_ESCAPE:
      sys.exit()
    elif inkey < 128:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

def main():
  Name = str(ask(screen, "Name"))
  fileOut.write(Name)

#load image into the game, display for 3 seconds
img = pygame.image.load('IntroV2.png')
screen.blit(img,(0,0))
pygame.display.flip() #refresh 
pygame.time.delay(3000)

while True: #forever loop
    pygame.display.flip() #refresh 
    random_background()
    screen.blit(INSTRUCTION, (185, 60))
    screen.blit(PLAY, (120, 145))
    screen.blit(Content_1, (170, 210))
    screen.blit(Content_2, (140, 260))
    screen.blit(Content_3, (170, 310))
    screen.blit(QUIT, (150, 380))
    pygame.time.delay(1500)

    for idle_event in pygame.event.get():
        if idle_event.type == QUIT:
            sys.exit()

        #escape when press esc
        if idle_event.type == KEYDOWN:
            if idle_event.key == K_ESCAPE:
                sys.exit()

            if idle_event.key == 32:  # play game when space key is pressed
                random_background()
                # start the paddle in the center
                paddle_location = height / 2

                # number of the ball when started
                balls = 4

                while balls > 0: #case #1, there is still life left
                    
                    ball_position = [ball_radius, ball_radius]
                    #set ball speed
                    ball_mvect = [randint(ball_speed_1, ball_speed_2), randint(ball_speed_1, ball_speed_2)]
                    ball_limit = size 
                    balls = balls - 1 #lost a life

                    while ball_position[0] + ball_radius < ball_limit[0]:  # still alive

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                sys.exit()

                            #if press esc during the game
                            elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    sys.exit()
                                # press up to move up
                                elif event.key == 273 \
                                    or event.key == 265 \
                                    or event.key == 264:  # up
                                    paddle_location = paddle_location - step
                                # press down to move down
                                elif event.key == 274 \
                                    or event.key == 259 \
                                    or event.key == 258:  # down
                                    paddle_location = paddle_location + step

                        # make sure the paddle is in-bounds
                        if paddle_location - paddle_radius < 0:
                            paddle_location = paddle_radius
                        elif paddle_location + paddle_radius >= height:
                            paddle_location = height - 1 - paddle_radius
                        
                        #show score
                        Score = font.render("Score:", 1, (255,255,255))
                        screen.blit(Score, (280, 10))
                        #get bounce time and change it to string to display
                        Score_number = Score = font.render(str(bounce_time), 1, (255,255,255))
                        screen.blit(Score_number, (440, 10))
                        #life = balls + 1, because in pong 1.0, it does not count the ball you are playing with
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
                        
                        #keep the screen in a colorful background until the ball hit the paddle
                        screen.fill((Background_Red,Background_Green,Background_Blue))

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
                                #ball become faster
                                ball_speed_1 = ball_speed_1 + 1
                                ball_speed_2 = ball_speed_2 + 1
            
                            #bounce on the paddle
                            elif i == 0 \
                                and ball_position[i] >= ball_limit[i] - ball_radius - paddle_width \
                                and ball_position[1] > paddle_location - paddle_radius \
                                and ball_position[1] < paddle_location + paddle_radius:
                                ball_position[i] = ball_limit[i] - ball_radius - paddle_width - 1
                                ball_mvect[i] = (-1) * ball_mvect[i]
                                step = step + 0.2 # the paddle will be faster
                                bounce_time = bounce_time + 1 #bounce_time + 1, score + 1
                                #choose background color again after it hits the paddle
                                Background_Red = randint(0,254) 
                                Background_Green = randint(0,254)
                                Background_Blue = randint(0,254)
                                pygame.mixer.music.play(-1, 0.0)
                
                if balls == 0: #case when player have no life anymore
                    bounce_time = 0 #reset the bounce_time(score) to zero
                    #fill screen with black color
                    screen.fill((0,0,0))
                    #show game over on screen
                    Game_Over = font.render("Game Over",True,(250,250,250))
                    screen.blit(Game_Over,(220,200))
                    pygame.display.flip() #refresh 
                    pygame.time.wait(2000)
                    

                    #show your score is in Score.txt
                    screen.fill((0,0,0))   
                    
                    Your_Score = font.render("Your Score is in Score.txt",True,(250,250,250))
                    screen.blit(Your_Score,(70,300))
                    Put_Name = font.render("Please type your Name",True,(250,250,250))
                    screen.blit(Put_Name,(70,100))
                    pygame.display.flip() #refresh 
                    if __name__ == '__main__': main()
                    pygame.time.wait(2000)

                    #change bounce time to string, in order to write it to output
                    fileOut.write(" ")
                    fileOut.write(str(bounce_time))
                    
                    
                    
                    



                    





                
                            


                        

            
             
                         

                                
                                
                               


                            



                               
