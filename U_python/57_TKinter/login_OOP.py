# TKinter - TK Interface
import tkinter as tk
from tkinter import ttk, messagebox

#-------------------------------------------------------------------

class Login(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Creating the window.
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('computer.icon')
        self.resizable(width = False, height = False)

        # Grid configuration.
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 3)
        
        self._component_creation()
        self.mainloop()

    #-------------------------------------------------------------------
    def _component_creation(self):
        
        # User.
        label_user = tk.Label(self, text = 'User:')
        label_user.grid(row = 0, column = 0, columnspan = 1, sticky = tk.E, padx = 5, pady = 5)
        self.entry_user = ttk.Entry(self, width = 20, justify = tk.LEFT)
        self.entry_user.grid(row = 0, column = 1, padx = 10, pady = 5)

        # Password.
        label_psw = tk.Label(self, text = 'Password:')
        label_psw.grid(row = 1, column = 0, columnspan = 1, sticky = tk.E, padx = 5, pady = 5)
        self.entry_psw = ttk.Entry(self, width = 20, justify = tk.LEFT, show = '*')
        self.entry_psw.grid(row = 1, column = 1, padx = 10)

        # Buttons.
        button_login = ttk.Button(self, text = 'Login', command = self.button_login_action)
        button_login.grid(row = 2, column = 0, columnspan = 4, sticky = 'NSWE', padx = 90, pady = 10)

    #-------------------------------------------------------------------

    # Functions.
    def button_login_action(self):
        msg1 = self.entry_user.get()
        msg2 = self.entry_psw.get()
        
        if msg1 and msg2:
            messagebox.showinfo('Login Information', f'User: {msg1}\nPassword: {msg2}')

#-------------------------------------------------------------------

# Creating the Login object.
Login()

#-------------------------------------------------------------------
