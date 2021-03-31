import tkinter as tk
import pandas
import numpy as np
import matplotlib
from fetchPrice import fetchPrice
import datetime as dt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style

matplotlib.use("TkAgg")
style.use("ggplot")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)


class livePrice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        fetch = fetchPrice()
        day = dt.datetime.now().strftime('%y-%m-%d')
        str(day)
        day = "20"+day
        price = fetch.get_data("2021-03-04", day)
        self.animate(price)
        label = tk.Label(self, text="welcome to the results page")
        label.pack()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def animate(self, data):
        df = pandas.DataFrame.from_dict(data['rates'], orient='index')
        df.sort_index(inplace=True)
        # print(df.to_string())
        xList = df.index.to_list()
        usdList = df['EUR'].to_list()
        euroList = df['USD'].to_list()
        a.clear()
        a.plot(xList, usdList, label="USD")
        a.plot(xList, euroList, label="EURO")
