from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
C=(52, 235, 210)

def p():
    G = green
    Y = yellow
    B = blue
    O = white
    logo = [
    O, B, B, B, B, O, O, O,
    O, B, B, B, B, B, O, O,
    O, B, B, B, B, B, O, O,
    O, B, B, B, B, B, O, O,
    O, B, B, B, B, O, O, O,
    O, B, O, O, O, O, O, O,
    O, B, O, O, O, O, O, O,
    O, B, O, O, O, O, O, O,
    ]
    return logo

def y():
    G = green
    R = red
    O =  white
    logo = [
    R, O, O, O, O, O, O, R, 
    O, R, O, O, O, O, R, O,
    O, O, R, O, O, R, O, O, 
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    ]
    return logo

def t():
    W = green
    O = white
    logo = [
     O, O, O, O, O, O, O, O, 
     W, W, W, W, W, W, W, W,
     W, W, W, W, W, W, W, W, 
     O, O, O, W, W, O, O, O,
     O, O, O, W, W, O, O, O,
     O, O, O, W, W, O, O, O,
     O, O, O, W, W, O, O, O,
     O, O, O, W, W, O, O, O,
    ]
    return logo

def h():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, W, W, O, O, O, W, W,
    O, W, W, O, O, O, W, W,
    O, W, W, W, W, W, W, W,
    O, W, W, W, W, W, W, W,
    O, W, W, O, O, O, W, W,
    O, W, W, O, O, O, W, W,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def o():
    P= green
    O = blue
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def n():
    P = C
    O = white
    logo = [
    P, P, O, O, O, O, P, P,
    P, P, O, O, O, O, P, P,
    P, P, P, O, O, O, P, P,
    P, P, P, P, O, O, P, P,
    P, P, O, P, P, O, P, P,
    P, P, O, O, P, P, P, P,
    P, P, O, O, O, P, P, P,
    P, P, O, O, O, O, P, P,
    ]
    return logo

images = [p,y,t,h,o,n]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
