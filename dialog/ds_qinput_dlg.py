import sys

from PySide6.QtWidgets import (
        QApplication, QMainWindow,
        QWidget, QPushButton, QLabel,QVBoxLayout,
        QLineEdit, QInputDialog, QFileDialog)

class MW (QMainWindow):

    def __init__(self):
        super(MW, self).__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        
        self.button0 = QPushButton('getText')
        self.button0.clicked.connect(self.slot00)
        self.button1 = QPushButton('getMultiLineText')
        self.button1.clicked.connect(self.slot00)
        self.button2 = QPushButton('getInt')
        self.button2.clicked.connect(self.slot00)
        self.button3 = QPushButton('getDouble')
        self.button3.clicked.connect(self.slot00)
        self.button4 = QPushButton('getItem')
        self.button4.clicked.connect(self.slot00)
        self.button5 = QPushButton('QFileDialog')
        self.button5.clicked.connect(self.slot00)


        self.ret_label = QLabel()


        layout = QVBoxLayout()
        layout.addWidget(self.button0)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.ret_label)
        
        tmp = QWidget()
        tmp.setLayout(layout)

        self.setCentralWidget(tmp)

    def slot00(self):
        print(self.sender())

        sender = self.sender()

        if sender == self.button0:
            ret_text, is_ok = QInputDialog.getText(
                    self,
                    "Input Text",
                    "Enter Your Text!",
                    QLineEdit.PasswordEchoOnEdit,
                    "default text",
                    )
            print(type(ret_text), type(is_ok))
            if is_ok:
                self.ret_label.setText(f'{ret_text}')

        elif sender == self.button1:
            ret_text, is_ok = QInputDialog.getMultiLineText(
                    self,
                    "Input Multiline Text",
                    "Enter your multiline text1",
                    )
            print(type(ret_text), type(is_ok))
            if is_ok:
                self.ret_label.setText(f'{ret_text}')
        elif sender == self.button2:
            ret_value, is_ok = QInputDialog.getInt(
                    self,
                    "Input Integer",
                    "Enter your int value",
                    0,
                    0, 100,
                    3,
                    )
            print(type(ret_value), type(is_ok))
            if is_ok:
                self.ret_label.setText(f'{ret_value}')
        elif sender == self.button3:
            ret_value, is_ok = QInputDialog.getDouble(
                    self,
                    "Input Double",
                    "Enter your Double value",
                    0,
                    0., 100.,
                    4,
                    )
            print(type(ret_value), type(is_ok))
            if is_ok:
                self.ret_label.setText(f'{ret_value}')
        elif sender == self.button4:
            ret_item, is_ok = QInputDialog.getItem(
                    self,
                    "Input Item",
                    "Select your favorite",
                    ["fait","hope","love"],
                    0,
                    )
            print(type(ret_item), type(is_ok))
            if is_ok:
                self.ret_label.setText(f'{ret_item}')
        elif sender == self.button5:
            ret_path, is_ok = QFileDialog.getOpenFileName(
                    self,
                    "open file",
                    "./",
                    )
            print(type(ret_path), type(is_ok))
            if is_ok:
                self.ret_label.setText(f'{ret_path}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())



