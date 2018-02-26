from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from datetime import timedelta


class Timer:
    def __init__(self, master):
        # general properties
        self.bgcolor = "black"

        # ring properties
        self.ring_color = "red4"
        self.initial_size = 300
        self.ring_margin = 20
        self.ring_width = 20

        # text properties
        self.central_text_size = 30
        self.central_text_color = "white"
        self.central_text_font = {"font": "Helvetica", "style": "bold"}


        self.master = master
        self.master.title("Workout App")
        self.master.geometry("{0}x{0}".format(self.initial_size))
        self.master.minsize(300, 300)
        self.master.configure(background=self.bgcolor)

        self.canvas = Canvas(self.master)
        self.canvas.pack()
        self.canvas.config(width=self.initial_size, height=self.initial_size, background="black", highlightthickness=0)
        self.ring_arc = self.canvas.create_arc(*self.ring_outter_coords)
        self.canvas.itemconfigure(self.ring_arc, start = 90, extent=270, fill=self.ring_color, width=0)
        self.ring_inner_oval = self.canvas.create_oval(*self.ring_inner_coords, fill=self.bgcolor)


        self.central_text = self.canvas.create_text(*self.central_text_coords, text="central_text",
                                                    font=(self.central_text_font.get("font"),
                                                          self.central_text_size,
                                                          self.central_text_font.get("style")),
                                                    fill=self.central_text_color)

        self.text_action = self.canvas.create_text(150, 180, text="text_action", font=("Courier", 15, "bold"), fill="gray48")
        self.text_shut_time = self.canvas.create_text(150, 120, text="text_shut_time", font=("Courier", 15), fill="gray48")

    @property
    def canvas_size(self):
        if getattr(self, "master", None) is not None:
            return min(self.master.winfo_height(), self.master.winfo_width())
        else:
            return self.initial_size

    @property
    def ring_margin(self):
        return self.get_dim(self.__ring_margin)

    @ring_margin.setter
    def ring_margin(self, x):
        self.__ring_margin = self.calc_dim(x)

    @property
    def ring_outter_coords(self):
        return (self.ring_margin, self.ring_margin,
                self.canvas_size-self.ring_margin, self.canvas_size-self.ring_margin)

    @property
    def ring_width(self):
        return self.get_dim(self.__ring_width)

    @ring_width.setter
    def ring_width(self, x):
        self.__ring_width = self.calc_dim(x)

    @property
    def ring_inner_coords(self):
        return (self.ring_width + self.ring_margin, self.ring_width + self.ring_margin,
                self.canvas_size - self.ring_width - self.ring_margin,
                self.canvas_size - self.ring_width - self.ring_margin)
    
    @property
    def central_text_size(self):
        return self.get_dim(self.__central_text_size)
    
    @central_text_size.setter
    def central_text_size(self, x):
        self.__central_text_size = self.calc_dim(x)

    @property
    def central_text_coords(self):
        return int(self.canvas_size/2), int(self.canvas_size/2)

    def calc_dim(self, x):
        return x/self.canvas_size

    def get_dim(self, x):
        return int(x*self.canvas_size)

    def scale_timer(self):
        print("test_variable:", self.central_text_font, self.central_text_size)
        self.canvas.config(width=self.canvas_size, height=self.canvas_size)
        self.canvas.itemconfigure(self.central_text, font=(self.central_text_font.get("font"),
                                                           self.central_text_size,
                                                           self.central_text_font.get("style")))

        self.canvas.itemconfigure(self.text_action, font=("Courier", int(self.canvas_size*0.05), "bold"))
        self.canvas.itemconfigure(self.text_shut_time, font=("Courier", int(self.canvas_size*0.05)))

        self.canvas.coords(self.ring_arc, *self.ring_outter_coords)

        self.canvas.coords(self.ring_inner_oval, *self.ring_inner_coords)
        self.canvas.coords(self.central_text, *self.central_text_coords)
        self.canvas.coords(self.text_action, self.canvas_size * 0.5, self.canvas_size * 0.6)
        self.canvas.coords(self.text_shut_time, self.canvas_size * 0.5, self.canvas_size * 0.4)
