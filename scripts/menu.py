import time
from display import display
from input import input

class menu:
    def __init__(self, childs):
        self.childs = childs
        
    def startBack(self):
        list = ["back"]
        for child in self.childs:
            list.append(child.getDisplayName())
        self.display = display(True, list)
        self.activeChild = 0
        self.inpt = input(self)
        
    def start(self, master):
        self.master = master
        list = ["back"]
        for child in self.childs:
            list.append(child.getDisplayName())
        self.display = display(True, list)
        self.activeChild = 0
        self.inpt = input(self)
        
    def tick(self):
        if isinstance(self.activeChild, int):
            self.inpt.tick()
        else:
            self.activeChild.tick()
            
    def back(self):
        self.master.startBack()
            
    def stop(self):
        self.inpt.stop()
        self.display.stop()
        
    def buttonPressed(self):
        selected = self.display.getSelection()
        self.stop()
        if selected == 0:
            self.back()
        else:
            self.activeChild = self.childs[selected - 1]
            self.activeChild.start(self)

    def buttonReleased(self):
        print("released")
        
    def rotaryUp(self):
        self.display.shiftSelectionDown()
        self.display.refresh()
        print("down")
        
    def rotaryDown(self):
        self.display.shiftSelectionUp()
        self.display.refresh()
        print("up")
