
from PIL import Image, ImageEnhance
import win32clipboard as w
import win32con
import subprocess
import os
import time

def image_to_string(im):
    im.save("t.jpg")
    open("r.txt", "w").write("")
    time.sleep(0.1)
    args = ["Tesseract-ocr\\tesseract.exe", "t.jpg", "r", "digits"]
    proc = subprocess.Popen(args)
    proc.wait()
    r = open("r.txt").read().strip()
    return r
 
def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d
 
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()


def read_pic(pic):
    im = Image.open(pic)
    im = im.convert("L")
    w, h = im.size
    h = h * 2
    w = w * 2
    im = im.resize((w, h))

    im2 = Image.new("L", (w, h), 250)
    for i in range(w):
        for j in range(h):
            if im.getpixel((i,j)) < 150:
                if i < w-1:
                    im2.putpixel((i,j), 10)
                    im2.putpixel((i+1,j), 10)
    im = im2
    # im = ImageEnhance.Brightness(im).enhance(1.2)
    # im = ImageEnhance.Contrast(im).enhance(5.0)
    # im = ImageEnhance.Sharpness(im).enhance(7.0)
    # im.show()

    txt = image_to_string(im)

    # print txt

    # txt = txt.replace("E=", "6")
    # txt = txt.replace("l", "1")
    # txt = txt.replace("I", "1")
    # txt = txt.replace("J", "1")
    # txt = txt.replace("B", "9")
    # txt = txt.replace("T", "7")
    # txt = txt.replace("E", "8")
    # txt = txt.replace("D", "0")
    # txt = txt.replace("i", "7")
    # txt = txt.replace("Z", "2")

    result = ""
    for c in txt:
        if c in "1234567890":
            result += c

    return result


reads = os.listdir("pics")

while True:

    pics = os.listdir("pics")

    for pic in pics:
        if pic not in reads:
            pic = "./pics/" + pic
            txt = read_pic(pic)
            print "-"
            print txt
            setText(txt)

    reads = pics

    time.sleep(0.5)
    print ".",