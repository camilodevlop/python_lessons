from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
import sys

class WindowPySide(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('OOP - PySide')

        # Size
        #self.resize(600, 400)
        self.setFixedSize(QSize(600,400))

        # Creating components.
        self._components_creation()

#-------------------------------------------------------------------

    def _components_creation(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('File')

        new_action = QAction('New', self)
        file_menu.addAction(new_action)
        
        new_action.setStatusTip('New file')
        self.statusBar().showMessage('Status Bar Information')
        
        button = QPushButton('New Button')
        self.setCentralWidget(button)

#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()
    
    wdw = WindowPySide()
    wdw.show()

    sys.exit(app.exec())

#-------------------------------------------------------------------
