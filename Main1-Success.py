import random, string, webbrowser, time, os, pyautogui
from PIL import Image
left, top, right, bottom, i = 600, 200, 1315, 550, 1
while ( i <= 10 ):
    def randomString( stringLength=10 ):
        letters = string.ascii_lowercase
        return ''.join( random.choice( letters ) for i in range( stringLength ) )
    testurl = "https://meet.google.com/" + randomString(10)
    webbrowser.open( testurl )
    time.sleep(15)
    scrnshot = pyautogui.screenshot().crop((left, top, right, bottom)).save("D:\\Ritik\\Locker\\IMFOR 3\\Project MeetHack\\1.png")
    os.system("taskkill /im chrome.exe /f")
    errorimg = "D:\\Ritik\\Locker\\IMFOR 3\\Project MeetHack\\ERROR2.png"
    testimg = "D:\\Ritik\\Locker\\IMFOR 3\\Project MeetHack\\1.png"
    if open(errorimg, "rb").read() == open(testimg,"rb").read():
        print False, "TARGET NOT FOUND...", testurl,"LINK TRIED:", i 
    else:
        print True, "TARGET FOUND...", testurl, "LINK TRIED:", i
    i += 1
os.remove(testimg)
