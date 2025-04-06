import subprocess
from display import display
from input import input
from textinput import textinput

class WifiHotspot:
    def __init__(self):
        self.lines = ["SSID:", "", "Password:", "", "Start Hotspot"]
    
    def start(self, master):
        self.master = master
        self.display = display(True, self.lines)
        self.inpt = input(self)
        
    def tick(self):
        self.inpt.tick()
        
    def stop(self):
        self.inpt.stop()
        self.display.stop()
        
    def buttonPressed(self):
        selection = self.display.getSelection()
        if selection % 2 == 1:
            self.inpt.stop()
            self.display.stop()
            self.inpt = textinput()
            self.lines[selection] = self.inpt.getInput(self.lines[selection - 1], "")
            self.start(self.master)
        elif selection == 4:
            self.stop()
            self.master.startBack()

    def buttonReleased(self):
        print("released")
        
    def rotaryUp(self):
        self.display.shiftSelectionDown()
        self.display.refresh()
        
    def rotaryDown(self):
        self.display.shiftSelectionUp()
        self.display.refresh()