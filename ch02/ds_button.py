# ds_button.py

# ================================================
# Import necessary modules.
import sys, os

PYSIDE6_MODE = True
PYQT_MODE = False

try:
    from PySide6.QtWidgets import (QApplication, QWidget, 
                                QLabel, QPushButton)
    from PySide6.QtGui import QFont,QIcon
    from PySide6.QtCore import Qt,QSize
except Exception as e:
    print(f"PySide6 import failed: {e}")
    PYSIDE6_MODE = False
    PYQT_MODE = True

if not PYSIDE6_MODE:
    try:
        from PyQt6.QtWidgets import (QApplication, QWidget, 
                                    QLabel, QPushButton)
        from PyQt6.QtGui import QFont,QIcon
        from PyQt6.QtCore import Qt,QSize
    except Exception as e:
        print(f"PyQt6 import failed: {e}")
        PYQT_MODE = False

if not PYSIDE6_MODE and not PYQT_MODE:
    print("No availabe Qt Binding found! Plz install PySide6 or PyQt6.")
    sys.exit(1)

# ================================================
# 주요 클래스 정의
class MW(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Set up the application's GUI"""
        #self.setFixedSize(250,250)
        self.setWindowTitle('QPushButton Example')
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        """Set up the Main Window"""

        # self.hello_label = QLabel('Hello, World and Qt!',self) # 아래 두라인과 동일한 수행.
        self.hello_label = QLabel(self)
        self.hello_label.setText('Hello, World and Qt!')
        self.hello_label.setFont(QFont('Arial',15))

        self.hello_label.resize(230,40)

        # 아래 code line을 적절히 주석해제하여 동작을 확인해 볼것.
        # self.hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter) # PyQt 
        # self.hello_label.setAlignment(Qt.AlignCenter)               # PySide6
        # self.hello_label.setStyleSheet("background-color: yellow")  # both

        # -----------------
        self.hello_label.move(10,20)
        
        path_py_file = os.path.realpath(__file__)
        path_py_file = os.path.dirname(path_py_file)
        img_fstr = os.path.join(path_py_file,'img/world.png')
        
        it_button = QPushButton("icon and text button",self)
        it_button.setIcon(QIcon(img_fstr))
        it_button.clicked.connect(self.it_btn_clicked)
        it_button.resize(150,50)
        it_button.move(50,70)
        
        icon_button = QPushButton(self)
        icon_button.setIcon(QIcon(img_fstr))
        icon_button.clicked.connect(self.icon_btn_clicked)
        icon_button.setIconSize (QSize(120,30))
        icon_button.resize(150,50)
        icon_button.move(50,130)
        
        
        text_button = QPushButton("icon button",self)
        text_button.clicked.connect(self.text_btn_clicked) 
        text_button.resize(150,50)
        text_button.move(50,190)
    
    def it_btn_clicked(self):
        self.hello_label.setText("Icon and txt Button")
        
    def icon_btn_clicked(self):
        self.hello_label.setText("Icon Button")
        
    def text_btn_clicked(self):
        self.hello_label.setText("text Button")
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
