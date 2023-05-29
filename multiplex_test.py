import board
from board import SCL, SDA
import busio
import os
import sys
import digitalio
#import adafruit_tsl2591
import adafruit_tca9548a
import PIL
from PIL import Image, ImageDraw, ImageFont
from time import *
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)

for channel in range(8):
    if tca[channel].try_lock():
        oled_a[channel] = adafruit_ssd1306.SSD1306_I2C(128, 32, tca[channel], reset=RESET_PIN)
        oled_a[channel].fill(0)
        oled_a[channel.show()
        image[channel] = Image.new("1", (oled[channel].width, oled[channel].height))
        draw[channel] = ImageDraw.Draw(image[channel])
        draw[channel].text((0, 0), "SHOOT", font=font, fill=255)
        oled[channel].image(image[channel])
        oled[channel].show()
        tca[channel].unlock()
        
# For each sensor, create it using the TCA9548A channel instead of the I2C object
#oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c, reset=RESET_PIN)
#oled = adafruit_ssd1306.SSD1306_I2C(128, 32, tca[6], reset=RESET_PIN)
#oled1 = adafruit_ssd1306.SSD1306_I2C(128, 32, tca[5], reset=RESET_PIN)


# Clear display.
#oled.fill(0)
#oled.show()
#oled1.fill(0)
#oled1.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

image1 = Image.new("1", (oled1.width, oled1.height))
draw1 = ImageDraw.Draw(image1)


# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
font3 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)


# Draw the text
#draw.text((0, 0), controls[0], font=font, fill=255)
#draw.text((0, 30), controls[1], font=font2, fill=255)

draw.text((0, 0), "SHOOT", font=font, fill=255)
draw1.text((0, 0), "JUMP", font=font, fill=255)

#draw.text((34, 50), sys.argv[3], font=font3, fill=255)
#draw.text((34, 50), rom_base[0], font=font3, fill=255)


# Display image
oled.image(image)
oled.show()

oled1.image(image1)
oled1.show()


