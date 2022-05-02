import pyautogui as pg
import os
import time

class PyAutoGUI_Master():

    def __init__(self):
        self.cords = None
        self.conf = 0.7
        self.path = os.getcwd()

    def locate(self, name, check=False, wait=0, move=False, click=True):
        if wait != 0: time.sleep(wait)
        path = os.path.join(self.path, 'src', name)+'.png'
        self.cords = pg.locateOnScreen(path, self.conf)
        count = 0
        while not self.cords and check:
            count +=1
            time.sleep(1)
            print(f"Trying to locate {name}, attempt: {count}")
            self.cords = pg.locateOnScreen(path, self.conf) 

        if self.cords != None:
            print(f"Found {name} at {self.cords}")
            if move: pg.moveTo(self.cords)
            if click: pg.click(self.cords)
            return True
        else:
            print(f"Not found {name}") 
            return False
    def get_position(self, name, wait=0):
        if wait != 0: time.sleep(wait)
        path = os.path.join(self.path, 'src', name)+'.png'
        return pg.locateOnScreen(path, self.conf)
    