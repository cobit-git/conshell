import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class ConshellOLED(object):
    def __init__(self):
        # Setting some variables for our reset pin etc.
        RESET_PIN = digitalio.DigitalInOut(board.D4)
        # Define the Reset Pin
        self.oled_reset = digitalio.DigitalInOut(board.D4)
        # Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
        i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, reset=RESET_PIN)
        # Clear display.
        self.oled.fill(0)
        self.oled.show()
        # Create blank image for drawing.
        self.con_image = Image.new("1", (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.con_image)
        # Load a font in 2 different sizes.
        self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        self.font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

    def clear_display(self):
        self.oled.fill(0)
        self.oled.show()

    def draw_large_text(self, string, x, y):
        self.draw.text((x, y), string, font=self.font, fill=255)
    
    def draw_small_text(self, string, x, y):
        self.draw.text((x, y), string, font=self.font2, fill=255)

    def update_display(self):
        self.oled.image(self.con_image)
        self.oled.show()

if __name__ == '__main__':
    con_oled = ConshellOLED()
    con_oled.draw_small_text("this is test", 0, 0)
    con_oled.update_display()