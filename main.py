from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.input__ = ""

        self.setWindowTitle("Calculator")
        self.resize(300, 300)

        self.input_lbl = QTextEdit(self)
        self.input_lbl.move(40, 10)
        self.input_lbl.resize(215, 40)

        x = 40
        y = 60

        step = 5
        indent = x
        btn_size = 50

        count_btn_in_row = 4

        for i in [1, 2, 3, "+", 4, 5, 6, "-", 7, 8, 9, "*", ".", 0, "=", "/"]:
            self.btn = QPushButton(str(i), self)
            self.btn.resize(btn_size, btn_size)
            self.btn.move(x, y)
            self.btn.clicked.connect(self.button_clicked)
            x += btn_size + step
            if x == (indent + btn_size * count_btn_in_row + step * count_btn_in_row):
                y += btn_size + step
                x = indent

    def button_clicked(self):
        num = self.sender().text()

        if num != "=":
            self.input__ += str(num)
            self.input_lbl.setText(self.input__)
        else:
            try:
                result = eval(self.input__)
                self.input_lbl.setText(str(result))
                self.input__ = ""
            except Exception:
                self.input__ = ""
                self.input_lbl.setText("<b>ERROR</b>")

# self.btn_1 = QPushButton("1", self)
# self.btn_2 = QPushButton("2", self)
# self.btn_3 = QPushButton("3", self)
# self.btn_4 = QPushButton("4", self)
# self.btn_5 = QPushButton("5", self)
# self.btn_6 = QPushButton("6", self)
# self.btn_7 = QPushButton("7", self)
# self.btn_8 = QPushButton("8", self)
# self.btn_9 = QPushButton("9", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
