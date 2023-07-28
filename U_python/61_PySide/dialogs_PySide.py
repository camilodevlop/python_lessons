import sys
from PySide6.QtWidgets import QLabel, QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QWidget, QMessageBox

#-------------------------------------------------------------------
'''
class DialogWindow(QDialog):
    def __init__(self, father = None, title = 'Dialog Window'):
        super().__init__(father)
        self.setWindowTitle(title)

        # Addition of Accept and Cancel buttons.
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.dialog_buttons = QDialogButtonBox(buttons)
        self.dialog_buttons.accepted.connect(self.accept)
        self.dialog_buttons.rejected.connect(self.reject)

        # Creating a layout to publish the buttons.
        self.layout = QVBoxLayout()
        message = QLabel('Choose one of the following options:')
        self.layout.addWidget(message)
        self.layout.addWidget(self.dialog_buttons)
        self.setLayout(self.layout)
'''


#-------------------------------------------------------------------

class MainWindow(QMainWindow): 
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('Dialogs in PySide')

        button = QPushButton('Show Dialog')
        button.clicked.connect(self.click_button)

        self.setCentralWidget(button)

    #-------------------------------------------------------------------

    # Functions and Slots.

    def click_button(self, s):
        print(f'Button Clicked: {s}')
        # dialog = DialogWindow(self, 'Help')       # Using DialogWindow().

        '''
        # Simple Dialog.
        dialog = QMessageBox(self)
        dialog.setWindowTitle('Simple Dialog')
        dialog.setText('Simple Dialog')
        '''

        '''
        # Dialog window with question.
        dialog = QMessageBox(self)
        dialog.setWindowTitle('Dialog window with question.')
        dialog.setText('Dialog window with question.')
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No) 
        dialog.setIcon(QMessageBox.Question)

        returned_value = dialog.exec()

        print(f'Returned value: {returned_value}')
        if returned_value == QMessageBox.Yes:
            print('Ok (Yes) pressed')
        else:
            print('Cancel (No) pressed')

        '''

        '''
        # Simplify the Dialog window with question.
        dialog = QMessageBox.question(self, 'Window with question', 'Dialog window with question', )
        '''

        # Custom dialog window.
        dialog = QMessageBox.critical(self, 'Critical problem', 'Critical problem window', 
                                      buttons = QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
                                      defaultButton = QMessageBox.Discard)

        if dialog == QMessageBox.Discard:
            print('Discard pressed')
        elif dialog == QMessageBox.NoToAll:
            print('NoToAll pressed')
        else:
            print('Ignore pressed')

#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()

    wdw = MainWindow()
    wdw.show()

    sys.exit(app.exec())

#-------------------------------------------------------------------
