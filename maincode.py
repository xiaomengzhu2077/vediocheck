import sys
import os
import time
import pytesseract
from PIL import Image
import win32api,win32con
import pyttsx3
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi(r'X:\python\pythonproject\vediocheck\UI.ui', self)
        self.pushButton.clicked.connect(self.Get_Pos)
        self.lineEdit.textEdited[str].connect(lambda: self.posone())
        self.lineEdit_2.textEdited[str].connect(lambda: self.posone_2())
        self.lineEdit_3.textEdited[str].connect(lambda: self.posone_3())
        self.lineEdit_4.textEdited[str].connect(lambda: self.posone_4())
        self.engine = pyttsx3.init()
    def Get_Pos(self):
        while True:
            beg = time.time()
            #app = QApplication(sys.argv)
            screen = QApplication.primaryScreen()
            #pix = screen.grabWindow(0, self.stpos, self.stpos_2, self.stpos_3, self.stpos_4)
            pix = screen.grabWindow(0,383,1175,200,50)
            pix.save("123.jpg")
            time.sleep(1)
            p = pytesseract.image_to_string(Image.open("123.jpg"), lang="eng")
            print(p)
            if 'Bea' in p:
                #win32api.MessageBox(1, "垫片报警", "提醒", win32con.MB_OK)
                engine = pyttsx3.init()
                engine.say("垫片报警")
                time.sleep(0.3)
                engine.say("垫片报警")
                time.sleep(0.3)
                engine.say("垫片报警")
                engine.runAndWait()
            else:
                pass
            end = time.time()
            print(end - beg)
            time.sleep(5)
    def posone(self):
        self.stpos = int(self.lineEdit.text())
        print("1...", self.stpos)
    def posone_2(self):
        self.stpos_2 = int(self.lineEdit_2.text())
        print("2...", self.stpos_2)
    def posone_3(self):
        self.stpos_3 = int(self.lineEdit_3.text())
        print("3...", self.stpos_3)
    def posone_4(self):
        self.stpos_4 = int(self.lineEdit_4.text())
        print("4...", self.stpos_4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

