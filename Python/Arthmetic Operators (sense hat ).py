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

def logo():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
   O, O, O, O, O, O, G, G,
   O, G, G, O, O, G, G, O,
   O, G, G, O, G, G, O, O,
   O, O, O, G, G, O, O, O,
   O, O, G, G, O, O, O, O,
   O, G, G, O, O, G, G, O,
   G, G, O, O, O, G, G, O,
   G, O, O, O, O, O, O, O,]
    return logo

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
   O, O, O, O, O, O, O, O,
   O, O, O, O, O, O, O, O,
   O, O, O, O, O, O, O, O,
   O, R, R, R, R, R, R, O,
   O, R, R, R, R, R, R, O,
   O, O, O, O, O, O, O, O,
   O, O, O, O, O, O, O, O,
   O, O, O, O, O, O, O, O,
   ]
    return logo

def plus():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

images = [logo, trinket_logo, plus, raspi_logo, raspi_logo, equals]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
