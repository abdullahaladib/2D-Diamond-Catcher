from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def find_zone(x,y):
    zone = 0
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

def convert_between_zone0_and_zonex(x, y, zone):
      if zone == 1:
            temp = x
            x = y
            y = temp
      elif zone == 2:
            temp = x
            x = y
            y = -temp
      elif zone == 3:
            x = -x
      elif zone == 4:
            x = -x
            y = -y
      elif zone == 5:
            temp = x
            x = -y
            y = -temp
      elif  zone == 6:
            temp = x
            x = -y
            y = -temp
      elif zone == 7:
            y = -y

      return [x,y]

def mpl(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    zone = find_zone(dx, dy)
    x1,y1 = convert_between_zone0_and_zonex(x1,y1,zone)
    x2,y2 = convert_between_zone0_and_zonex(x2,y2,zone)
    dx = x2-x1
    dy = y2-y1
    d = (2*dy) - dx
    delNE = 2*(dy-dx)
    delE = 2*dy

    for x in range(x1,(x2+1)):
      draw_points(convert_between_zone0_and_zonex(x,y1,zone))
      if d>0:
           d += delNE
           y1 += 1
      else:
           d += delE  


def draw_points(lst):
    x,y=lst
    glPointSize(5)         
    glBegin(GL_POINTS)     
    glVertex2f(x, y)        
    glEnd()

def setup_projection():
    glViewport(0, 0, 500, 500)     # Define the portion of the window to render to
    glMatrixMode(GL_PROJECTION)    # Switch to the projection matrix
    glLoadIdentity()               # Reset the projection matrix
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)  # Define a 2D orthographic projection
    glMatrixMode(GL_MODELVIEW)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and depth buffer
    glLoadIdentity()                                    # Reset transformations
    setup_projection()                                  # Set up coordinate system
    glColor3f(1.0, 1.0, 0.0)                            # Set color (R, G, B) → Yellow
    mpl(100,400,300,300)                                   # Draw the point
    glutSwapBuffers()  

glutInit()                               # Initialize GLUT
glutInitDisplayMode(GLUT_RGBA)           # Set display mode: RGBA color
glutInitWindowSize(500, 500)             # Set window size (width, height)
glutInitWindowPosition(0, 0)             # Set window position (top-left corner)
glutCreateWindow(b"OpenGL 2D Point")     # Create window with a title
glutDisplayFunc(display)                 # Register display callback
glutMainLoop()                           # Start the main event-processing loop
