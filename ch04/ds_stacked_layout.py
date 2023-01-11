import sys, os

from PyQt6.QtWidgets import (QApplication, QWidget,
        QStackedLayout, QVBoxLayout,
        QLabel,
        QComboBox)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MW (QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #self.setMinimumSize(700,400)
        self.setWindowTitle("Ex Input Widgets")
        self.setup_main_wnd()
        self.show()
# ------------------------------------

    def setup_main_wnd (self):
        fpath = os.path.dirname(
            os.path.abspath(__file__)
        )
        pages = ['faith','hope','love']
        self.imgs = [
            os.path.join(fpath,'img/faith.png'),
            os.path.join(fpath,'img/hope.png'),
            os.path.join(fpath,'img/love.png')
        ]
        
        combo_box = QComboBox()
        combo_box.addItems(pages)
        combo_box.setCurrentIndex(2)
        combo_box.activated.connect(self.change_page)
        
        
        self.stacked_lm = QStackedLayout()
        
        for idx, c in enumerate(pages):
            label = self.setup_page(idx)
            self.stacked_lm.addWidget(label)
            
        v_box_lm = QVBoxLayout()
        v_box_lm.addWidget(combo_box)
        v_box_lm.addLayout(self.stacked_lm)
        
        self.setLayout(v_box_lm)
        
    def setup_page(self , page_num):
        
        label = QLabel()
        pixmap = QPixmap(self.imgs[page_num])
        label.setPixmap(pixmap)
        label.setScaledContents(True) # label에 포함된 image가 resize되도록 설정.
        
        return label
    
    def change_page(self, idx):
        self.stacked_lm.setCurrentIndex(idx)

# ------------------------------------
if __name__ == "__main__":
    print(os.path.realpath(__file__))
    app = QApplication(sys.argv)
    wdw = MW()
    sys.exit(app.exec())
