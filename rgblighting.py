import pyautogui
from colorthief import ColorThief
import bolt

cachedir = "/home/saurabh000345/"
imgdir = cachedir + "tmp.png"


def getss():
    ss = pyautogui.screenshot()
    ss.save(imgdir)


def get_dominant():
    thief = ColorThief(imgdir)
    return thief.get_color(quality=1)


def main():
    while(True):
        getss()
        print(get_dominant())


if __name__ == "__main__":
    main()
