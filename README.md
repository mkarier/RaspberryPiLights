I have taken the code from https://www.tweaking4all.com/hardware/arduino/adruino-led-strip-effects/ and re-wrote it in python 
so that it can run on my Raspberry pi. 

Another Tutorial is https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage

You do need neopixel librarys:

sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka

These python programs need to be run as sudo.
