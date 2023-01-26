import sys,os
from PyQt6.QtWidgets import (QApplication, QMainWindow,
    QWidget, QLabel, QVBoxLayout)

from PyQt6.QtGui import QPixmap, QKeyEvent
from PyQt6.QtCore import Qt, pyqtSignal, QObject, QSize

class DsSignal(QObject):
    """Define a signal, change_pixmap, that takes no arguments."""
    change_pixmap = pyqtSignal(int)

class MW(QMainWindow):
    change_pixmap = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Set up the application's GUI."""
        self.fstr = os.path.dirname(
            os.path.abspath(__file__)
        )
        """Define a signal, change_pixmap, that takes no arguments."""
        self.setGeometry(100,100, 200, 300)
        self.setWindowTitle("Custom Signals Ex")
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        self.idx = 0
        
        # create instance of DsSignal class
        # self.signal = DsSignal()
        # self.signal.change_pixmap.connect(self.change_pixmap_handler)
        self.change_pixmap.connect(self.change_pixmap_handler)
        
        lm = QVBoxLayout()
        
        info_label = QLabel("<p>Press <i>+</i> key or <i>-</i> key to change image</p>")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lm.addWidget(info_label)
        
        self.img_label = QLabel()
        pixmap = QPixmap(f"{self.fstr}/img/0.png")
        self.img_label.setPixmap(pixmap.scaled(
            QSize(180,250),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
        self.img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lm.addWidget(self.img_label)
        
        container = QWidget()
        container.setLayout(lm)
        
        self.setCentralWidget(container)
        
    
    def keyPressEvent(self, a0: QKeyEvent) -> None:
        
        print(a0.key())
        
        if a0.key() == Qt.Key.Key_Plus:
            # self.signal.change_pixmap.emit(1)
            self.change_pixmap.emit(1)
        elif a0.key() == Qt.Key.Key_Minus:
            # self.signal.change_pixmap.emit(-1)
            self.change_pixmap.emit(-1)
        
        return super().keyPressEvent(a0) 
    
    def change_pixmap_handler(self, offset):
        self.idx = (self.idx + offset) % 10
        if self.idx <0 :
            self.idx = 9
        print(self.idx)
        pixmap = QPixmap(f"{self.fstr}/img/{self.idx}.png")
        self.img_label.setPixmap(pixmap.scaled(
            QSize(180,250),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())