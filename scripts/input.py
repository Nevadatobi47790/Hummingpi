from RPi import GPIO

class input:
    
    def __init__(self, master):
        self.master = master
        self.clk = 14
        self.dt = 15
        self.sw = 18

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.counter = 0
        self.lastCounter = 0
        self.clkLastState = GPIO.input(self.clk)
        self.swLastState = GPIO.input(self.sw)

    def getButton(self):
        return GPIO.input(self.sw)

    def tick(self):
        self.swState = GPIO.input(self.sw)
        if self.swState != self.swLastState:
            if self.swState == 1:
                self.master.buttonPressed()
            else:
                self.master.buttonReleased()
                    
        self.swLastState = self.swState
        self.clkState = GPIO.input(self.clk)
        self.dtState = GPIO.input(self.dt)
        if self.clkState != self.clkLastState:
            if self.dtState != self.clkState:
                self.counter += 0.5
                if self.lastCounter == self.counter - 1:
                    self.master.rotaryUp()
                    self.lastCounter = self.counter
            else:
                self.counter -= 0.5
                if self.lastCounter == self.counter + 1:
                    self.master.rotaryDown()
                    self.lastCounter = self.counter
        self.clkLastState = self.clkState
        
    def stop(self):
        GPIO.cleanup()
