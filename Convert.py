from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
import importlib.util

class mainProgram(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainProgram, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.BTN_Convert.clicked.connect(self.convert)
        self.BTN_Exit.clicked.connect(self.close)
        self.BTN_Browse.clicked.connect(self.getfiles)
        self.show()
    def convert(self):

        spec = importlib.util.spec_from_file_location("module.name","skrypty/"+self.comboBox.currentText()+"/"+"core.py")
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        print(folderpath)
        try:
            if folderpath!='':
                for fromfile in self.filenames:
                    foo.Core.main(foo.Core,folderpath,fromfile)
                msg = QMessageBox()
                msg.setWindowTitle("Info")
                msg.setText("Konwersja Udana")
                x = msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Info")
            msg.setText("Brak pliku wejsciowego")
            print(e)
            x = msg.exec_()

    def getfiles(self):
        newWindow=QFileDialog()
        newWindow.setFileMode(QFileDialog.ExistingFiles)
        if newWindow.exec_():
            self.filenames = newWindow.selectedFiles()
            self.textEdit.setText(str("\n".join(self.filenames)))

if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = mainProgram()
        sys.exit(app.exec_())
    except Exception as e:
      print("Erorr to : %s", e)