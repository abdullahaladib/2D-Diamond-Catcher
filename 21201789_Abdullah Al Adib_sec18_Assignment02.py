from time import sleep
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import os

diamond_speed = 2
box_x = -30
box_y = -300
d_x = 100
d_y = 260
coll = False
score = 0
color = (1.0,1.0,1.0)
over = False
play = True
box_speed = 20
cheat = False
max_dia_speed = 8
            
def find_zone(x,y):
    zone = 0
    if x == 0:
        if y > 0:
            zone = 1
        else:
            zone = 5

    if abs(x) > abs(y):
        if x>0 and y>0:
            zone = 0
        elif x>0 and y<0:
            zone = 7
        elif x<0 and y>0:
            zone = 3
        elif x<0 and y<0:
            zone = 4
    if abs(x) < abs(y):
        if x>0 and y>0:
            zone = 1
        elif x>0 and y<0:
            zone = 6
        elif x<0 and y>0:
            zone = 2
        elif x<0 and y<0:
            zone = 5
    
    return zone

def convert_between_zone0_and_zonex(mode, x, y, zone):
      if mode == True:
        if zone == 0:
                return [x,y]
        elif zone == 1:
                return [y,x]
        elif zone == 2:
                return [y,-x]
        elif zone == 3:
                return [-x,y]
        elif zone == 4:
                return [-x,-y]
        elif zone == 5:
                return [-y,-x]
        elif  zone == 6:
                return [-y, x]
        elif zone == 7:
                return [x,-y]
      else:
        if zone == 0:
             return [x,y]
        elif zone == 1:
                return [y,x]
        elif zone == 2:
                return [y,-x]
        elif zone == 3:
                return [-x,y]
        elif zone == 4:
                return [-x,-y]
        elif zone == 5:
                return [-y,-x]
        elif  zone == 6:
                return [y, -x]
        elif zone == 7:
                return [x,-y]
          
def mpl(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    zone = find_zone(dx, dy)
    x1,y1 = convert_between_zone0_and_zonex(True,x1,y1,zone)
    x2,y2 = convert_between_zone0_and_zonex(True,x2,y2,zone)
    dx = x2-x1
    dy = y2-y1
    d = (2*dy) - dx
    delNE = 2*(dy-dx)
    delE = 2*dy

    for x in range(x1,(x2+1)):
      draw_points(convert_between_zone0_and_zonex(False, x,y1,zone))
      if d>0:
           d += delNE
           y1 += 1
      else:
           d += delE  

def draw_points(lst):
    x,y=lst
    glPointSize(2)         
    glBegin(GL_POINTS)     
    glVertex2f(x, y)        
    glEnd()

def setup_projection():
    glViewport(0, 0, 500, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250.0, 250, -300.0, 300, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    glLoadIdentity()                                    
    setup_projection()
    if not play:
        draw_play()
    else:
        draw_pause()
    draw_box()
    draw_return()
                                     
    
    draw_cross()
    if not over:
        draw_diamond()                             
    glutSwapBuffers()  

def draw_cross():
    glColor3f(1.0, 0.0, 0.0)
    mpl(220,270,240,290)
    mpl(240,270,220,289)

def draw_pause():
    glColor3f(1.0,1.0,0.0)
    mpl(-5,270,-5,290)
    mpl(5,270,5,290)

def draw_play():
     glColor3f(1.0,1.0,0.0)
     mpl(-10,280,10,290)
     mpl(-10,280,10,270)
     mpl(10,270,10,290)

def draw_return():
    glColor3f(0.0,0.0,1.0)
    mpl(-240,280,-220,280)
    mpl(-240,280,-230,290)
    mpl(-240,279,-230,270)

def draw_diamond():
   
    global d_x, d_y

    glColor3f(1.0, 1.0, 0.0)
    mpl(d_x,d_y,d_x+10,d_y+15)
    mpl(d_x+10,d_y+15,d_x+20,d_y)
    mpl(d_x,d_y,d_x+10,d_y-15)
    mpl(d_x+20,d_y,d_x+10,d_y-15)

def draw_box():
     global box_x, box_y

     glColor3f(*color)
     mpl(box_x,box_y,box_x+60,box_y)
     mpl(box_x+59,box_y+1,box_x+80,box_y+20)
     mpl(box_x-20,box_y+20,box_x,box_y+1)
     mpl(box_x-20,box_y+20,box_x+80,box_y+20)
     

def animate():
    global d_x, d_y, diamond_speed, over, play
    if over == False and play:
        if cheat:
            check_collision()
            if d_y <= -280:
                d_x = random.randint(-230,230)
                d_y = 260
            d_y = d_y - diamond_speed
            cheat_mode()
        else:
            check_collision()
            if d_y <= -280:
                d_x = random.randint(-230,230)
                d_y = 260
            d_y = d_y - diamond_speed

    glutPostRedisplay()

def check_collision():
    global box_x, d_x, d_y, coll, score, color, over, play, diamond_speed, box_speed, max_dia_speed
    if ((box_x-20) < (d_x+10) < (box_x+80)) and (d_y <= -260):
        d_x = random.randint(-230,230)
        d_y = 260
        coll = True
        score += 1
        print("Score: ",score)
        if diamond_speed <= max_dia_speed:    
            diamond_speed += 1
    else:
        if d_y < -270:
            coll = False
            over = True
            color = (1.0,0.0,0.0)
            print("Game is over. Score: ", score)
    
def special_key_listener(key,x,y):
    global box_x, box_y, box_speed
    if not over:
        if key == GLUT_KEY_RIGHT and (box_x+80) <= 240:
            box_x += box_speed
        elif key == GLUT_KEY_LEFT and (box_x-20) >= -240:
            box_x -= box_speed
    glutPostRedisplay()

def reset_game():
    global diamond_speed, box_x, box_y, d_x, d_y, coll, score, color, over, play, box_speed, cheat
    diamond_speed = 1
    box_x = -30
    box_y = -300
    d_x = 100
    d_y = 260
    coll = False
    score = 0
    color = (1.0,1.0,1.0)
    over = False
    play = True
    box_speed = 10
    cheat = False

def mouseListener(button,state,x,y):
    global play
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and 240<x<260 and 10<y<30:
        play = not play

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and 470<x<490 and 10<y<30:
        glutDestroyWindow(wind)
        os._exit(0)
    
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and 10<x<30 and 10<y<30:
        reset_game()
        print("Starting Over.")

def cheat_mode():
    global d_x, box_x, box_speed, max_box_speed
    
    target = d_x + 10  
    
    left = box_x - 15
    right = box_x + 75

    if left > target and box_x > -240:
        box_x -= box_speed
        sleep(0.01)

    elif right < target and box_x < 240:
        box_x += box_speed 
        sleep(0.01)


def keyboardListener(key,x,y):
    global cheat
    if key == b'c':
        cheat = True
        print("Cheat mode activated!")

glutInit()                               
glutInitDisplayMode(GLUT_RGBA)           
glutInitWindowSize(500, 600)             
glutInitWindowPosition(0, 0)            
wind = glutCreateWindow(b"Diamond Catcher")  
glutDisplayFunc(display)         
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutSpecialFunc(special_key_listener)
glutMainLoop()                   
