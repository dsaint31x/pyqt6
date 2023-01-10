import sys

from PyQt6.QtWidgets import (QApplication, QWidget,
                             QLabel,
                             QVBoxLayout,
                             QLineEdit)
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


        self.le = QLineEdit()
        self.le.setMaxLength(10) # 10글자 제한.
        self.le.textChanged.connect(self.on_changed)
        self.le.textEdited.connect(self.on_edited)
        self.le.editingFinished.connect(self.on_editing_finished)
        lm.addWidget(self.le)

        
        self.dp_label0 = QLabel()
        lm.addWidget(self.dp_label0)
        self.dp_label1 = QLabel()
        lm.addWidget(self.dp_label1)
        self.dp_label2 = QLabel()
        lm.addWidget(self.dp_label2)
        
        self.setLayout(lm)
    
    def on_changed(self, text):
        tmp = "textChanged:"
        tmp += text 
        self.dp_label0.setText(tmp)
    
    def on_edited(self, text):
        tmp = "textEdited:"
        tmp += text 
        self.dp_label1.setText(tmp)
    
    def on_editing_finished(self):
        tmp = "editingFinished"
        tmp += self.le.text() 
        self.dp_label2.setText(tmp)
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
    
    
        
        
                              
