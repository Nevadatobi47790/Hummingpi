from input import input
from display import display

class textinput:
    def __init__(self):
        self.ascii = [["¬", "«", "Á", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
            ["¬", "«", "¹", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
            ["¬", "«", "%", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["¬", "«", "á", " ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "'", "{", "|", "}", "~"]]
        self.inpt = input(self)
        self.txt = ""
        self.currentAscii = 0
        self.currentLetter = 0
        self.done = False

    def getInput(self, title, start):
        self.txt = start
        self.display = display(False, [title, start])
        while True:
            if self.done:
                self.inpt.stop()
                return self.txt
            self.inpt.tick()

    def updateDisplay(self):
        self.display.setLine(1, self.txt + self.ascii[self.currentAscii][self.currentLetter])
        self.display.refresh()

    def buttonPressed(self):
        if self.currentLetter == 0:
            self.done = True

        elif self.currentLetter == 1:
            if not len(self.txt) == 0:
                self.txt = self.txt[:-1]
                self.updateDisplay()

        elif self.currentLetter == 2:
            self.currentAscii = (self.currentAscii + 1) % 4
            if self.currentLetter >= len(self.ascii[self.currentAscii]):
                self.currentLetter = 0
            self.updateDisplay()

        else:
            self.txt = self.txt + self.ascii[self.currentAscii][self.currentLetter]
            self.updateDisplay()
                
                
    def buttonReleased(self):
        print("released")
        
    def rotaryDown(self):
        self.currentLetter = self.currentLetter - 1
        if self.currentLetter < 0:
            self.currentLetter = 0
        self.updateDisplay()
        
    def rotaryUp(self):
        self.currentLetter = self.currentLetter + 1
        if self.currentLetter == len(self.ascii[self.currentAscii]):
            self.currentLetter = 0
        self.updateDisplay()
