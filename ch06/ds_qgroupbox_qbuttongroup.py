import sys, os
from PyQt6.QtWidgets import (QApplication, QWidget, 
                             QRadioButton, QCheckBox, QButtonGroup,
                             QHBoxLayout,QVBoxLayout,
                             QGroupBox)
from PyQt6.QtCore import Qt

class MW (QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setMinimumSize(400,200)
        self.setWindowTitle("QGroupBox Ex")
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        
        lm = QHBoxLayout()
        self.checks = QGroupBox("QCheckBox Grp")
        self.checks.setCheckable(True)
        self.checks.setChecked(False)
        self.radios = QGroupBox("QRadioButton Grp")
        lm.addWidget(self.checks)
        lm.addWidget(self.radios)
        
        self.set_checks()
        self.set_radios()
        
        self.setLayout(lm)
    
    def set_checks(self):
        
        lm = QVBoxLayout()
        
        self.button_grp_checks = QButtonGroup()
        for idx in range(3):
            cb = QCheckBox(f"check {idx}")
            self.button_grp_checks.addButton(cb)
            lm.addWidget(cb)
        self.checks.setLayout(lm)
        self.button_grp_checks.setExclusive(False)
        self.button_grp_checks.buttonClicked.connect(self.toggle_check_box)
        self.checks.clicked.connect(self.clk_checks)
        
    def set_radios(self):
        
        lm = QVBoxLayout()
        self.button_grp_radios = QButtonGroup()
        for idx in range(3):
            rb = QRadioButton(f"radio {idx}")
            self.button_grp_radios.addButton(rb)
            lm.addWidget(rb)
        self.radios.setLayout(lm)
        self.button_grp_radios.setExclusive(False)
        self.button_grp_radios.buttonClicked.connect(self.toggle_radio_btn)
        self.radios.clicked.connect(self.clk_radios)
    
    def toggle_check_box(self, state):
        # if state:
        #     print(self.sender().text())
            
        for c in self.button_grp_checks.buttons():
            # if c.checkState() == Qt.CheckState.Checked:
            if c.isChecked():
                print(c.text())
                
        print("======================")    
        print(self.button_grp_checks.checkedButton())
        print("======================")    
    def toggle_radio_btn(self, state):
        # if state:
        #     print("sender:", self.sender().text())
            
        for c in self.button_grp_radios.buttons():
            if c.isChecked():
                print(c.text())    
        print("======================")    
        print(self.button_grp_radios.checkedButton().text())
        print("======================")    
                   
    def clk_checks(self, checked):
        print("checks!")
        print(checked)
    def clk_radios(self, button):
        print("radios!")
        print(button)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())             