# -*- coding: utf-8 -*-
#
# ex_qmain_window.py
#
# Description: QMainWindow를 상속받아 메인 윈도우를 생성하고,
#              Central Widget을 설정하는 방법을 보여주는 예제입니다.
# Author: [작성자 이름 또는 조직명]
# Date: 2026-02-23
#

# 1. 필요한 library 및 module을 import 하기
import sys
import os

# PySide6/PyQt6 사용을 확인하기 위한 flag
PYSIDE = False
PYQT = False

# PySide6를 우선적으로 import 하도록 시도
try:
    from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                                   QLabel, QVBoxLayout)
    from PySide6.QtGui import QIcon
    PYSIDE = True
except ImportError:
    pass

# PySide6 import에 실패했을 경우, PyQt6를 import 하도록 시도
if not PYSIDE:
    try:
        from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                                     QLabel, QVBoxLayout)
        from PySide6.QtGui import QIcon
        PYQT = True
    except ImportError:
        pass

# QMainWindow를 상속받아 메인 윈도우 class를 정의
class MW(QMainWindow):
    def __init__(self):
        """ 생성자(Constructor) """
        # 부모 class인 QMainWindow의 생성자를 호출
        super().__init__()
        # UI 초기화를 위해 user-defined method 호출
        self.initialize_ui()
        
    def initialize_ui(self):
        """Application의 UI 설정을 담당"""

        # 윈도우의 최소 크기를 400x500으로 설정
        self.setMinimumSize(400, 500) #width, height
        # 윈도우의 title bar에 보일 text를 설정
        self.setWindowTitle("Title of Main Window")
        
        # 아이콘 이미지 경로 설정
        # os.path.join을 사용하여 OS에 맞는 경로 구분자로 경로를 조합
        # __file__은 현재 스크립트의 절대 경로를 나타냄
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img/pyqt_logo.png')
        # QIcon을 사용하여 윈도우 아이콘을 설정
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # 메인 윈도우의 central widget을 설정하는 method 호출
        self.setup_main_wnd()

        # 설정된 윈도우를 화면에 표시
        self.show()
        
    def setup_main_wnd(self):
        """메인 윈도우의 Central Widget을 생성 및 설정"""
        
        # 1번 과정: Central Widget에 포함될 자식 widget들을 생성
        label0 = QLabel("test0")
        label1 = QLabel("test1")
        
        # 2번 과정: 자식 widget들을 배치할 Layout Manager를 생성 (QVBoxLayout: 수직 정렬)
        vbox = QVBoxLayout()
        
        # 3번 과정: Layout Manager에 자식 widget들을 추가
        vbox.addWidget(label0)
        vbox.addWidget(label1)
        
        # 4번 과정: 자식 widget들과 layout을 담을 container widget(QWidget)을 생성
        container = QWidget()
        
        # 5번 과정: container widget의 layout을 2번 과정에서 만든 vbox로 설정
        container.setLayout(vbox)
        
        # 6번 과정: 메인 윈도우의 Central Widget으로 container widget을 설정
        self.setCentralWidget(container)
        
# 3. Main script로 동작하는 루틴 구현
if __name__ == '__main__':
    # PySide6나 PyQt6 모두 사용 불가능할 경우 메시지 출력 후 종료
    if not PYSIDE and not PYQT:
        print("Neither PySide6 nor PyQt6 is available. Please install one.")
        sys.exit(1)

    # 모든 GUI app은 하나의 QApplication instance를 필요로 함
    app = QApplication(sys.argv)
    # Main window(MW)의 instance를 생성
    window = MW()
    # application의 event loop를 시작
    sys.exit(app.exec())
