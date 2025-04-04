# first_dlg.py

import sys
from PySide6.QtWidgets import ( QApplication,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout, QLabel,
    QMainWindow,
    QPushButton,
)

class MW(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog Ex.")

        button = QPushButton("Press it for a Dialog")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)
        dlg = QDialog(self) 
        dlg.setWindowTitle("QDialog Title") 
        # dlg.exec()
        dlg.open()
        
        # -------------
        # for custom dlg
        # dlg = CustomDlg(self)
        # if dlg.exec(): # Modal Dialog
        #     print('ok')
        # else:
        #     print("cancel")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    app.exec()