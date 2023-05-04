from tkinter import *
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import Menu
from PIL import ImageTk, Image
from pathlib import Path
import sys, os

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src'))

from utils import *

class TopLevel(Toplevel):

    WINDOWS = [
        "MAIN",
        "CONFIG",
        "ABOUT",
        "INIT",
        "ORDER",
        "CUSTOMER",
        "PAYMENT",
        "RECEIPT"
    ]

    # private root Tk
    # private canvas Canvas
    # private running Boolean
    def __init__(self, type: str):
        super().__init__()
        self.type = type.upper()
        self.protocol("WM_DELETE_WINDOW", self.window_close)
    
    def redraw(self):
        self.update()
        self.update_idletasks()

    def window_close(self):
        if(self.type not in TopLevel.WINDOWS):
            TopLevel.WINDOWS.append(self.type)
            self.running = False
            self.destroy()

    def wait_for_close(self):
        self.running = True
        while(self.running == True):
            self.redraw()

    def window_close(self):
        if(self.type not in TopLevel.WINDOWS):
            TopLevel.WINDOWS.append(self.type)
            self.running = False
            self.destroy()