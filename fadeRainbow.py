import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.RGB
wait = 0.5

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False, pixel_order=ORDER)


def setColor(r, g, b):
	for index in range(0, num_pixels):
		pixels[index] = (r,g,b)

def pickColor(index):
	color = [0,0,0]
	if(index < 85):
		color[0] = index *3
		color[1] = 255 - index *3
		color[2] = 0
	elif(index < 170):
		index -= 85
		color[0] = 255 - index * 3
		color[1] = 0
		color[2] = index *3
	else:
		index -= 170
		color[0] = 0
		color[1] = index *3
		color[2] = 255 - index * 3
	return color

while True:
	#red loop
	for seed in range(0, 255):
		color = pickColor(seed)
		setColor(color[0], color[1], color[2])
		pixels.show()
		time.sleep(wait)

