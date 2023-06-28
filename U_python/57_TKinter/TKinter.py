# Graphical User Interface
# TKinter - TK Interface.

import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu   # Include the components.

# basic configuration.
window = tk.Tk()
window.geometry('600x400')
window.title('Component Handling')
window.iconbitmap('computer.icon')

#-------------------------------------------------------------------
'''
# Grid configuration.
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 5)
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 5)
'''
#-------------------------------------------------------------------
# Events
def event1():
    '''
    # Information associated with the box.
    #label1.config(text = entry1_var.get())
    #entry1_var.set('Type a string:')
    label1.config(text = entry1.get())
    '''

    # Using messagebox.
    message1 = entry1.get()
    if message1:
        messagebox.showinfo('Information: ', message1 + ' (Information)')
        #messagebox.showerror('Information: ', message1 + ' (Error)')
        #messagebox.showwarning('Information: ', message1 + ' (Warning)')

    '''
    print(entry1.get())
    button1.config(text = entry1.get())
    #entry1.delete(0, tk.END)    # Deleting the content of the box.
    entry1.select_range(0, tk.END)  # Selecting the content of the box.
    entry1.focus()
    '''

def exit():
    window.quit()
    window.destroy()
    sys.exit()

def create_menu():
    main_menu = Menu(window) # tearoff: it avoids the separation of both the menu and the window.

    file_menu = Menu(main_menu, tearoff = False)
    # Adding the 'New' option to the file_menu.
    file_menu.add_command(label = 'New')
    # Adding a separator.
    file_menu.add_separator()
    # Adding the 'Exit' option to the file_menu.
    file_menu.add_command(label = 'Exit', command = exit)

    help_menu = Menu(main_menu, tearoff = False)
    # Adding the 'About' option to the help_menu.
    help_menu.add_command(label = 'About')

    # Adding the 'file_menu' and 'help_menu' to the main_menu.
    main_menu.add_cascade(menu = file_menu, label = 'File')
    main_menu.add_cascade(menu = help_menu, label = 'Help')
    window.config(menu = main_menu)


'''
def event2():
    button2.config(text='Button 2 pressed')

def event4():
    button4.config(text='Button 4 pressed', fg='blue')
'''
#-------------------------------------------------------------------
# Buttons. # sticky 'N' (up), 'S' (down),  'W' (left), 'E' (right), 

button1 = ttk.Button(window, text = 'Send', command = event1)
button1.grid(row = 0, column = 1, sticky = 'NSWE', padx = 5, pady = 5, ipadx = 5, ipady = 5)

'''
button2 = ttk.Button(window, text = 'Button 2', command = event2)
button2.grid(row = 1, column = 0, sticky = 'NSWE')

button3 = ttk.Button(window, text = 'Button 3')
button3.grid(row = 0, column = 1, sticky = 'NSWE')

button4 = tk.Button(window, text = 'Button 4', command = event4)
button4.grid(row = 1, column = 1, sticky = 'NSWE')
'''
#-------------------------------------------------------------------

# Labels.
label1 = tk.Label(window, text = 'Content of the box.')
label1.grid(row = 1, column = 0, columnspan = 2, sticky = 'W')

#-------------------------------------------------------------------

# show is mainly used for hide passwords.
#entry1 = ttk.Entry(window, width = 30, justify = tk.CENTER, show = '*', state = tk.DISABLED)
#entry1_var = tk.StringVar(value = 'Type a string:')
#entry1 = ttk.Entry(window, width = 30, justify = tk.CENTER, textvariable = entry1_var)
entry1 = ttk.Entry(window, width = 30, justify = tk.CENTER)
entry1.grid(row = 0, column = 0)
entry1.insert(0, 'Type a string:')
#entry1.config(state = 'readonly')

#-------------------------------------------------------------------

# This method shows the window.
create_menu()
window.mainloop()

#-------------------------------------------------------------------
