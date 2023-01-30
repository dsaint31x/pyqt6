import os, sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QHBoxLayout, QVBoxLayout,
                             QTabWidget, 
                             QRadioButton, QGroupBox, QLineEdit)

class MW (QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setMinimumSize(400,300)
        self.setWindowTitle("Container Ex")
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        tab_bar = QTabWidget(self)
        self.prof_details_tab = QWidget() # container0
        self.background_tab = QWidget() # container1
        tab_bar.addTab(self.prof_details_tab,"Profile Details")
        tab_bar.addTab(self.background_tab,"Background")
        
        self.set_prof_details_tab()
        self.set_background_tab()
        
        main_lm = QHBoxLayout()
        main_lm.addWidget(tab_bar)
        self.setLayout(main_lm)
        
    def set_prof_details_tab(self):
        n_label = QLabel("name")
        n_edit = QLineEdit()
        a_label = QLabel("address")
        a_edit = QLineEdit()
        
        male_rb = QRadioButton("Male")
        female_rb = QRadioButton("Female")
        
        gender_box = QHBoxLayout()
        gender_box.addWidget(male_rb)
        gender_box.addWidget(female_rb)
        gender_gb = QGroupBox("Gencer")
        gender_gb.setLayout(gender_box)
        
        lm = QVBoxLayout()
        lm.addWidget(n_label)
        lm.addWidget(n_edit)
        lm.addStretch()
        lm.addWidget(a_label)
        lm.addWidget(a_edit)
        lm.addStretch()
        lm.addWidget(gender_gb)
        
        self.prof_details_tab.setLayout(lm)
        
    def set_background_tab(self):
        lm = QVBoxLayout()
        
        ed_list = ["High School Diploma",
                   "Associate's Degree",
                   "Bachelor's Degree",
                   "Master's Degree",
                   "Doctorate or Higher"]
        
        for e in ed_list:
            self.e_rb = QRadioButton(e)
            lm.addWidget(self.e_rb)
            
        self.e_gb = QGroupBox("Highest Level of Education")
        self.e_gb.setLayout(lm)
        
        v_lm = QVBoxLayout()
        v_lm.addWidget(self.e_gb)
        self.background_tab.setLayout(v_lm)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())        