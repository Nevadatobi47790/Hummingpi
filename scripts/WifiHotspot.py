import subprocess
from display import display
from input import input
from textinput import textinput
import os
import time

class WifiHotspot:
    def __init__(self):
        self.lines = ["SSID:", "", "Password:", "", "Start Hotspot", "Cancel and stop Hotspot"]
    
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
        if selection == 1 or selection == 3:
            self.inpt.stop()
            self.display.stop()
            self.inpt = textinput()
            self.lines[selection] = self.inpt.getInput(self.lines[selection - 1], "")
            self.start(self.master)
        elif selection == 4:
            os.system("sudo nmcli connection delete t-450")
            print(os.system("sudo nmcli device wifi hotspot con-name t-450 ssid " + self.lines[1] + " password " + self.lines[3]))
            self.stop()
            self.master.startBack()
        elif selection == 5:
            os.system("sudo nmcli connection delete t-450")
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
