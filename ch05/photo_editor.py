# import necessary moudles
import sys, os

from PyQt6.QtWidgets import ( QApplication,
                             QMainWindow, QWidget, 
                             QLabel, QPushButton, 
                             QDockWidget, QDialog,
                             QFileDialog, QMessageBox, QToolBar,
                             QStatusBar, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize, QRect
from PyQt6.QtGui import (QIcon, QAction, QPixmap,
                         QTransform, QPainter)
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog

class MW (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Set up the application's GUI"""
        
        self.fpath = os.path.dirname(
            os.path.abspath(__file__)
        )
        
        self.setFixedSize(650,650)
        self.setWindowTitle("5.2- Photo Editor GUI")
        self.setup_main_wnd()
        self.create_tools_dock_widget() # toggle_dock_tools_act를 생성.
        self.create_actions()          
        self.create_menu()
        self.create_toolbar()
        self.show()
        
    def setup_main_wnd(self):
        """Create and arrange widgets in the main wnd"""
        self.img = QPixmap()
        self.img_label = QLabel()
        self.img_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.setCentralWidget(self.img_label)
        
        # Create the status bar
        self.setStatusBar(QStatusBar())
        
        
    def create_actions(self):
        """Create and applicaion's menu actions."""
        
        # Create actions for File menu
        self.open_act = QAction(
            QIcon(f"{self.fpath}/img/open_file.png"), "Open"
        )
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.setStatusTip("Open a new image")
        # self.open_act.triggered.connect(self.openImg)
        
        self.save_act = QAction(
            QIcon(f"{self.fpath}/img/save_file.png"), "Save"
        )
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.setStatusTip("Save image")
        # self.save_act.triggered.connect(self.saveImg)
        
        self.print_act = QAction(
            QIcon(f"{self.fpath}/img/print.png"), "Print"
        )
        self.print_act.setShortcut("Ctrl+P")
        self.print_act.setStatusTip("Print image")
        # self.print_act.triggered.connect(self.printImg)
        self.print_act.setEnabled(False)
        
        self.quit_act = QAction(
            QIcon(f"{self.fpath}/img/exit.png"), "Quit"
        )
        
        # Create actions for Edit menu
        self.rotate90_act = QAction("Rotate 90°")
        self.rotate90_act.setStatusTip(
            "Rotate image 90° clockwise")
        # self.rotate90_act.triggered.connect(
        #     self.rotateImage90)
        self.rotate180_act = QAction("Rotate 180°")
        self.rotate180_act.setStatusTip(
            "Rotate image 180° clockwise")
        # self.rotate180_act.triggered.connect(
        #     self.rotateImage180)
        self.flip_hor_act = QAction("Flip Horizontal")
        self.flip_hor_act.setStatusTip(
            "Flip image across horizontal axis")
        # self.flip_hor_act.triggered.connect(
        #     self.flipImageHorizontal)
        self.flip_ver_act = QAction("Flip Vertical")
        self.flip_ver_act.setStatusTip(
            "Flip image across vertical axis")
        # self.flip_ver_act.triggered.connect(
        #     self.flipImageVertical)
        self.resize_act = QAction("Resize Half")
        self.resize_act.setStatusTip(
            "Resize image to half the original size")
        # self.resize_act.triggered.connect(
        #     self.resizeImageHalf)
        self.clear_act = QAction(
            QIcon(f"{self.fpath}/img/clear.png"), "Clear Image")
        self.clear_act.setShortcut("Ctrl+D")
        self.clear_act.setStatusTip("Clear the current image")
        # self.clear_act.triggered.connect(self.clearImage)
        
        
    def create_menu(self):
        """Create the application's menu bar.
        """
        mb = self.menuBar()
        # mb.setNativeMenuBar(False)
        mb.setNativeMenuBar(True)
        
        # Create File menu and add actions
        file_menu = mb.addMenu("File")
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.print_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)
        
        # Create Edit menu and add actions
        edit_menu = self.menuBar().addMenu("Edit")
        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.rotate180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flip_hor_act)
        edit_menu.addAction(self.flip_ver_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_act)
        
        # Create View menu and add actions
        view_menu = self.menuBar().addMenu("View")
        view_menu.addAction(self.toggle_dock_tools_act)
        
    def create_toolbar(self):
        """Crete the application's toolbar."""
        toolbar = QToolBar("Photo Eidtor Toolbar")
        toolbar.setIconSize(QSize(24,24))
        self.addToolBar(toolbar)
        
        # Add actions to the toolbar
        toolbar.addAction(self.open_act)
        toolbar.addAction(self.save_act)
        toolbar.addAction(self.print_act)
        toolbar.addAction(self.clear_act)
        toolbar.addSeparator()
        toolbar.addAction(self.quit_act)
    
    def create_tools_dock_widget(self):
        """Create the application's dock widget. 
        Use View -> Edit Image Tools 
        menu to show/hide the dock."""
        self.dock_widget = QDockWidget()
        self.dock_widget.setWindowTitle("Edit Image Tools")
        self.dock_widget.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea |
            Qt.DockWidgetArea.RightDockWidgetArea
        )
        
        # Create buttons for editing images
        self.rotate90 = QPushButton("Rotate 90˚")
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.setStatusTip("Rotate image 90º clockwise")
        # self.rotate90.clicked.connect(self.rotateImage90)

        self.rotate180 = QPushButton("Rotate 180º")
        self.rotate180.setMinimumSize(QSize(130, 40))
        self.rotate180.setStatusTip("Rotate image 180º clockwise")
        # self.rotate180.clicked.connect(self.rotateImage180)

        self.flip_horizontal = QPushButton("Flip Horizontal")
        self.flip_horizontal.setMinimumSize(QSize(130, 40))
        self.flip_horizontal.setStatusTip("Flip image across horizontal axis")
        # self.flip_horizontal.clicked.connect(self.flipImageHorizontal)

        self.flip_vertical = QPushButton("Flip Vertical")
        self.flip_vertical.setMinimumSize(QSize(130, 40))
        self.flip_vertical.setStatusTip("Flip image across vertical axis")
        # self.flip_vertical.clicked.connect(self.flipImageVertical)

        self.resize_half = QPushButton("Resize Half")
        self.resize_half.setMinimumSize(QSize(130, 40))
        self.resize_half.setStatusTip("Resize image to half the original size")
        # self.resize_half.clicked.connect(self.resizeImageHalf) 

        # Create layout for dock widget 
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        dock_v_box.addWidget(self.rotate180)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.flip_horizontal)
        dock_v_box.addWidget(self.flip_vertical)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize_half)
        dock_v_box.addStretch(10)

        # Create QWidget that acts as a container and
        # set the layout for the dock
        tools_contents = QWidget()
        tools_contents.setLayout(dock_v_box)
        self.dock_widget.setWidget(tools_contents)
        
        # Set initial location of dock widget
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, 
            self.dock_widget)

        # Handle the visibility of the dock widget
        self.toggle_dock_tools_act = self.dock_widget.toggleViewAction()
    
        
        
    
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(
        Qt.ApplicationAttribute.AA_DontShowIconsInMenus, True
    )
    wnd = MW()
    sys.exit(app.exec())
    
