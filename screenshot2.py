from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
import time
import cv2 as cv
beg = time.time()
#hwnd = 1377344
hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("screenshot.jpg")
end = time.time()
print(end - beg)
img=cv.imread("screenshot.jpg")
cv.imshow("test",img)
cv.waitKey(0)
#cv.destoryAllWindows()


