# labels.py
#
# Setting up the main window to show how to use QLabel widgets


# Import necessary modules.
import sys, os

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        """Set up the appliation's GUI"""
        self.setGeometry(100,100,250,250)
        self.setWindowTitle('QLabel Example')
        self.setUpMainWindow()
        self.show()
        
    def setUpMainWindow(self):
        hello_label = QLabel(self)
        hello_label.setText('Hello')
        hello_label.move(105,15)
        
        path_py_file = os.path.realpath(__file__)
        path_py_file = os.path.dirname(path_py_file)
        img_fstr = os.path.join(path_py_file,'img/world.png')
        try:
            with open(img_fstr):
                world_label = QLabel(self)
                pixmap = QPixmap(img_fstr)
                world_label.setPixmap(pixmap)
                world_label.move(25,40)
        except FileNotFoundError as err:
            print(f'Image not found.\nError: {err}')
            
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())