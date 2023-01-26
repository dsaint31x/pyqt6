# change_icons.py 
# Import necessary modules 

import sys, random

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout,
QMessageBox) 

from PyQt6.QtCore import Qt, QSize 
from PyQt6.QtGui import QIcon 
 
class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self): 
        """Set up the application's GUI.""" 
        self.setMinimumSize(200, 200) 
        self.setWindowTitle("Changing Icons Example")
        
        self.setWindowIcon(QIcon("img/pyqt_logo.png")) 
        #self.setUpMainWindow() 
        self.show()
        QMessageBox.about(self, "About QMessageBox", """<p>안녕하세요.</p> <p>MMMIL</p>""")  
    
if __name__ == '__main__': 
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())