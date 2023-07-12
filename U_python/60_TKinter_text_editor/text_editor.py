import tkinter as tk
from tkinter import LEFT, messagebox, Menu
from tkinter.filedialog import askopenfile, asksaveasfilename

class TextEditor(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title('Text Editor')
        self.iconbitmap('computer.ico')

        # Configuration of the minimum window size.
        self.rowconfigure(0, minsize = 600, weight = 1)
        self.columnconfigure(1, minsize = 600, weight = 1)

        # Text file attribute.
        self.text_space = tk.Text(self, wrap = tk.WORD)

        # Attributes for file management.
        self.file = None
        self.opened_file = False

        # self.geometry('600x400+200+0')

        # Creating components and Showing the window. 
        self._components_creation()
        self._menu_creation()
        self.mainloop()

#-------------------------------------------------------------------

    # Functions and commands.

    def _open_file(self):
        self.opened_file = askopenfile('r+')
        self.text_space.delete(1.0, tk.END)

        if not self.opened_file:
            return

        with open(self.opened_file.name, 'r+') as self.file:
            text = self.file.read()
            self.text_space.insert(1.0, text)
            self.title(f'*Text Editor - {self.file.name}')

    def _save_file(self):
        if self.opened_file:
            with open(self.opened_file.name, 'w') as self.file:
                text = self.text_space.get(1.0, tk.END)
                self.file.write(text)
                self.title(f'Text Editor - {self.file.name}')
        else:
            self._save_as_file()


    def _save_as_file(self):
        self.file = asksaveasfilename(defaultextension = '', filetypes = [('Text Files', ''), ('All Files', '*.*')])
        
        if not self.file:
            return

        with open(self.file, 'w') as self.file:
            text = self.text_space.get(1.0, tk.END)
            self.file.write(text)
            self.title(f'Text Editor - {self.file.name}')
            self.opened_file = self.file

#-------------------------------------------------------------------

    def _components_creation(self):

        # Left array of buttons.
        buttons_frame = tk.Frame(self, relief = tk.RAISED, bd = 2)
        buttons_frame.grid(row = 0, column = 0, sticky = 'NS')

        open_button = tk.Button(buttons_frame, text = 'Open', command = self._open_file)
        open_button.grid(row = 0, column = 0, sticky = 'WE', padx = 5, pady = 5)

        save_button = tk.Button(buttons_frame, text = 'Save', command = self._save_file)
        save_button.grid(row = 1, column = 0, sticky = 'WE', padx = 5, pady = 5)

        save_as_button = tk.Button(buttons_frame, text = 'Save as...', command = self._save_as_file)
        save_as_button.grid(row = 2, column = 0, sticky = 'WE', padx = 5, pady = 5)

        # Adding the text space.
        self.text_space.grid(row = 0, column = 1, sticky = 'NSWE')

    def _menu_creation(self):

        # File Menu.
        # tearoff: it avoids the separation of both the menu and the window.
        main_menu = tk.Menu(self) 
        self.config(menu = main_menu)

        file_menu = tk.Menu(main_menu, tearoff = False)
        main_menu.add_cascade(label = 'File', menu = file_menu)

        file_menu.add_command(label = 'Open', command = self._open_file)
        file_menu.add_command(label = 'Save', command = self._save_file)
        file_menu.add_command(label = 'Save as...', command = self._save_as_file)

        file_menu.add_separator()
        file_menu.add_command(label = 'Exit', command = self.quit)

        # Adding the 'file_menu' to the main_menu.
        #main_menu.add_cascade(menu = file_menu, label = 'File')


#-------------------------------------------------------------------

if __name__ == "__main__":
    TextEditor()

#-------------------------------------------------------------------
