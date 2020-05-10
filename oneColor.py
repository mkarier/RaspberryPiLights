import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB
wait = 1.0

white = (255,255,255)
color = white

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False, pixel_order=ORDER)

for pos in range(num_pixels):
	pixels[pos] = color
pixels.show()
time.sleep(wait);
