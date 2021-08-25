from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('aaa.ui', self)
        btn = pushButton_2("CLICK", self)
        self.show()
    def clickme(self):
        # printing pressed
        print("pressed")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()