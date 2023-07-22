from PySide6.QtWidgets import QDial, QSlider, QDoubleSpinBox, QLineEdit, QListWidget, QCheckBox, QComboBox, QLabel, QSpinBox, QWidget, QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setWindowTitle('Components')
        self.setFixedSize(500, 600)

        '''
        # Labels
        label = QLabel('Hello')
        label.setPixmap(QPixmap('/Users/camiloalejandro/Documents/Python/U_python/61_PySide/layla.jpg'))
        label.setScaledContents(True)

        label.setText('Greetings') # Modifying the ve initial text.
        font = label.font() # Modifying the font.
        font.setPixelSize(25)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        '''
        
        '''
        # Checkbox
        checkbox = QCheckBox('Checkbox')
        checkbox.setTristate(True)
        checkbox.stateChanged.connect(self.show_state)
        '''

        '''
        # ComboBox or drop down list.
        combobox = QComboBox()
        #combobox.addItem('One')    # Adding elements.
        combobox.addItems(['One', 'Two', 'Three'])
        # Detecting both Indice and Texts changes.
        combobox.currentIndexChanged.connect(self._index_change)
        combobox.currentTextChanged.connect(self._text_change)
        # Editable mode is activated for the ComboBox.
        combobox.setEditable(True)
        # The insert policy is specified.
        #combobox.setInsertPolicy(QComboBox.NoInsert) # The insertion of new elements is not allowed.
        # combobox.setInsertPolicy(QComboBox.InsertAtTop) # Activating the insert at the beginning of the ComboBox.
        # combobox.setInsertPolicy(QComboBox.InsertAtCurrent) # Modifying the current element.
        # combobox.setInsertPolicy(QComboBox.InsertAtBottom) # Activating the insert at the end of the ComboBox.
        # combobox.setInsertPolicy(QComboBox.InsertBeforeCurrent) # Insert an element before the current one.
        # combobox.setInsertPolicy(QComboBox.InsertAfterCurrent) # Insert an element after the current one.
        combobox.setInsertPolicy(QComboBox.InsertAlphabetically) # Insert an element alphabetically.
        combobox.setMaxCount(5) # Limits the elements that can be added to the ComboBox.
        '''

        '''
        # ListWidget.
        listw = QListWidget()
        # listw.addItem('One') # Adding elements.
        listw.addItems(['One', 'Two', 'Three'])
        # Detecting both Element and Text changes.
        listw.currentItemChanged.connect(self._item_change)
        listw.currentTextChanged.connect(self._item_text)
        '''

        '''
        # Text line.
        text_line = QLineEdit()
        text_line.setMaxLength(25) # Setting the maximum number of characters.
        text_line.setPlaceholderText('Input Your Name: ') # Setting a placeholder.
        # text_line.setReadOnly(True)
        text_line.setInputMask('000-000-00-00')
        # Detecting Enter, text selection change, and text change.
        text_line.returnPressed.connect(self._enter_pressed)
        text_line.selectionChanged.connect(self._change_selection)
        text_line.textChanged.connect(self._text_change)
        '''

        '''
        # QSpinBox.
        # number = QSpinBox()
        number = QDoubleSpinBox()
        # number.setMinimum(-5)
        # number.setMaximum(8)
        number.setRange(-5,5)
        number.setPrefix('$')
        number.setSuffix('c')
        number.setSingleStep(2)
        # Detecting a value change and sending the value in text format.
        number.valueChanged.connect(self._change_value)
        number.textChanged.connect(self._text_change)
        '''

        '''
        # QSlider.
        component = QSlider(Qt.Horizontal)
        # component.setMinimum(-5)
        # component.setMaximum(8)
        component.setRange(-5,8) 
        # Detecting a value change.
        component.valueChanged.connect(self._change_value)
        component.sliderMoved.connect(self._slider_change_position)
        component.sliderPressed.connect(self._slider_pressed)
        component.sliderReleased.connect(self._slider_released)
        '''

        # QDial.
        component = QDial()
        # component.setMinimum(-5)
        # component.setMaximum(8)
        component.setRange(-5,50) 
        # Detecting a value change.
        component.valueChanged.connect(self._change_value)
        component.sliderMoved.connect(self._slider_change_position)
        component.sliderPressed.connect(self._slider_pressed)
        component.sliderReleased.connect(self._slider_released)

        self.setCentralWidget(component)

#-------------------------------------------------------------------

    '''
    # Functions of Checkbox.
    def show_state(self, state):
        print(f'Checkbox State: {state}')

        if state == 2:
            print('Checkbox ON')
        elif state == 1:
            print('Checkbox Partially ON')
        elif state == 0:
            print('Checkbox OFF')
        else:
            print('Invalid state of the Checkbox.')
    '''

    '''
    # Functions of ComboBox.
    def _index_change(self, new_index):
        print(f'New Index: {new_index}')

    def _text_change(self, new_text):
        print(f'New Text: {new_text}')
    '''

    '''
    def _item_change(self, new_item):
        print(f'New Selected Item: {new_item.text}')
        
    def _item_text(self, new_text):
        print(f'New Item: {new_text}')
    '''

    '''
    # Functions of Line Edit.
    def _enter_pressed(self):
        print(f'Enter Pressed')
        self.centralWidget().setText('000-000-00-00')

    def _change_selection(self):
        print('Change of text selection.')
        print(self.centralWidget().selectedText())

    def _text_change(self, new_text):
        print(f'New Text: {new_text}')
    '''

    '''
    # Functions of Double Spin Box.
    def _change_value(self, value):
        print(f'Value: {value}')

    def _text_change(self, new_text):
        print(f'New Text: {new_text}')
    '''

    '''
    # Funtions of Slider.
    def _change_value(self, value):
        print(f'Value: {value}')
    
    def _slider_change_position(self, new_position):
        print(f'New Position: {new_position}')

    def _slider_pressed(self):
        print(f'Slider Pressed')

    def _slider_released(self):
        print(f'Slider Released')
    '''

    # Funtions of QDial.
    def _change_value(self, value):
        print(f'Value: {value}')
    
    def _slider_change_position(self, new_position):
        print(f'New Position: {new_position}')

    def _slider_pressed(self):
        print(f'Dial Pressed')

    def _slider_released(self):
        print(f'Dial Released')

#-------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication()
    
    wdw = MainWindow()
    wdw.show()

    sys.exit(app.exec())

#-------------------------------------------------------------------
