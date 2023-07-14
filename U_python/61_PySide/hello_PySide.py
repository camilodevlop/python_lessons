import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Base class of Qt (PySide).

# It processes the events of the application (event loop).
app = QApplication()

# Window objects.
#window = QWidget()
#window = QPushButton('PySide Button')

window = QMainWindow()
window.setWindowTitle('Hello PySide')
window.resize(600, 400)

#-------------------------------------------------------------------

window.show()

#-------------------------------------------------------------------

sys.exit(app.exec())

#-------------------------------------------------------------------
