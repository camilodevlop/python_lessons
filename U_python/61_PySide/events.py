 # Signals (are the envents) and Slots (Process the events).

from PySide6.QtWidgets import QWidget, QApplication,QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout
import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('Signals and Slots')
        self.setFixedSize(400, 200)

        self.label = QLabel()
        self.text_entry = QLineEdit()

        self.text_entry.textChanged.connect(self.label.setText)

        # Componentes publication using a layout.
        layout = QVBoxLayout()
        layout.addWidget(self.text_entry)
        layout.addWidget(self.label)
        
        # Container creation.
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        
        '''
        self.windowTitleChanged.connect(self.window_title_change) 

        # Associating an event (click) to the button. 
        # Then, connecting the event to a slot (click_event function).
        self.button = QPushButton('Click here')
        self.button.clicked.connect(self.event_click)
        self.setCentralWidget(self.button)

        button.setCheckable(True) # The button is highlighted if the button is pressed.
        
        button.clicked.connect(self.event_check)
        '''

    #-------------------------------------------------------------------
    # Functions.
    '''
    def event_check(self, check):
        self.button_check = check
        print('Is checked? ', self.button_check)

    def event_click(self):
        self.button.setText('New text of the Button')
        self.button.setEnabled(False)
        self.setWindowTitle('New title of the window.')
        print('Click event')

    def window_title_change(self, new_title):
        print(f'Window title has changed: {new_title}')
    '''
#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())  

#-------------------------------------------------------------------
