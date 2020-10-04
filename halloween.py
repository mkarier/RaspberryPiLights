import time
import board
import neopixel


pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB
lengthOfTime = 5

wait = 1.0
width = 4
white = (255,255,255)
orange = (177,61,4)
purple = (59,4,105)
color = purple

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False, pixel_order=ORDER)


def alternativePattern(lengthOfTime, color):
    seconds = 0
    while((lengthOfTime - seconds) != 0):
        count = 0
        for pos in range(num_pixels):
            count = (count + 1) % width
            if(count == 0):
                if(color == purple):
                    color = orange
                else:
                    color = purple
            pixels[pos] = color
        pixels.show()
        time.sleep(wait)
        seconds+=1

def swapColor(color):
    if(color == purple):
        return orange
    else:
        return purple

def raftPattern(maxCycle, color):
    background = color
    color = swapColor(color)
    raft = color
    raftSize = width *3
    position = 0
    cycle = 0
    while((maxCycle - cycle) != 0):
        for pos in range(num_pixels):
            pixels[pos] = background
        for pos in  range(raftSize):
            if(position == 300):
                cycle += 1
            position = (position + 1) % num_pixels
            pixels[position] = raft
        pixels.show()
        time.sleep(wait/2)
while(True):
    alternativePattern(lengthOfTime, color)
    raftPattern(lengthOfTime, color)