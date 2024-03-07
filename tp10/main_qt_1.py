
from PySide6 import QtCore, QtWidgets, QtGui,QtUiTools

def main():
    ui_file_name = "main.ui"
    ui_file = QtCore.QFile(ui_file_name)
    app = QtWidgets.QApplication()
    loader = QtUiTools.QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.show()

    app.exec()

if __name__=='__main__':
    main()
