import sys, os

from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QToolBar, QLabel)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction,QIcon

class MW (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.fpath = os.path.dirname(
            os.path.abspath(__file__)
        )
        self.setFixedSize(600,600)
        self.setWindowTitle("ds toolbar")
        self.setup_main_wnd()
        self.create_actions()
        self.create_tool_bar()
        self.create_menu()
        self.show()
        
    def setup_main_wnd(self):
        self.label = QLabel("QToolBar")
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.setCentralWidget(self.label)
        
    def create_actions(self):
        self.open_act = QAction(
            QIcon(f"{self.fpath}/img/open_file.png"),
            "Open"
        )
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.triggered.connect(
            self.open_event
        )
        
        self.close_act = QAction(
            QIcon(f"{self.fpath}/img/clear.png"),
            "Close"
        )
        self.close_act.setShortcut("Ctrl+X")
        self.close_act.triggered.connect(
            self.close
        )
        
    def create_tool_bar(self):
        tool_bar = QToolBar("QToolBar Test")
        tool_bar.setIconSize(QSize(30,30))
        
        tool_bar.addAction(self.open_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.close_act)
        
        self.addToolBar(tool_bar)
    
    def create_menu(self):
        
        mb = self.menuBar()
        mb.setNativeMenuBar(False)
        
        open_menu = mb.addMenu("Open")
        open_menu.addAction(self.open_act)
        
    def open_event(self):
        if self.label.text() != "open clicked ok":
            self.label.setText("open clicked ok")
        else:
            self.label.setText("open clicked ok again")
    
    # def close_event(self):
    #     self.label.setText("close clicked ok")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())    