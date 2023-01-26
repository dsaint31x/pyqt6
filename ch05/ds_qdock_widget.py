import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QWidget,
                             QVBoxLayout,
                             QDockWidget, QLabel, QPushButton)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction

class MW (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setFixedSize(600,600)
        self.setWindowTitle("ds QDockWidget")
        self.setup_main_wnd()
        # self.create_actions()
        self.create_dock_widget()
        self.create_menu()
        self.show()
        
    def setup_main_wnd(self):
        self.label = QLabel("QDockWidget")
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.setCentralWidget(self.label)
        
    def create_dock_widget(self):
        self.dock_widget = QDockWidget()
        self.dock_widget.setWindowTitle("The 1st dockwidget")
        self.dock_widget.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea |
            Qt.DockWidgetArea.RightDockWidgetArea
        )
        
        d_label = QLabel("label 0")
        self.d_btn = QPushButton("test")
        self.d_btn.setMinimumSize(QSize(100,50))
        self.d_btn.clicked.connect(self.test_clicked)
        
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(d_label)
        dock_v_box.addWidget(self.d_btn)
        
        container = QWidget()
        container.setLayout(dock_v_box)
        
        self.dock_widget.setWidget(container)
        
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea,
                           self.dock_widget)
        
        self.toggle_dock_act = self.dock_widget.toggleViewAction()
    
    def create_menu(self):
        
        mb = self.menuBar()
        mb.setNativeMenuBar(False)
        
        toggle_menu = mb.addMenu("dock widget")
        toggle_menu.addAction(self.toggle_dock_act)
        
    def test_clicked(self):
        if self.label.text() == "text":
            self.label.setText("ok")
        else:
            self.label.setText("text")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())    
            
    
        
        
         
        
    
    