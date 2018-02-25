from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from datetime import timedelta


class Timer:
    def __init__(self, master):
        # dimensions
        self.initial_size = 300
        self.ring_margin = 20
        self.ring_width = 20
        self.dimensions = {"timer_ring_margin": 70}

        self.master = master
        self.master.title("Workout App")
        self.master.geometry("{0}x{0}".format(self.initial_size))
        self.master.minsize(300, 300)
        self.master.configure(background="black")

        self.canvas = Canvas(self.master)
        self.canvas.pack()
        self.canvas.config(width=self.initial_size, height=self.initial_size, background="black", highlightthickness=0)

        self.arc = self.canvas.create_arc(self.dimensions.get("timer_ring_margin"), self.dimensions.get("timer_ring_margin"), 290, 290)
        self.canvas.itemconfigure(self.arc, start = 90, extent=270, fill = "red4", width = 0)

        self.oval = self.canvas.create_oval(30, 30, 270, 270, fill="black")
        self.center_text = self.canvas.create_text(150, 150, text="center_text", font = ("Verdanaaaa", 30, "bold"), fill="white")
        self.text_action = self.canvas.create_text(150, 180, text="text_action", font=("Courier", 15, "bold"), fill="gray48")
        self.text_shut_time = self.canvas.create_text(150, 120, text="text_shut_time", font=("Courier", 15), fill="gray48")

    @property
    def canvas_size(self):
        return min(self.master.winfo_height(), self.master.winfo_width())

    @property
    def ring_margin(self):
        return self.get_dim(self.__ring_margin)

    @ring_margin.setter
    def ring_margin(self, x):
        self.__ring_margin = self.calc_dim(x)

    def calc_dim(self, x):
            try:
                return x/self.canvas_size
            except AttributeError:
                return x/self.initial_size

    def get_dim(self, x):
            try:
                return int(x*self.canvas_size)
            except AttributeError:
                return int(x*self.initial_size)

    def scale_timer(self):
        print("test_variable:", self.ring_margin)
        self.canvas.config(width=self.canvas_size, height=self.canvas_size)
        self.canvas.itemconfigure(self.center_text, font=("Helveticaaa", int(self.canvas_size * 0.1), "bold"))
        self.canvas.itemconfigure(self.text_action, font=("Courier", int(self.canvas_size*0.05), "bold"))
        self.canvas.itemconfigure(self.text_shut_time, font=("Courier", int(self.canvas_size*0.05)))

        self.canvas.coords(self.arc, self.ring_margin, self.ring_margin, self.canvas_size-self.ring_margin, self.canvas_size-self.ring_margin)

        self.canvas.coords(self.oval, self.canvas_size*0.1, self.canvas_size*.1, self.canvas_size-(self.canvas_size*0.1), self.canvas_size-(self.canvas_size*0.1))
        self.canvas.coords(self.center_text, self.canvas_size * 0.5, self.canvas_size * 0.5)
        self.canvas.coords(self.text_action, self.canvas_size * 0.5, self.canvas_size * 0.6)
        self.canvas.coords(self.text_shut_time, self.canvas_size * 0.5, self.canvas_size * 0.4)

