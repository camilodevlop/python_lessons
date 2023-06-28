
# TKinter - TK Interface
import tkinter as tk
from tkinter import ttk, messagebox

#-------------------------------------------------------------------

# Creating the window.
window = tk.Tk()
window.geometry('300x130')
window.title('Login')
window.iconbitmap('computer.icon')
window.resizable(width = False, height = False)

#-------------------------------------------------------------------

# Grid configuration.
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 3)

#-------------------------------------------------------------------

# Functions.
def button_login_action():
    msg1 = entry_user.get()
    msg2 = entry_psw.get()
    
    if msg1 and msg2:
        messagebox.showinfo('Login Information', f'User: {msg1}\nPassword: {msg2}')

#-------------------------------------------------------------------

# Labels.
label_user = tk.Label(window, text = 'User:')
label_user.grid(row = 0, column = 0, columnspan = 1, sticky = tk.E, padx = 5, pady = 5)

label_psw = tk.Label(window, text = 'Password:')
label_psw.grid(row = 1, column = 0, columnspan = 1, sticky = tk.E, padx = 5, pady = 5)

#-------------------------------------------------------------------

# Entries.
entry_user = ttk.Entry(window, width = 20, justify = tk.LEFT)
entry_user.grid(row = 0, column = 1, padx = 10, pady = 5)

entry_psw = ttk.Entry(window, width = 20, justify = tk.LEFT, show = '*')
entry_psw.grid(row = 1, column = 1, padx = 10)

#-------------------------------------------------------------------

# Buttons.
button_login = ttk.Button(window, text = 'Login', command = button_login_action)
button_login.grid(row = 2, column = 0, columnspan = 4, sticky = 'NSWE', padx = 90, pady = 10)

#-------------------------------------------------------------------



#-------------------------------------------------------------------

# This method shows the window.
window.mainloop()

#-------------------------------------------------------------------
