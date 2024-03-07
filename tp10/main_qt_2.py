from main_ui import Ui_MainWindow
from PySide6 import QtCore, QtWidgets, QtGui,QtUiTools


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()

if __name__=='__main__':
    main()
