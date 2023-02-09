# labels.py

# ================================================
# Import necessary modules.
import sys, os

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont,QPixmap
from PyQt6.QtCore import Qt

# ================================================
# 주요 클래스 정의
class MW(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        """Set up the appliation's GUI"""
        self.setGeometry(100,100,250,200)
        self.setFixedSize(250,200)
        self.setWindowTitle('QLabel Example')
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        """Set up the Main Window"""

        # hello_label = QLabel('Hello, World and Qt!',self) # 아래 두라인과 동일한 수행.
        hello_label = QLabel(self)
        hello_label.setText('Hello, World and Qt!')
        hello_label.setFont(QFont('Arial',15))

        # 아래 두 줄을 주석해제하여 동작을 확인해 볼것.
        # hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        # hello_label.setStyleSheet("background-color: yellow")
        hello_label.move(10,10)
        
        path_py_file = os.path.realpath(__file__)
        path_py_file = os.path.dirname(path_py_file)
        img_fstr = os.path.join(path_py_file,'img/world.png')
        try:
            with open(img_fstr):
                world_label = QLabel(self)
                pixmap = QPixmap(img_fstr)
                pixmap = pixmap.scaled(200,200, Qt.AspectRatioMode.KeepAspectRatio)
                world_label.setPixmap(pixmap)
                world_label.move(25,40)
        except FileNotFoundError as err:
            print(f'Image not found.\nError: {err}')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
