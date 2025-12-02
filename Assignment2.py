from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

class Diamond:
      def __init__(self, x1,y1,x2,y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
    
      def collition(self,other):  
            if (self.x1 < other.x2 < self.x2) or (self.x1<other.x1<self.x2):
                if (self.y1 < other.y2 < self.y2):
                    return True
                else:
                    return False
            else:
                return False
            
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
    glViewport(0, 0, 500, 600)     # Define the portion of the window to render to
    glMatrixMode(GL_PROJECTION)    # Switch to the projection matrix
    glLoadIdentity()               # Reset the projection matrix
    glOrtho(-250.0, 250, -300.0, 300, 0.0, 1.0)  # Define a 2D orthographic projection
    glMatrixMode(GL_MODELVIEW)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and depth buffer
    glLoadIdentity()                                    # Reset transformations
    setup_projection()
    iterate()
    draw_return()
    draw_pause()                                 # Set up coordinate system
    draw_cross()
    draw_diamond()                                  # Draw the point
    glutSwapBuffers()  
def draw_cross():
    glColor3f(1.0, 0.0, 0.0)
    mpl(220,270,240,290)
    mpl(240,270,220,289)

def draw_pause():
    glColor3f(1.0,1.0,0.0)
    mpl(-5,270,-5,290)
    mpl(5,270,5,290)

def draw_return():
    glColor3f(0.0,0.0,1.0)
    mpl(-240,280,-220,280)
    mpl(-240,280,-230,290)
    mpl(-240,279,-230,270)
def draw_diamond():
   
    global d_x, d_y
    d_x = random.randint(-240,240)
    d_y = 260
    glColor3f(1.0, 1.0, 1.0)
    mpl(d_x,d_y,d_x+10,d_y+15)
    mpl(d_x+10,d_y+15,d_x+20,d_y)
    mpl(d_x,d_y,d_x+10,d_y-15)
    mpl(d_x+20,d_y,d_x+10,d_y-15)


def iterate():
    glViewport(0, 0, 500, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250.0, 250, -300.0, 300, 0.0, 1.0)  # Define a 2D orthographic projection
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

glutInit()                               # Initialize GLUT
glutInitDisplayMode(GLUT_RGBA)           # Set display mode: RGBA color
glutInitWindowSize(500, 600)             # Set window size (width, height)
glutInitWindowPosition(0, 0)             # Set window position (top-left corner)
glutCreateWindow(b"OpenGL 2D Point")     # Create window with a title
glutDisplayFunc(display)                 # Register display callback
glutMainLoop()                           # Start the main event-processing loop
