import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

#-------------------------------------------------------------------

class Tabs(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # Creating the window.
        self.geometry('600x400+500+100')
        self.title('Components')
        self.iconbitmap('computer.ico')

        # Creating components and Showing the window. 
        self._create_tabs()
        self.mainloop()

    #-------------------------------------------------------------------

    # Functions or commands.

    def _components_tab1(self, tab):
        label1 = ttk.Label(tab, text = 'Name: ')
        label1.grid(row = 0, column = 0, sticky = tk.E)
        entry1 = ttk.Entry(tab, width = 30)
        entry1.grid(row = 0, column = 1, padx = 5, pady = 5)

        # Adding a button.

        def send():
            messagebox.showinfo('Message: ', f'Name: {entry1.get()}')

        button1 = ttk.Button(tab, text = 'Send', command = send)
        button1.grid(row = 1, column = 0, columnspan = 2)


    def _components_tab2(self, tab):
        content = 'Text of the tabulator.'
        scroll = scrolledtext.ScrolledText(tab, width = 50, height = 10, wrap = tk.WORD)
        scroll.insert(tk.INSERT, content)
        scroll.grid(row = 0, column = 0)    # Showing the component.

    def _components_tab3(self, tab):
        data = [x for x in range(10)]     # Using a list comprehensions.
        combobox = ttk.Combobox(tab, width = 15, values = data)
        combobox.grid(row = 0, column = 0, padx = 10, pady = 10)
        combobox.current(5)

        def show_value():
            messagebox.showinfo('Selected Value: ', f'{combobox.get()}')

        button1 = ttk.Button(tab, text = 'Show Value', command = show_value)
        button1.grid(row = 0, column = 1)

    def _components_tab4(self, tab):
        img = tk.PhotoImage(file = '58_TKinter_tabs/python-logo.png')

        def show_info():
            messagebox.showinfo('Img info: ', f'{img.cget("file")}')

        button_img = ttk.Button(tab, image = img, command = show_info)
        button_img.grid(row = 0, column = 0)

    def _components_tab5(self, tab):
        progress_bar = ttk.Progressbar(tab, orient = 'horizontal', length = 550)
        progress_bar.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 4)

        # Creating buttons for controlling the progress bar.

        def bar_execution():
            progress_bar['maximum'] = 100
            for value in range(101):
                sleep(0.03)
                progress_bar['value'] = value
                progress_bar.update()
            
            progress_bar['value'] = 0

        def loop_execution():
            progress_bar.start()

        def stop_execution():
            progress_bar.stop()

        def stop_timer():
            timer = 2000
            self.after(timer, progress_bar.stop())

        start_button = ttk.Button(tab, text = 'Execute', command = bar_execution)
        start_button.grid(row = 1, column = 0)

        loop_button = ttk.Button(tab, text = 'Execute loop', command = loop_execution)
        loop_button.grid(row = 1, column = 1)

        stop_button = ttk.Button(tab, text = 'Stop', command = stop_execution)
        stop_button.grid(row = 1, column = 2)

        timer_button = ttk.Button(tab, text = 'Timer stop', command = stop_timer)
        timer_button.grid(row = 1, column = 3)

    #-------------------------------------------------------------------

    # Using Notebook class for creating a tab control.

    def _create_tabs(self):
        tab_control = ttk.Notebook(self)

        # Adding the first tab.
        tab1 = ttk.Frame(tab_control)   # Adding a frame to the tab control.
        tab_control.add(tab1, text = 'Tab 1')   # Adding a tab to the tab control.
        tab_control.pack(fill = 'both')     # Showing the tab control.
        self._components_tab1(tab1)

        # Adding the second tabulator.
        tab2 = ttk.LabelFrame(tab_control, text = 'Content: ')   # Adding a frame to the tab control.
        tab_control.add(tab2, text = 'Tab 2')   # Adding a tab to the tab control.
        self._components_tab2(tab2)

        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab3, text = 'Tab 3')
        self._components_tab3(tab3)

        tab4 = ttk.Frame(tab_control)
        tab_control.add(tab4, text = 'Tab 4')
        self._components_tab4(tab4)
        
        tab5 = ttk.LabelFrame(tab_control, text = 'Progress Bar')
        tab_control.add(tab5, text = 'Tab 5')
        self._components_tab5(tab5)
    
#-------------------------------------------------------------------

# Creating an object of type Tabs.
if __name__ == '__main__':
    Tabs()

#-------------------------------------------------------------------
