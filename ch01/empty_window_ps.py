# basic_window.py
# Import necessary modules
import sys

PY_SIDE6 = True
try:
    import PySide6.QtCore
    from PySide6.QtWidgets import (QApplication, QWidget,
                                   QLabel)
except:
    PY_SIDE6 = False

PYQT = True
try:
    import PyQt6.QtCore
    from PyQt6.QtWidgets import (QApplication, QWidget,
                                 QLabel)
except:
    PYQT6 = False

class MW(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        """set up the application."""
        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle("Main Window in PyQt or PySide. 한글.")
        self.setup_main_wnd()
        self.show() # Display the window on the screen
        
    def setup_main_wnd(self):
        """set up the main window."""
        hello_label = QLabel(self)
        hello_label.setText('Hello, World and Qt!')
        hello_label.move(150,90)

# Run the program
if __name__ == '__main__':
    if PY_SIDE6:
        print(PySide6.__version__)
        print(PySide6.QtCore.__version__)
    if PYQT6:
        print(PyQt6.QtCore.qVersion())

    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())
