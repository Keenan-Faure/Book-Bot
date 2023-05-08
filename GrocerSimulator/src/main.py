from pathlib import Path
import os, sys

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / 'window'))

from window import *

def main():
    win = Window(460, 515, "main", "Grocer Simulator")
    win.wait_for_close()

main()