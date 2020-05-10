import time
import board
import neopixel
import random

pixel_pin = board.D18

num_pixels = 300

Order = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False, pixel_order=Order)

randSeed = 10
randCompare = 8
meteorSize = 15

meteorTrailDecay = 64


def setAll(red, blue, green):
	for index in range(0,num_pixels):
		pixels[i] = (red, blue, green)

def meteorRain(red, blue, green, boolRandomDecay):
	for index in range(0, num_pixels):
		#fade brightness all LEDs one step
		for j in range(0,num_pixels):
			if( not boolRandomDecay or (random.randrange(randSeed)>randCompare)):
				fadeToBlack(j, meteorTrailDecay)
		
		for m in range(0,meteorSize):
			if (((index -m)<num_pixels) and ((index-m)>=0)):
				pixels[index-m] = (red, blue, green)
		pixels.show()

def meteorRainReverse(red, blue, green, boolRandomDecay):
	for index in range(num_pixels, 0, -1):
		for j in range(0, num_pixels):
			if( not boolRandomDecay or (random.randrange(randSeed) > randCompare)):
				fadeToBlack(j, meteorTrailDecay)

		for m in range(0, meteorSize):
			if (((index -m ) < num_pixels) and ((index -m)>= 0)):
				pixels[index-m] = (red, blue, green)
		pixels.show()


def fadeToBlack(ledNo, fadeValue):

	oldColor = pixels[ledNo]
	color = [0,0,0]
	color[0] = (oldColor[0] & 0x00ff0000 ) >> 16
	color[1] = (oldColor[1] & 0x00ff0000) >> 8
	color[2] = (oldColor[2] & 0x00ff0000)

	for i in range(0,3):
		if color[i] < 10:
			color[i] = 0
		else:
			color[i] = int(color[0] - (color*fadeValue/256))
	pixels[ledNo] = color

def pickColor(seed):
	color = [0,0,0]
	if(seed < 85):
		color[0] = seed *3
		color[1] = 255 - seed * 3
		color[2] = 0
	elif(seed < 170):
		seed -= 85
		color[0] = 255 - seed *3
		color[1] = 0
		color[2] = seed * 3
	else:
		seed -= 170
		color[0] =0
		color[1] = seed *3
		color[2] = 255 - seed *3
	return color


while True:
	for seed in range(0,255, 10):
		color = pickColor(seed)
		meteorRain(color[0], color[1], color[2], True)
		color = pickColor(255 -seed)
		meteorRainReverse(color[0], color[1], color[2], True)
