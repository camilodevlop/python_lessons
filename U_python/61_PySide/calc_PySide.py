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
        main_layout = QVBoxLayout()
        buttons_layout = QGridLayout()

        # Text of the mathematical operations.
        self.text_line = QLineEdit()
        self.text_line.setAlignment(Qt.AlignRight)
        self.text_line.setPlaceholderText('0')
        main_layout.addWidget(self.text_line)
        
        # Buttons of the calculator.
        button_0 = QPushButton('0')
        button_0.pressed.connect(lambda: self.update_operations('0'))
        button_1 = QPushButton('1')
        button_1.pressed.connect(lambda: self.update_operations('1'))
        button_2 = QPushButton('2')
        button_2.pressed.connect(lambda: self.update_operations('2'))
        button_3 = QPushButton('3')
        button_3.pressed.connect(lambda: self.update_operations('3'))
        button_4 = QPushButton('4')
        button_4.pressed.connect(lambda: self.update_operations('4'))
        button_5 = QPushButton('5')
        button_5.pressed.connect(lambda: self.update_operations('5'))
        button_6 = QPushButton('6')
        button_6.pressed.connect(lambda: self.update_operations('6'))
        button_7 = QPushButton('7')
        button_7.pressed.connect(lambda: self.update_operations('7'))
        button_8 = QPushButton('8')
        button_8.pressed.connect(lambda: self.update_operations('8'))
        button_9 = QPushButton('9')
        button_9.pressed.connect(lambda: self.update_operations('9'))
        button_sum = QPushButton('+')
        button_sum.pressed.connect(lambda: self.update_operations('+'))
        button_sub = QPushButton('-')
        button_sub.pressed.connect(lambda: self.update_operations('-'))
        button_mul = QPushButton('x')
        button_mul.pressed.connect(lambda: self.update_operations('*'))
        button_div = QPushButton('/')
        button_div.pressed.connect(lambda: self.update_operations('/'))
        button_point = QPushButton('.')
        button_point.pressed.connect(lambda: self.update_operations('.'))
        button_clc = QPushButton('C')
        button_clc.pressed.connect(lambda: self.update_operations('C'))
        button_eq = QPushButton('=')
        button_eq.setShortcut(Qt.Key_Return)
        button_eq.pressed.connect(self.eq_button)

        main_layout.addLayout(buttons_layout)

        buttons_layout.addWidget(button_7, 0, 0)
        buttons_layout.addWidget(button_8, 0, 1)
        buttons_layout.addWidget(button_9, 0, 2)
        buttons_layout.addWidget(button_div, 0, 3)

        buttons_layout.addWidget(button_4, 1, 0)
        buttons_layout.addWidget(button_5, 1, 1)
        buttons_layout.addWidget(button_6, 1, 2)
        buttons_layout.addWidget(button_mul, 1, 3)

        buttons_layout.addWidget(button_1, 2, 0)
        buttons_layout.addWidget(button_2, 2, 1)
        buttons_layout.addWidget(button_3, 2, 2)
        buttons_layout.addWidget(button_sub, 2, 3)

        buttons_layout.addWidget(button_0, 3, 0)
        buttons_layout.addWidget(button_point, 3, 1)
        buttons_layout.addWidget(button_clc, 3, 2)
        buttons_layout.addWidget(button_sum, 3, 3)
        buttons_layout.addWidget(button_eq, 3, 4)
        
        # Publishing layouts.
        component = QWidget()
        component.setLayout(main_layout)

        self.setCentralWidget(component)

#-------------------------------------------------------------------

    def update_operations(self, inpt):
        if inpt != 'C':
            self.operations += inpt
            print(f'{self.operations}')
            self.text_line.setText(self.operations)
        else:
            self.operations = ''
            self.text_line.setText(self.operations)
            self.text_line.setPlaceholderText('0')

    def eq_button(self):
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
