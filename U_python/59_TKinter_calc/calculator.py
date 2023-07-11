import tkinter as tk
from tkinter import END, messagebox

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('343x180+200+0')
        self.resizable(width = False, height = False)
        self.title('Calculator')
        self.iconbitmap('calculator.ico')
        self._buffer = '' 

        '''
        # Grid configuration.
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.columnconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 1)
        self.columnconfigure(4, weight = 1)
        self.rowconfigure(5, weight = 1)
        self.columnconfigure(5, weight = 1)
        '''

        # Creating components and Showing the window. 
        self._components_creation()
        self.mainloop()

    #-------------------------------------------------------------------

    # Functions and commands.
    
    def _is_entry_empty(self):
        if self.entry_user.get() == '0':
            return True

        return False

    #-------------------------------------------------------------------

    def _updating_entry(self, button_char):
        if not(self._is_entry_empty()):
            self._buffer += button_char
        else:
            self._buffer = button_char

        self.entry_user.delete(0, END)
        self.entry_user.insert(0, self._buffer)

    #-------------------------------------------------------------------

    # Commands of buttons.
    def _clear_button(self):
        self.entry_user.delete(0, END)
        self.entry_user.insert(0, '0')
        self._buffer = ''

    def _eq_button(self):
        try:
            self._buffer = str(eval(self.entry_user.get()))
        except Exception as e:
            messagebox.showerror('Error: ', f'{e}')
            self._buffer = '0'
        finally:
            self.entry_user.delete(0, END)
            self.entry_user.insert(0, self._buffer)


    #-------------------------------------------------------------------

    # Component creation.

    def _components_creation(self):
        
        # Calculator inputs.
        #enter_frame = tk.Frame(self, width = 400, height = 50, bg = 'gray')
        #enter_frame.pack()
        self.entry_user = tk.Entry(self, font = ('arial', 18, 'bold'), width = 30, justify = tk.RIGHT)
        self.entry_user.grid(row = 0, column = 0, columnspan = 4, sticky = 'NSWE')
        self.entry_user.insert(0, '0')
        

        # Calculator buttons.

        # Row 1.
        clear_button = tk.Button(self, text = 'C', bg = '#eee', command = self._clear_button)
        clear_button.grid(row = 1, column = 0, columnspan = 3, sticky = 'NSWE', padx = 0, pady = 0)
        #div_button = tk.Button(self, text = '/', command = self._div_button)
        div_button = tk.Button(self, text = '/', command = lambda: self._updating_entry('/'))
        div_button.grid(row = 1, column = 3, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)

        # Row 2.
        seven_button = tk.Button(self, text = '7', command = lambda: self._updating_entry('7'))
        seven_button.grid(row = 2, column = 0, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)
        eight_button = tk.Button(self, text = '8', command = lambda: self._updating_entry('8'))
        eight_button.grid(row = 2, column = 1, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)
        nine_button = tk.Button(self, text = '9', command = lambda: self._updating_entry('9'))
        nine_button.grid(row = 2, column = 2, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)
        mul_button = tk.Button(self, text = '*', command = lambda: self._updating_entry('*'))
        mul_button.grid(row = 2, column = 3, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)

        # Row 3.
        four_button = tk.Button(self, text = '4', command = lambda: self._updating_entry('4'))
        four_button.grid(row = 3, column = 0, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)
        five_button = tk.Button(self, text = '5', command = lambda: self._updating_entry('5'))
        five_button.grid(row = 3, column = 1, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)
        six_button = tk.Button(self, text = '6', command = lambda: self._updating_entry('6'))
        six_button.grid(row = 3, column = 2, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)
        subs_button = tk.Button(self, text = '-', command = lambda: self._updating_entry('-'))
        subs_button.grid(row = 3, column = 3, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)

        # Row 4.
        one_button = tk.Button(self, text = '1', command = lambda: self._updating_entry('1'))
        one_button.grid(row = 4, column = 0, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)
        two_button = tk.Button(self, text = '2', command = lambda: self._updating_entry('2'))
        two_button.grid(row = 4, column = 1, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)
        three_button = tk.Button(self, text = '3', command = lambda: self._updating_entry('3'))
        three_button.grid(row = 4, column = 2, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)
        plus_button = tk.Button(self, text = '+', command = lambda: self._updating_entry('+'))
        plus_button.grid(row = 4, column = 3, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)

        # Row 5.
        zero_button = tk.Button(self, text = '0', command = lambda: self._updating_entry('0'))
        zero_button.grid(row = 5, column = 0, columnspan = 2, sticky = 'NSWE', padx = 0, pady = 0)
        point_button = tk.Button(self, text = '.', command = lambda: self._updating_entry('.'))
        point_button.grid(row = 5, column = 2, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)
        eq_button = tk.Button(self, text = '=', cursor = 'hand2', command = self._eq_button)
        eq_button.grid(row = 5, column = 3, columnspan = 1, sticky = 'NSWE', padx = 0, pady = 0)

#-------------------------------------------------------------------

if __name__ == '__main__':
    Calculator()

#-------------------------------------------------------------------
