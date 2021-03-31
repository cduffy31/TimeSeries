import matplotlib
import tkinter as tk

matplotlib.use("TkAgg")
from figurePage import figurePage
from livePrice import livePrice
from prepPage import prepPage
from warning import warning


class pageCont(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Forex Data Prediction")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        self.frames = {}
        for f in (warning, prepPage, figurePage, livePrice):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(warning)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = pageCont()
app.mainloop()
