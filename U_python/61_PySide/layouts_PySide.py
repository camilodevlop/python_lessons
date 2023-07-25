import sys
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QStackedLayout, QTabWidget, QVBoxLayout, QWidget, QHBoxLayout

#-------------------------------------------------------------------

class Color(QWidget):
    def __init__(self, new_color):
        super().__init__()
        self.setAutoFillBackground(True)
        color_palette = self.palette()

        # Creating the new component of background color.
        color_palette.setColor(QPalette.Window, QColor(new_color))
        self.setPalette(color_palette)


class MainWindow(QMainWindow): 
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('Layouts and Tabs in PySide')

        '''
        # Nesting the layouts.
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(10, 10, 10, 10)
        h_layout.setSpacing(30)

        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(5, 10, 5, 10)
        v_layout.setSpacing(20)

        # Some widgets are added to the vertical layout.
        v_layout.addWidget(Color('darkred'))
        v_layout.addWidget(Color('darkblue'))
        v_layout.addWidget(Color('darkgreen'))
        
        # The vertical layout is added to the horizontal layout.
        h_layout.addLayout(v_layout)
        h_layout.addWidget(Color('gray'))
        h_layout.addWidget(Color('purple'))
        '''

        '''
        # GridLayout.
        layout = QGridLayout()
        layout.addWidget(Color('darkred'), 0, 0)
        layout.addWidget(Color('darkblue'), 0, 2)
        layout.addWidget(Color('darkgreen'), 1, 1)
        layout.addWidget(Color('gray'), 1, 0)
        layout.addWidget(Color('purple'), 1, 2)
        '''
        
        '''
        # QStackedLayout.
        layout = QStackedLayout()
        layout.addWidget(Color('darkred'))
        layout.addWidget(Color('darkgreen'))
        layout.addWidget(Color('darkblue'))
        layout.setCurrentIndex(2)
        '''
        
        '''
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()
        
        main_layout.addLayout(button_layout)
        main_layout.addLayout(self.stack_layout)
        
        # Creation of the buttons.
        red_button = QPushButton('Red')
        button_layout.addWidget(red_button)
        self.stack_layout.addWidget(Color('darkred'))
        red_button.pressed.connect(lambda: self._change_color(0))

        blue_button = QPushButton('Blue')
        button_layout.addWidget(blue_button)
        self.stack_layout.addWidget(Color('darkblue'))
        blue_button.pressed.connect(lambda: self._change_color(1))

        green_button = QPushButton('Green')
        button_layout.addWidget(green_button)
        self.stack_layout.addWidget(Color('darkgreen'))
        green_button.pressed.connect(lambda: self._change_color(2))

        # To publish a layout it is required a generic component.
        component = QWidget() 
        component.setLayout(main_layout)
        '''

        # Tab component.
        tab = QTabWidget()
        tab.setTabPosition(QTabWidget.North)
        tab.setMovable(True)
        tab.setDocumentMode(True)

        # Adding the color to the labels.
        tab.addTab(Color('darkred'), 'Red')
        tab.addTab(Color('darkblue'), 'Blue')
        tab.addTab(Color('darkgreen'), 'green')

        self.setCentralWidget(tab)

#-------------------------------------------------------------------
    
    '''
    # Functions and Slots.
    def _change_color(self, index):
        self.stack_layout.setCurrentIndex(index)
    '''

#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()

    wdw = MainWindow()
    wdw.show()

    sys.exit(app.exec())

#-------------------------------------------------------------------
