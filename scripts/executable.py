class executable:
    def __init__(self, programm, displayName):
        self.programm = programm
        self.displayName = displayName
    

    def start(self, master):
        self.programm.start(master)

    def tick(self):
        self.programm.tick()

    def stop(self):
        self.programm.stop()

    def getDisplayName(self):
        return self.displayName
