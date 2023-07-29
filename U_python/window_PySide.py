import sys
from random import randint
from PySide6.QtWidgets import QLabel, QLineEdit, QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget

#-------------------------------------------------------------------

class NewWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('New Window')
        
        layout = QVBoxLayout()
        self.label = QLabel(f'New Window: {randint(0, 100)}')
        layout.addWidget(self.label)
        self.setLayout(layout)

#-------------------------------------------------------------------

class MainWindow(QMainWindow): 
    def __init__(self):
        QMainWindow.__init__(self)
        # self.new_window = None
        self.new_window = NewWindow()

        self.setWindowTitle('Windows in PySide')

        self.button = QPushButton('Show/Hide New Button')
        self.button.clicked.connect(self.show_new_window)

        self.text_entry = QLineEdit() 
        self.text_entry.textChanged.connect(self.new_window.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.text_entry)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

#-------------------------------------------------------------------

    # Functions and Slots.

    def show_new_window(self, state):
        if self.new_window.isVisible():
            self.new_window.hide()
        else:
            self.new_window.show()
        
        '''
        # Using self.new_window == None.
        if self.new_window == None:
            self.new_window = NewWindow()
            self.new_window.show()
        else:
            self.new_window.close()
            self.new_window = None
        '''

#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()

    wdw = MainWindow()
    wdw.show()

    sys.exit(app.exec())

#-------------------------------------------------------------------
