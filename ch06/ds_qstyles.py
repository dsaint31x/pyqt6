import sys, os
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QRadioButton, QCheckBox,
                             QTabWidget, QGroupBox, QButtonGroup,
                             QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QPixmap

style_sheet = """
    QWidget {
        background-color: #21C908;
    }
    QWidget#Tab{
        background-color: #EBFCCD;
        border-radius: 8px;
    }
    QWidget#Feedback{
        background-color: #D0EF96;
        broder-radius: 9px;
    }
    QLabel {
        background-color: #D0EF96;
        border-width: 4px;
        border-style: solid;
        border-radius: 10px;
        border-color: #EEFDEE;
    }
    QLabel#Title {
        background-color: #D0EF96;
        border-width: 2px;
        border-style: solid;
        border-radius: 4px;
        border-color: #D0EF96;
        padding-left: 10px;
        color: #1A9607
    }
    QGroupBox{
        Background-color: #EBFCCD;
        color: #1A9607;
    }
    QCheckBox {
        background-color: #F9FCF3;
    }

"""

qcheckbox_stylesheet = """
QCheckBox {
    spacing: 5px;
}
QCheckBox::indicator {
    width: 13px;
    height: 13px;
}

QCheckBox::indicator:unchecked {
    background-color: red;
    /* image: url(:/images/checkbox_unchecked.png); */
}

QCheckBox::indicator:unchecked:hover {
    /* image: url(:/images/checkbox_unchecked_hover.png); */
    background-color: yellow;
}

QCheckBox::indicator:unchecked:pressed {
    /* image: url(:/images/checkbox_unchecked_pressed.png); */
    background-color: blue;
}

QCheckBox::indicator:checked {
    /* image: url(:/images/checkbox_checked.png); */
    background-color: black;
}

QCheckBox::indicator:checked:hover {
    /* image: url(:/images/checkbox_checked_hover.png); */
    background-color: gray;
}

QCheckBox::indicator:checked:pressed {
    /* image: url(:/images/checkbox_checked_pressed.png); */
    background-color: megenta;
}

QCheckBox::indicator:indeterminate:hover {
    /* image: url(:/images/checkbox_indeterminate_hover.png); */
    background-color: tan;
}

QCheckBox::indicator:indeterminate:pressed {
    /* image: url(:/images/checkbox_indeterminate_pressed.png); */
    background-color: red;
}
"""

qgroupbox_stylesheet = """QGroupBox {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);
    border: 2px solid gray;
    border-radius: 5px;
    margin-top: 1ex; /* leave space at the top for the title */
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center; /* position at the top center */
    padding: 0 3px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #FF0ECE, stop: 1 #FFFFFF);
}
"""

qgroupbox_checkable_stylesheet = """QGroupBox::indicator {
    width: 13px;
    height: 13px;
}

QGroupBox::indicator:unchecked {
    /*image: url(:/images/checkbox_unchecked.png);*/
    background-color: yellow;
}

/* proceed with styling just like QCheckBox */
"""


