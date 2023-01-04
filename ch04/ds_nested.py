import sys

from PyQt6.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout,
                             QLabel,
                             QComboBox, QSpinBox,
                             QMessageBox)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
        
    def init_ui(self):
        self.setWindowTitle('Ex - NestedLayout')
        self.setMinimumSize(512,128)
        self.setup_main_window()
        self.show()
        
    def setup_main_window(self):
        top_label = QLabel(
            "Select 3 important item for your life and "+
            "their importance score!"
        )
        top_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        top_label.setFont(QFont('Bold', 10))
        
        item_lst = ['faith', 'hope', 'love', 'money', 'health']
        self.items = []
        self.scores = []
        main_wnd_layout = QVBoxLayout()
        
        main_wnd_layout.addWidget(top_label)
        
        for i in range(3):
            c_cb = QComboBox()
            c_cb.addItems(item_lst)
            self.items.append(c_cb)
            c_sb = QSpinBox()
            c_sb.setRange(0,100)
            c_sb.setSuffix('pnt')
            c_sb.valueChanged.connect(
                self.cal_total
            )
            self.scores.append(c_sb)
            
            c_h_box = QHBoxLayout()
            c_h_box.addWidget(c_cb)
            c_h_box.addWidget(c_sb)
            
            main_wnd_layout.addLayout(c_h_box)
        
        self.totals_label = QLabel('Total score: pnt')
        self.totals_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )
        
        main_wnd_layout.addWidget(self.totals_label)
        
        self.setLayout(main_wnd_layout)
        
    def cal_total(self,val):
        total = 0
            
        if total > 100:
            QMessageBox.warning(
                self,
                "Warning",
                f"""<p> Sum is above 100pnt""",
                QMessageBox.StandardButton.Ok
            )
            
        self.totals_label.setText(f'Total score: {total}pnt')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
