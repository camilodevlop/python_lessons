import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt

#-------------------------------------------------------------------

class MainWindow(QMainWindow): 
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('Events in PySide')
        self.label = QLabel('Click on this window.')

        self.setCentralWidget(self.label)

    # def mouseMoveEvent(self, event):
    #    self.label.setText('Mouse Move Event detected.')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText('Mouse Press Event left Button.')
        elif event.button() == Qt.MiddleButton:
            self.label.setText('Mouse Press Event MiddleButton Button.')
        elif event.button() == Qt.RightButton:
            self.label.setText('Mouse Press Event Right Button.')

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText('Mouse Release Event left Button.')
        elif event.button() == Qt.MiddleButton:
            self.label.setText('Mouse Release Event MiddleButton Button.')
        elif event.button() == Qt.RightButton:
            self.label.setText('Mouse Release Event Right Button.')

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText('Mouse Double Click Event left Button.')
        elif event.button() == Qt.MiddleButton:
            self.label.setText('Mouse Double Click MiddleButton Button.')
        elif event.button() == Qt.RightButton:
            self.label.setText('Mouse Double Click Right Button.')

#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()

    wdw = MainWindow()
    wdw.show()

    sys.exit(app.exec())

#-------------------------------------------------------------------
