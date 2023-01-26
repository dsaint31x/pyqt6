# sytle.py
# Import necessary modules
import sys, os
from PyQt6.QtWidgets import QApplication, QStyleFactory

# Find out your OS's available styles
print(f"Keys:{QStyleFactory.keys()}")

# find out the default style applied to an application.
app = QApplication(sys.argv)
print(type(app.style()))
print(f"Default style: {app.style().name()}")

app.setStyle("Windows")
print(f"Changed style: {app.style().name()}")

