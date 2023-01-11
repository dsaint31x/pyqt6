import sys

from PyQt6.QtWidgets import (QApplication, QWidget,
        QFormLayout,
        QLabel,
        QLineEdit, QTextEdit, QDateEdit,
        QComboBox,
        QPushButton)

from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont

class MW (QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #self.setMinimumSize(700,400)
        self.setWindowTitle("Ex Input Widgets")
        self.setup_main_wnd()
        self.show()
    # --------------------------------------------

    def setup_main_wnd(self):

        top_label = QLabel("입력 widget들")
        top_label.setFont(QFont("Arial", 16))
        top_label.setAlignment(
                Qt.AlignmentFlag.AlignCenter)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("place hoder text")
        self.line_edit.textEdited.connect(self.clear_text)
        
        self.le_mask = QLineEdit()
        self.le_mask.setPlaceholderText("input mask 사용법(전화번호 형태)")
        self.le_mask.setInputMask("(099) 0999-9999;x")
        self.le_mask.textEdited.connect(self.clear_text)

        self.date_edit = QDateEdit()
        self.date_edit.setDisplayFormat("yyyy/MM/dd")
        self.date_edit.setMaximumDate(
                QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())


        self.combo_box = QComboBox()
        self.combo_box.addItems(["1학년", "2학년", "3학년", "4학년"])

        self.text_edit = QTextEdit()


        self.dp_str_label = QLabel()

        push_button = QPushButton("print")
        push_button.setMaximumWidth(150)
        push_button.clicked.connect(self.ck_form)

        #----------------------------
        form_lm = QFormLayout()
        form_lm.setFieldGrowthPolicy(
                #form_lm.FieldGrowthPolicy.AllNonFixedFieldsGrow)
                #form_lm.FieldGrowthPolicy.ExpandingFieldsGrow)
                form_lm.FieldGrowthPolicy.FieldsStayAtSizeHint)
        form_lm.setFormAlignment(
                Qt.AlignmentFlag.AlignHCenter | \
                Qt.AlignmentFlag.AlignBottom)
        form_lm.setLabelAlignment(
                Qt.AlignmentFlag.AlignLeft)

        form_lm.addRow(top_label)
        form_lm.addRow("QlineEdit0", self.line_edit)
        form_lm.addRow("QLineEdit1", self.le_mask)
        form_lm.addRow("QDateEdit" , self.date_edit)
        form_lm.addRow("QComboBox" , self.combo_box)

        form_lm.addRow(QLabel("QTextEdit"))
        form_lm.addRow(self.text_edit)
        form_lm.addRow(push_button)

        form_lm.addRow(self.dp_str_label)

        self.setLayout(form_lm)

    def clear_text(self, text):
        self.dp_str_label.clear()

    def ck_form(self):
        dp_str = ""
        if self.line_edit.text() == "":
            dp_str += "[INFO] Missing line_edit0\n"
        if self.le_mask.hasAcceptableInput() == False:
            dp_str += "[INFO] line_edit1 entered incorrectly.\n"

        self.dp_str_label.setText(dp_str)



        






# ------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wdw = MW()
    sys.exit(app.exec())


