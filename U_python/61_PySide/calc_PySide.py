from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtCore import Qt


#-------------------------------------------------------------------

class Calculator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('Calculator') 
        self.setFixedSize(235, 235)

        # Operations string.
        self.operations = ''

        # Layouts.
        self.main_layout = QVBoxLayout()
        self.buttons_layout = QGridLayout()

        # Setting the operations text line.
        self._setting_operations_text_line()

        # Setting the calculator buttons.
        self._buttons_creation()
        self._buttons_slots()

        # Publishing layouts.
        component = QWidget()
        component.setLayout(self.main_layout)

        self.setCentralWidget(component)

#-------------------------------------------------------------------

    # Functions and Slots.

    def _setting_operations_text_line(self):
        self.text_line = QLineEdit()
        self.text_line.setAlignment(Qt.AlignRight)
        self.text_line.setPlaceholderText('0')
        self.text_line.setReadOnly(True)
        self.main_layout.addWidget(self.text_line)

    def _buttons_creation(self):
        self.buttons = {}

        buttons = {'7':(0,0), '8':(0,1), '9':(0,2), '/':(0,3), '4':(1,0),
                   '5':(1,1), '6':(1,2), '*':(1,3), '1':(2,0), '2':(2,1),
                   '3':(2,2), '-':(2,3), '0':(3,0), '.':(3,1), 'C':(3,2),
                   '+':(3,3), '=':(3,4)}
        
        for text_button, position in buttons.items():
            self.buttons[text_button] = QPushButton(text_button)
            self.buttons[text_button].setFixedSize(40,40)
            self.buttons_layout.addWidget(self.buttons[text_button], position[0], position[1])

        self.main_layout.addLayout(self.buttons_layout)     # Adds the grid layout to the Main Layout.

    def _buttons_slots(self):
        for text_button, button in self.buttons.items():
            if text_button != '=':
                button.clicked.connect(partial(self._update_operations, text_button)) 

        self.buttons['='].clicked.connect(self._eq_button)
        self.buttons['='].setShortcut(Qt.Key_Return)        # The return key activates the equal button.

    def _update_operations(self, inpt):
        if inpt != 'C':
            self.operations += inpt
            self.text_line.setText(self.operations)
        else:
            self.operations = ''
            self.text_line.setText(self.operations)

    def _eq_button(self):
        try:
            self.operations = str(eval(self.operations))

        except Exception as e:
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Error')
            dialog.setText(f'An error has Occurred')
            dialog.exec()
            self.operations = ''

        finally:
            self.text_line.setText(self.operations)

#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()

    calculator = Calculator()
    calculator.show()

    sys.exit(app.exec())    

#-------------------------------------------------------------------
