import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
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
        new_button = QAction(QIcon('Nuevo.png'), 'New', self)
        tool_bar.addAction(new_button)
        new_button.setStatusTip('New File')
        new_button.triggered.connect(self.new_button_click)
        # new_button.setCheckable(True)

        # Action of Save File.
        save_button = QAction('Save', self )
        tool_bar.addAction(save_button)
        save_button.setStatusTip('Saving File')
        save_button.triggered.connect(self.save_button_click)

        tool_bar.addSeparator()

        tool_bar.addWidget(QCheckBox())
        tool_bar.addWidget(QLabel('Exit'))

        self.setCentralWidget(label)

#-------------------------------------------------------------------

    # Functions and Slots.

    def new_button_click(self):
        print(f'New File')

    def save_button_click(self):
        print(f'Saving File...')

#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()

    wdw = MainWindow()
    wdw.show()

    sys.exit(app.exec())

#-------------------------------------------------------------------
