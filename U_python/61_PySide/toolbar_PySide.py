import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow, QLabel, QToolBar, QStatusBar

#-------------------------------------------------------------------

class MainWindow(QMainWindow): 
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('Toolbar in PySide')

        label = QLabel('Hello')
        label.setAlignment(Qt.AlignCenter)

        tool_bar = QToolBar('My Tool Bar')
        self.addToolBar(tool_bar)
        tool_bar.setIconSize(QSize(16, 16))
        # tool_bar.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        # tool_bar.setToolButtonStyle(Qt.ToolButtonTextOnly)
        # tool_bar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        # tool_bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.setStatusBar(QStatusBar(self))

        # Action of New File.
        new_button = QAction('New', self)
        tool_bar.addAction(new_button)
        new_button.setStatusTip('New File')
        new_button.triggered.connect(self.new_button_click)
        # new_button.setCheckable(True)

        # Action of Save File.
        save_button = QAction('Save', self )
        tool_bar.addAction(save_button)
        save_button.setStatusTip('Saving File')
        save_button.triggered.connect(self.save_button_click)
        
        # Action of About.
        about_button = QAction('About', self)
        about_button.setStatusTip('About this program.')
        about_button.triggered.connect(self.about_button_click)
        
        # Action of Exit.
        exit_button = QAction('Exit', self)
        tool_bar.addAction(exit_button)
        exit_button.setStatusTip('Exit')

        # tool_bar.addSeparator()
        # tool_bar.addWidget(QCheckBox())
        # tool_bar.addWidget(QLabel('Exit'))

        # Menus.
        menu = self.menuBar()
        file_menu = menu.addMenu('File')
        file_menu.addAction(new_button)
        file_menu.addAction(save_button)
        file_menu.addSeparator()
        file_menu.addAction(exit_button)

        help_menu = menu.addMenu('Help')
        help_menu.addAction(about_button)

        # Submenu.
        file_menu.addMenu(help_menu)

        # Shortcuts.
        # new_button.setShortcut(QKeySequence('Ctrl+n'))
        # about_button.setShortcut(QKeySequence('Ctrl+h'))
        new_button.setShortcut(Qt.CTRL | Qt.Key_N)
        save_button.setShortcut(Qt.CTRL | Qt.Key_S)
        about_button.setShortcut(Qt.CTRL | Qt.Key_J)

        self.setCentralWidget(label)

#-------------------------------------------------------------------

    # Functions and Slots.

    def new_button_click(self):
        print(f'New File')

    def save_button_click(self):
        print(f'Saving File...')

    def about_button_click(self):
        print(f'About this...')

#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()

    wdw = MainWindow()
    wdw.show()

    sys.exit(app.exec())

#-------------------------------------------------------------------
