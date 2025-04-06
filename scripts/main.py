import time
from menu import menu
from executable import executable as exe
from WifiHotspot import WifiHotspot

WifiExe = []
WifiExe.append(exe(WifiHotspot(), "WifiHotspot"))

mainMenuExe = []
mainMenuExe.append(exe(menu(WifiExe), "Wifi Tools"))

mainMenu = menu(mainMenuExe)

mainMenu.start(mainMenu)
while True:
    mainMenu.tick()