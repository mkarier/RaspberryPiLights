import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB
wait = 1.0

white = (255,255,255)
orange = (177,61,4)
purple = (59,4,105)
color = purple

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False, pixel_order=ORDER)



count = 0
for pos in range(num_pixels):
    count = (count + 1) %4
    if(count == 0):
        if(color == purple):
            color = orange
        else:
            color = purple
    pixels[pos] = color
pixels.show()
time.sleep(wait);
