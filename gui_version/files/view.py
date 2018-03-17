from tkinter import *
from tkinter.ttk import *
from tkinter import font
from tkinter.colorchooser import *
import tkinter.font as tkfont

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
        self.central_text_position = 0.5

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
        # return self.canvas_size//2, self.canvas_size//2
        return self.canvas_size // 2, int(self.canvas_size * (1 - self.central_text_position))

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


class OptionsWindow():
    def __init__(self, app, master, settings_obj):
        self.app = app
        self.opt_win = Toplevel(master)
        self.master = master
        self.win_settings = getattr(settings_obj, 'timer_window_settings', None)
        self.rem_last_dir = getattr(settings_obj, 'remember_last_directory', None)

        # self.opt_win.geometry("{0}x{0}".format(200, 200))
        self.opt_win.title("Options")
        self.opt_win.resizable(0, 0)

        # Tab Control / Notebook
        self.tabControl = Notebook(self.opt_win)
        self.tab1 = Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='general')
        self.tab2 = Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='main window')
        self.tab3 = Frame(self.tabControl)
        self.tabControl.add(self.tab3, text='central text')
        self.tab4 = Frame(self.tabControl)
        self.tabControl.add(self.tab4, text='exercise name text')
        self.tab5 = Frame(self.tabControl)
        self.tabControl.add(self.tab5, text='repetitions text')
        self.tab6 = Frame(self.tabControl)
        self.tabControl.add(self.tab6, text='next exercise text')
        self.tab7 = Frame(self.tabControl)
        self.tabControl.add(self.tab7, text='info text')
        self.tabControl.pack(expand=1, fill="both")

        # control buttons
        self.control_buttons_frame = Frame(self.opt_win)
        self.btn_Apply = Button(self.control_buttons_frame, text='Apply', command=self.save_and_apply_settings)
        self.btn_Cancel = Button(self.control_buttons_frame, text='Cancel')
        self.btn_Reset = Button(self.control_buttons_frame, text='Reset')
        self.btn_Defaults = Button(self.control_buttons_frame, text='Defaults', command=self.get_defaults)
        for tmp in self.control_buttons_frame.winfo_children():
            tmp.pack(side=LEFT)
        self.control_buttons_frame.pack(side=RIGHT)

        # save last dir
        self.var_rem_last_dir = BooleanVar()
        self.var_rem_last_dir.set(self.rem_last_dir)
        self.btn_rem_last_dir = Checkbutton(self.tab1, text='Remember last directory', variable=self.var_rem_last_dir,
                                            onvalue=True, offvalue=False, command=self.save_and_apply_settings)
        self.btn_rem_last_dir.grid(column=0, row=0)

        self.texts = ["central_text", "text_plus_1", "text_plus_2", "text_minus_1", "text_minus_2"]
        self.text_tabs = self.tabControl.winfo_children()[2:]
        for tab in self.text_tabs:
            idx = self.text_tabs.index(tab)
            tab.idx = idx
            text_name = self.texts[idx]
            tab.opt_frame = Frame(tab)
            tab.opt_frame.config(height=100)
            tab.opt_frame.pack(expand=1, fill="both", padx=10, pady=10)

            lbl_font = Label(tab.opt_frame, text="Font:")
            lbl_font.grid(column=0, row=0, sticky='E')
            tab.ent_font = Combobox(tab.opt_frame, values=font.families())
            tab.ent_font.set(self.win_settings.get(text_name + "_family"))
            tab.ent_font.grid(column=1, row=0, columnspan=2, sticky='EW')
            tab.ent_font.bind('<<ComboboxSelected>>', self.save_and_apply_settings)

            lbl_size = Label(tab.opt_frame, text="Size:")
            lbl_size.grid(column=0, row=1, sticky='E')
            tab.ent_size = Combobox(tab.opt_frame, values=tuple(range(0, 41)))
            tab.ent_size.set(self.win_settings.get(text_name + "_size"))
            tab.ent_size.grid(column=1, row=1, columnspan=2, sticky='EW')
            tab.ent_size.bind('<<ComboboxSelected>>', self.save_and_apply_settings)

            lbl_style = Label(tab.opt_frame, text="Style:")
            lbl_style.grid(column=0, row=2, sticky='E')
            tab.ent_style = Combobox(tab.opt_frame, values = ("normal", "bold", "roman", "italic", "underline", "overstrike"))
            tab.ent_style.set(self.win_settings.get(text_name +"_style"))
            tab.ent_style.grid(column=1, row=2, columnspan=2, sticky='EW')
            tab.ent_style.bind('<<ComboboxSelected>>', self.save_and_apply_settings)

            tab.lbl_color = Label(tab.opt_frame, text="Color:").grid(column=0, row=3, sticky='E')
            tab.cur_color = text=self.win_settings.get(text_name +"_color")
            # tab.lbl_cur_col = Label(tab.opt_frame, text=tab.cur_color)
            # tab.lbl_cur_col.grid(column=1, row=3, sticky='EW')
            tab.ent_color = Button(tab.opt_frame, text="Color chooser", command=self.getColor)
            tab.ent_color.grid(column=1, row=3, columnspan=2, sticky='EW')

            lbl_pos = Label(tab.opt_frame, text="Position:")
            lbl_pos.grid(column=3, row=0, )
            tab.ent_pos = Scale(tab.opt_frame, orient=VERTICAL, value=self.win_settings.get(text_name +"_position"),
                                from_=1, to=0, command=self.save_and_apply_settings)
            tab.ent_pos.grid(column=3, row=1, rowspan=4)

            tab.opt_frame.columnconfigure(3, minsize=100)

            # Add some space around each label
            for child in tab.opt_frame.winfo_children():
                child.grid_configure(padx=4, pady=2)

    def getColor(self):
        idx = self.tabControl.index(self.tabControl.select())
        color = askcolor(parent=self.opt_win)
        print(idx, color[1])
        if idx > 1:
            self.win_settings.update({self.texts[idx-2] + '_color': color[1]})
        self.save_and_apply_settings()

    def save_and_apply_settings(self, e=None):
        for tab in self.text_tabs:
            idx = self.text_tabs.index(tab)
            text_name = self.texts[idx]
            self.win_settings.update({text_name + '_family': tab.ent_font.get()})
            self.win_settings.update({text_name + '_size': tab.ent_size.get()})
            self.win_settings.update({text_name + '_style': tab.ent_style.get()})
            # self.win_settings.update({text_name + '_color': tab.cur_color})
            self.win_settings.update({text_name + '_position': tab.ent_pos.get()})
        self.app.save_and_apply_settings(timer_window_settings=self.win_settings,
                                         remember_last_directory=self.var_rem_last_dir.get())

    def get_defaults(self):
        self.app.get_default_settings()
