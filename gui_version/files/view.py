from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from datetime import timedelta


class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Workout App")
        self.master_initial_size = 500
        self.master.geometry('{0}x{0}'.format(self.master_initial_size))
        self.master.minsize(400, 400)
        self.master.configure(background='black')
        self.canvas = Canvas(self.master)
        self.canvas.pack()
        self.canvas.config(width=300, height=300, background="black", highlightthickness=0)
        self.arc = self.canvas.create_arc(10, 10, 290, 290)
        self.canvas.itemconfigure(self.arc, start = 90, extent = 270, fill = 'red4', width = 0)
        self.oval = self.canvas.create_oval(30, 30, 270, 270, fill='black')
        self.text = self.canvas.create_text(150, 150, text = '', font = ('Courier', 30, 'bold'), fill="white")
        self.text_action_dict = {1: "until lock", 2: "until shutdown"}
        self.text_action = self.canvas.create_text(150, 180, text='', font=('Courier', 15, 'bold'), fill="gray48")
        self.text_shut_time = self.canvas.create_text(150, 120, text='123213', font=('Courier', 15), fill="gray48")

    def scale_timer(self):
        w_height = self.master.winfo_height()
        w_width = self.master.winfo_width()
        max_canvas_size = min(w_height, w_width)
        self.canvas.config(width=max_canvas_size, height=max_canvas_size)
        self.canvas.itemconfigure(self.text, font=('Courier', int(max_canvas_size*0.1), 'bold'))
        self.canvas.itemconfigure(self.text_action, font=('Courier', int(max_canvas_size*0.05), 'bold'))
        self.canvas.itemconfigure(self.text_shut_time, font=('Courier', int(max_canvas_size*0.05)))
        self.canvas.coords(self.arc, 10, 10, max_canvas_size-10, max_canvas_size-10)
        self.canvas.coords(self.oval, max_canvas_size*0.1, max_canvas_size*.1, max_canvas_size-(max_canvas_size*0.1), max_canvas_size-(max_canvas_size*0.1))
        self.canvas.coords(self.text, max_canvas_size*0.5, max_canvas_size*0.5)
        self.canvas.coords(self.text_action, max_canvas_size * 0.5, max_canvas_size * 0.6)
        self.canvas.coords(self.text_shut_time, max_canvas_size * 0.5, max_canvas_size * 0.4)
