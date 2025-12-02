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

    for i in range(x1,(x2+1)):
      pass

mpl(40,30,20,-50)