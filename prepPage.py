import tkinter as tk
from tkinter import ttk
from figurePage import figurePage
from livePrice import livePrice
from tkcalendar import Calendar
import datetime as dt


class prepPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="please pick your preferences")
        label.pack()
        '''
        year = dt.datetime.year()
        month = dt.datetime.month()
        day = dt.datetime.day()
        startDate = Calendar(self, selectmode='day', year=2012, month=12, day=22).pack()
        endDate = Calendar(self, selectmode='day', year=year, month=month, day=day).pack()
        '''
        calculate = tk.Button(self, text="calculate", height=5, width=10,
                              command=lambda: controller.show_frame(figurePage))
        calculate.pack()

        liveFeed = tk.Button(self, text="Live Feed", height=5, width=10,
                             command=lambda: controller.show_frame(livePrice))
        liveFeed.pack()
