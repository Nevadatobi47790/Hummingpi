import time

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306



class display:

    def __init__(self, selectionMode, lineList):
        # param if there should be a selection arrow
        self.sel = selectionMode
        self.selection = 0

        # list to hold the contents of the lines
        self.lines = lineList
        self.lineCount = len(lineList)
        while self.lineCount < 4:
            self.lines.append("")
            self.lineCount = len(self.lines)

        # index of which the lines are shown
        self.topLine = 0

        # Create the I2C interface.
        i2c = busio.I2C(SCL, SDA)

        # Create the SSD1306 OLED class.
        # The first two parameters are the pixel width and pixel height.  Change these
        # to the right size for your display!
        self.disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

        # Clear display.
        self.disp.fill(0)
        self.disp.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new("1", (self.width, self.height))

        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        self.padding = -2
        self.top = self.padding
        self.bottom = self.height - self.padding

        # Move left to right keeping track of the current x position for drawing shapes.
        self.x = 0

        # Load default font.
        self.font = ImageFont.load_default()

        # Alternatively load a TTF font.  Make sure the .ttf font file is in the
        # same directory as the python script!
        # Some other nice fonts to try: http://www.dafont.com/bitmap.php
        # font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)

        self.refresh()

    def selectionMode(self, bool):
        self.sel = bool

    def select(self, line):
        self.selection = line

    def getSelection(self):
        return self.selection

    def shiftSelectionDown(self):
        if not self.selection == self.lineCount - 1:
            self.selection = self.selection + 1
            if self.selection == self.topLine + 4:
                self.shiftLinesDown()

    def shiftSelectionUp(self):
        if not self.selection == 0:
            self.selection = self.selection - 1
            if self.selection == self.topLine - 1:
                self.shiftLinesUp()

    def refresh(self):
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        # Write four lines of text.
        if not self.sel:
            self.draw.text((self.x, self.top + 0), self.lines[self.topLine], font=self.font, fill=255)
            self.draw.text((self.x, self.top + 8), self.lines[self.topLine + 1], font=self.font, fill=255)
            self.draw.text((self.x, self.top + 16), self.lines[self.topLine + 2], font=self.font, fill=255)
            self.draw.text((self.x, self.top + 24), self.lines[self.topLine + 3], font=self.font, fill=255)
        else:
            self.draw.text((self.x, self.top + 0), " " + self.lines[self.topLine], font=self.font, fill=255)
            self.draw.text((self.x, self.top + 8), " " + self.lines[self.topLine + 1], font=self.font, fill=255)
            self.draw.text((self.x, self.top + 16), " " + self.lines[self.topLine + 2], font=self.font, fill=255)
            self.draw.text((self.x, self.top + 24), " " + self.lines[self.topLine + 3], font=self.font, fill=255)

            self.draw.text((self.x, self.top + (self.selection - self.topLine)*8), ">", font=self.font, fill=255)

        # Display image.
        self.disp.image(self.image)
        self.disp.show()

    def newLines(self, lineList):
        self.lines = lineList
        self.topLine = 0
        self.selection = 0
        self.lineCount = len(lineList)

    def setLine(self, index, line):
        self.lines[index] = line
        
    def shiftLinesDown(self):
        if not self.topLine == self.lineCount - 4:
            self.topLine = self.topLine + 1

    def shiftLinesUp(self):
        if not self.topLine == 0:
            self.topLine = self.topLine - 1
            
    def stop(self):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
