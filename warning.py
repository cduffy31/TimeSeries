import tkinter as tk
from prepPage import prepPage
#from tkinter import ttk

'''

this is for use when results are to be added
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
'''


class warning(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        warnings = """
        This is a warning to any users that any 
        predictions, models or advice produce 
        is taken at the users own risk.
        This is one tool a technical trader might 
        use, not a crystal ball for user to access.
        As a result this software  is given 'As Is'.
        The models are created from ECB data so its 
        important that as a user you trust them. 
        """
        # manual for running the program
        manual = '''
        1. pick dates to train the LSTM on 
        2. pick currency to compare
        3. pick frequency, daily is recommended
        4. click train
        5. click show to be shown a graph
        6. click download to download a csv file. 
        '''

        # window creation
        # text creation
        man = tk.Text(self, height=10, width=60)
        man.insert(tk.END, manual, 'color')
        warn = tk.Text(self, height=10, width=60)
        warn.insert(tk.END, warnings, 'color')
        warned = tk.Label(self, text="Warning")
        warned.pack(fill=tk.X)
        warn.pack(fill=tk.X)
        man.pack(fill=tk.X)
        accept = tk.Button(self, text="Accept", height=5, width=10,
                           command=lambda: controller.show_frame(prepPage))
        accept.pack()
