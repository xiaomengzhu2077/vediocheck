import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi(r'X:\python\pythonproject\vediocheck\UI.ui', self)
        self.pushButton.clicked.connect(self.Get_Pos)
    def Get_Pos(self):
        pass

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
