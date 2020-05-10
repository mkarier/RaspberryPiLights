import time
import board
import neopixel
import random



pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.RGB
wait = 1.0

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

def randomColorForPosition(pos):
	pixels[pos] = (random.randrange(255), random.randrange(255), random.randrange(255))



while True:
	for pos in range(num_pixels):
		randomColorForPosition(pos)
	pixels.show()
	time.sleep(wait)
