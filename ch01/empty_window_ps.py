# basic_window.py
# Import necessary modules
import sys
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        """Set up the application."""
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Empty Window in PyQt")
        self.show() # Display the window on the screen

# Run the program
if __name__ == '__main__':
    print(PySide6.__version__)
    print(PySide6.QtCore.__version__)
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())
