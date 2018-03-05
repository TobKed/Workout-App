from tkinter import *
from tkinter.ttk import *


class Timer:
    def __init__(self, master, inital_settings):
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
        self.central_text_family = "Helvetica"
        self.central_text_style = "normal"

        self.text_plus_1_size = 15
        self.text_plus_1_color = "white"
        self.text_plus_1_family = "Helvetica"
        self.text_plus_1_style = "normal"
        self.text_plus_1_position = 0.7

        self.text_plus_2_size = 15
        self.text_plus_2_color = "white"
        self.text_plus_2_family = "Helvetica"
        self.text_plus_2_style = "bold"
        self.text_plus_2_position = 0.8

        self.text_minus_1_size = 10
        self.text_minus_1_color = "white"
        self.text_minus_1_family = "Helvetica"
        self.text_minus_1_style = "normal"
        self.text_minus_1_position = 0.37

        self.text_minus_2_size = 10
        self.text_minus_2_color = "white"
        self.text_minus_2_family = "Helvetica"
        self.text_minus_2_style = "normal"
        self.text_minus_2_position = 0.2

        # set text settings according to settings file
        self.update_timer_settings(inital_settings)

        # master
        self.master = master
        self.master.title("Workout App")
        self.master.geometry("{0}x{0}".format(self.initial_size))
        self.master.minsize(300, 300)
        self.master.configure(background=self.bgcolor)

        # canvas
        self.canvas = Canvas(self.master)
        self.canvas.pack()
        self.canvas.config(width=self.initial_size, height=self.initial_size, background=self.bgcolor, highlightthickness=0)
        self.ring_arc = self.canvas.create_arc(*self.ring_outter_coords)
        self.canvas.itemconfigure(self.ring_arc, start = 90, extent=270, fill=self.ring_color, width=0)
        self.ring_inner_oval = self.canvas.create_oval(*self.ring_inner_coords, fill=self.bgcolor, outline="")

        # text creation
        self.central_text = self.canvas.create_text(*self.central_text_coords, text="time",
                                                    font=(self.central_text_family,
                                                          self.central_text_size,
                                                          self.central_text_style),
                                                    fill=self.central_text_color)

        self.text_plus_1 = self.canvas.create_text(*self.text_plus_1_coords, text="exercise name",
                                                   font=(self.text_plus_1_family,
                                                          self.text_plus_1_size,
                                                          self.text_plus_1_style),
                                                   fill=self.text_plus_1_color)

        self.text_plus_2 = self.canvas.create_text(*self.text_plus_2_coords, text="repetitions",
                                                   font=(self.text_plus_2_family,
                                                          self.text_plus_2_size,
                                                          self.text_plus_2_style),
                                                   fill=self.text_plus_2_color)

        self.text_minus_1 = self.canvas.create_text(*self.text_minus_1_coords, text="next\nexercise",
                                                    font=(self.text_minus_1_family,
                                                          self.text_minus_1_size,
                                                          self.text_minus_1_style),
                                                    fill=self.text_minus_1_color)

        self.text_minus_2 = self.canvas.create_text(*self.text_minus_2_coords, text="press pause to start",
                                                    font=(self.text_minus_2_family,
                                                          self.text_minus_2_size,
                                                          self.text_minus_2_style),
                                                    fill=self.text_minus_2_color)


    @staticmethod
    def time_to_str(sec):
        sec = int(sec)
        minutes = (sec%(60*60))//60
        seconds = sec%60
        if minutes:
            return "{: 2d}:{:02d}".format(minutes, seconds)
        else:
            return "{: 2d}".format(seconds)

    #TODO finish apply_settings
    def apply_settings(self, settings):
        pass


    def calc_dim(self, x):
        # return x/self.canvas_size
        return x/self.initial_size

    def get_dim(self, x):
        return int(x*self.canvas_size)

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

    # ======================
    # text decorators start
    # ======================
    @property
    def central_text_size(self):
        return self.get_dim(self.__central_text_size)

    @central_text_size.setter
    def central_text_size(self, x):
        self.__central_text_size = self.calc_dim(x)

    @property
    def central_text_coords(self):
        return self.canvas_size//2, self.canvas_size//2

    # text_plus_1
    @property
    def text_plus_1_size(self):
        return self.get_dim(self.__text_plus_1_size)

    @text_plus_1_size.setter
    def text_plus_1_size(self, x):
        self.__text_plus_1_size = self.calc_dim(x)

    @property
    def text_plus_1_coords(self):
        return self.canvas_size//2, int(self.canvas_size * (1-self.text_plus_1_position))

    # text_plus_2
    @property
    def text_plus_2_size(self):
        return self.get_dim(self.__text_plus_2_size)

    @text_plus_2_size.setter
    def text_plus_2_size(self, x):
        self.__text_plus_2_size = self.calc_dim(x)

    @property
    def text_plus_2_coords(self):
        return self.canvas_size//2, int(self.canvas_size * (1-self.text_plus_2_position))

    # text_minus_1
    @property
    def text_minus_1_size(self):
        return self.get_dim(self.__text_minus_1_size)

    @text_minus_1_size.setter
    def text_minus_1_size(self, x):
        self.__text_minus_1_size = self.calc_dim(x)

    @property
    def text_minus_1_coords(self):
        return self.canvas_size//2, int(self.canvas_size * (1-self.text_minus_1_position))

    # text_minus_2
    @property
    def text_minus_2_size(self):
        return self.get_dim(self.__text_minus_2_size)

    @text_minus_2_size.setter
    def text_minus_2_size(self, x):
        self.__text_minus_2_size = self.calc_dim(x)

    @property
    def text_minus_2_coords(self):
        return self.canvas_size//2, int(self.canvas_size * (1-self.text_minus_2_position))
    # ======================
    # text decorators end
    # ======================


    def scale_timer(self, settings):
        self.update_timer_settings(settings)

        self.master.configure(background=self.bgcolor)
        self.canvas.config(background=self.bgcolor)
        self.canvas.itemconfigure(self.ring_inner_oval, fill=self.bgcolor)

        self.canvas.config(width=self.canvas_size, height=self.canvas_size)
        self.canvas.itemconfigure(self.central_text, font=(self.central_text_family,
                                                           self.central_text_size,
                                                           self.central_text_style),
                                  fill=self.central_text_color)

        self.canvas.itemconfigure(self.text_plus_1, font=(self.text_plus_1_family,
                                                          self.text_plus_1_size,
                                                          self.text_plus_1_style),
                                  fill=self.text_plus_1_color)

        self.canvas.itemconfigure(self.text_plus_2, font=(self.text_plus_2_family,
                                                          self.text_plus_2_size,
                                                          self.text_plus_2_style),
                                  fill=self.text_plus_2_color)

        self.canvas.itemconfigure(self.text_minus_1, font=(self.text_minus_1_family,
                                                           self.text_minus_1_size,
                                                           self.text_minus_1_style),
                                  fill=self.text_minus_1_color)

        self.canvas.itemconfigure(self.text_minus_2, font=(self.text_minus_2_family,
                                                           self.text_minus_2_size,
                                                           self.text_minus_2_style),
                                  fill=self.text_minus_2_color)

        self.canvas.coords(self.ring_arc, *self.ring_outter_coords)
        self.canvas.coords(self.ring_inner_oval, *self.ring_inner_coords)
        self.canvas.coords(self.central_text, *self.central_text_coords)
        self.canvas.coords(self.text_plus_1, *self.text_plus_1_coords)
        self.canvas.coords(self.text_plus_2, *self.text_plus_2_coords)
        self.canvas.coords(self.text_minus_1, *self.text_minus_1_coords)
        self.canvas.coords(self.text_minus_2, *self.text_minus_2_coords)

    def update_timer_settings(self, settings):
        for key, value in settings.items():
            if key.find("text") != -1 and key.find("size") != -1:
                value = int(value)
            self.__setattr__(key, value)

    def update_ex(self, current_ex={}, next_ex={}, ring_angle=360):
        current_ex_name = current_ex.get("name", "")
        current_ex_time = current_ex.get("time", "")
        current_ex_repetitions = current_ex.get("repetitions", "")
        current_ex_nr = current_ex.get("ex_nr", "")
        current_ex_nr_of_exs = current_ex.get("nr_of_exs", "")
        current_ex_set_nr = current_ex.get("set_nr", "")
        current_ex_nr_of_sets = current_ex.get("nr_of_sets", "")

        next_ex_name = next_ex.get("name", "")

        self.canvas.itemconfigure(self.central_text, text=self.time_to_str(current_ex_time))
        self.canvas.itemconfigure(self.text_plus_1, text=current_ex_name)
        self.canvas.itemconfigure(self.text_plus_2, text=current_ex_repetitions)
        if current_ex_name:
            self.canvas.itemconfigure(self.text_minus_1, text="{}\n{}".format("next", next_ex_name))
        else:
            self.canvas.itemconfigure(self.text_minus_1, text="")
        if current_ex_nr is -1:
            self.canvas.itemconfigure(self.text_minus_2, text="pause to skip")
        elif current_ex_nr:
            self.canvas.itemconfigure(self.text_minus_2, text="ex {} of {}\nset {} of {}".format(current_ex_nr,
                                                                                                  current_ex_nr_of_exs,
                                                                                                  current_ex_set_nr,
                                                                                                  current_ex_nr_of_sets))

        self.canvas.itemconfigure(self.ring_arc, extent=ring_angle)
