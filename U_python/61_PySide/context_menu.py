import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QMenu
from PySide6.QtGui import QAction

#-------------------------------------------------------------------

class MainWindow(QMainWindow): 
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('Contextual Menus in PySide')
        
        # Showing and connection of the contextual menu.
        self.show()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenuEvent)

    def contextMenuEvent(self, position):
        context_menu = QMenu(self)

        new_button = QAction('New', self)
        new_button.triggered.connect(self.new_button_click)

        save_button = QAction('Save', self)
        save_button.triggered.connect(self.save_button_click)

        exit_button = QAction('Exit', self)
        exit_button.triggered.connect(self.exit_button_click)

        context_menu.addAction(new_button)
        context_menu.addAction(save_button)
        context_menu.addAction(exit_button) 

        context_menu.exec(self.mapToGlobal(position))

    '''
    def contextMenuEvent(self, event):
        context_menu = QMenu(self)

        new_button = QAction('New', self)
        new_button.triggered.connect(self.new_button_click)

        save_button = QAction('Save', self)
        save_button.triggered.connect(self.save_button_click)

        exit_button = QAction('Exit', self)
        exit_button.triggered.connect(self.exit_button_click)

        context_menu.addAction(new_button)
        context_menu.addAction(save_button)
        context_menu.addAction(exit_button) 

        context_menu.exec(event.globalPos())
    '''
#-------------------------------------------------------------------

    # Functions and Slots.

    def new_button_click(self, s):
        print(f'New File')

    def save_button_click(self, s):
        print(f'Saving File...')

    def exit_button_click(self, s):
        print(f'Exit File')

#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()

    wdw = MainWindow()
    wdw.show()

    sys.exit(app.exec())

#-------------------------------------------------------------------
