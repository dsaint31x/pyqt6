import sys

from PyQt6.QtWidgets import (QApplication, QWidget,
                             QLabel,
                             QVBoxLayout,
                             QComboBox)
from PyQt6.QtCore import Qt

class MW (QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Ex: QCheckbox")
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        lm = QVBoxLayout()
        
        lm.addWidget(QLabel('What is most important?'))

        self.items = ['faith', 'hope', 'love']

        cb = QComboBox()

        for idx,c in enumerate(self.items):
            cb.addItem(self.items[idx])

        cb.activated.connect(self.on_selected)
        lm.addWidget(cb)

        
        self.dp_label = QLabel("")
        lm.addWidget(self.dp_label)
        
        self.setLayout(lm)
    
    def on_selected(self, idx):
        tmp = "you selected :"
        tmp += self.items[idx] 
        
        print(tmp)
        self.dp_label.setText(tmp)
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
    
    
        
        
                              
