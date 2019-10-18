1.打开QTdesigner anconda3下路径在Anaconda3\Library\bin\designer.exe，建好ui,可以使用如下格式导入UI：
from PyQt5.uic import loadUi
class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi(r'文件路径', self)
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
2.可以适用以下命令转换ui文件成为py文件
r"Y:\Anaconda3\Scripts\pyuic5.exe filename.ui -o newfilename.py"
此时导入主函数方法则为以下：
class MainWindow(QMainWindow,Ui_MainWindow):#Ui_MainWindow为转py的ui的classname

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