class MW (QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        fstr = os.path.dirname(
            os.path.abspath(__file__)
        )
        self.setWindowTitle("QStyleSheet Ex")
        self.setMinimumSize(600,900)
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        
        main_lm = QHBoxLayout()
        
        # ------------------------------------
        # tabbar (left)
        self.tab_bar = QTabWidget()
        
        self.checks_tab = QWidget()
        self.checks_tab.setObjectName("Tab")
        self.tab_bar.addTab(self.checks_tab, "QCheckBox Tab")
        
        self.radios_tab = QWidget()
        self.radios_tab.setObjectName("Tab")
        self.tab_bar.addTab(self.radios_tab, "QRadioButton Tab")
        
        main_lm.addWidget(self.tab_bar,2)
        
        # ------------------------------------
        # feedback sidebar. (right)
        self.sidebar = QWidget()
        self.sidebar.setObjectName("Tab")
        label = QLabel("Check Signals and Slots!")
        label.setObjectName("Title")
        
        feedback = QWidget()
        feedback.setObjectName("Feedback")
        checks_label = QLabel("from QCheckBox Tab")
        self.feedback_cks = QLabel("")
        radios_label = QLabel("from QRadioButton Tab")
        self.feedback_rad = QLabel("")
        
        feedback_grid = QGridLayout()
        feedback_grid.addWidget(checks_label,0,0, Qt.AlignmentFlag.AlignRight)
        feedback_grid.addWidget(self.feedback_cks,1,0, Qt.AlignmentFlag.AlignRight)
        feedback_grid.addWidget(radios_label,2,0, Qt.AlignmentFlag.AlignRight)
        feedback_grid.addWidget(self.feedback_rad,3,0, Qt.AlignmentFlag.AlignRight)
        feedback.setLayout(feedback_grid)
        
        feedback_lm = QVBoxLayout()
        feedback_lm.addWidget(label)
        feedback_lm.addWidget(feedback)
        feedback_lm.addStretch()
        
        self.sidebar.setLayout(feedback_lm)
        
        main_lm.addWidget(self.sidebar,1)
        
        self.setLayout(main_lm)
        
        self.set_checks()
        
    def set_checks(self):
        
        cks_tab_lm = QVBoxLayout()
        self.checks_tab.setLayout(cks_tab_lm)
        
        # 00 --------------------------
        cks_lm   = QVBoxLayout()
        cks_gbox = QGroupBox()
        cks_gbox.setTitle("cks 0")
        self.cks_bg_0 = QButtonGroup()
        
        for i in range(5):
            ck = QCheckBox(f"check {i}")
            cks_lm.addWidget(ck)
            self.cks_bg_0.addButton(ck)
        desc = QLabel("desc. 0")
        cks_lm.addWidget(desc)
        cks_gbox.setLayout(cks_lm)
        
        cks_tab_lm.addWidget(cks_gbox)
        cks_tab_lm.addStretch()
        
        # 01 --------------------------
        cks_lm   = QVBoxLayout()
        cks_gbox = QGroupBox()
        cks_gbox.setTitle("cks 0")
        self.cks_bg_0 = QButtonGroup()
        
        for i in range(5):
            ck = QCheckBox(f"check {i}")
            cks_lm.addWidget(ck)
            self.cks_bg_0.addButton(ck)
            ck.setStyleSheet(qcheckbox_stylesheet)
        desc = QLabel("desc. 1")
        cks_lm.addWidget(desc)
        cks_gbox.setLayout(cks_lm)
        
        cks_tab_lm.addWidget(cks_gbox)
        cks_tab_lm.addStretch()
        
        # 02 --------------------------
        cks_lm   = QVBoxLayout()
        cks_gbox = QGroupBox()
        cks_gbox.setTitle("cks 2")
        self.cks_bg_0 = QButtonGroup()
        
        for i in range(5):
            ck = QCheckBox(f"check {i}")
            cks_lm.addWidget(ck)
            self.cks_bg_0.addButton(ck)
        desc = QLabel("desc. 2")
        cks_lm.addWidget(desc)
        cks_gbox.setLayout(cks_lm)
        cks_gbox.setStyleSheet(qgroupbox_stylesheet)
        
        cks_tab_lm.addWidget(cks_gbox)
        cks_tab_lm.addStretch()
        
        # 03 --------------------------
        cks_lm   = QVBoxLayout()
        cks_gbox = QGroupBox()
        cks_gbox.setTitle("cks 3")
        cks_gbox.setCheckable(True)
        self.cks_bg_0 = QButtonGroup()
        
        for i in range(5):
            ck = QCheckBox(f"check {i}")
            cks_lm.addWidget(ck)
            self.cks_bg_0.addButton(ck)
        desc = QLabel("desc. 3")
        cks_lm.addWidget(desc)
        cks_gbox.setLayout(cks_lm)
        cks_gbox.setStyleSheet(qgroupbox_checkable_stylesheet)
        
        cks_tab_lm.addWidget(cks_gbox)
        cks_tab_lm.addStretch()
        
    
    def set_radios(self):
        pass
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = MW()
    sys.exit(app.exec())    
        
        
