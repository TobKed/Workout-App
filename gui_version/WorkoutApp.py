#!/usr/bin/python3

import settings_default
from files.view import *
from files.workout_model import *
from tkinter import *


class WorkoutApp:
    def __init__(self):
        self.root = Tk()
        self.model = Workout()
        self.view = Timer(self.root)
        self.root.bind('<space>', self.get_item)
        self.root.bind('<Configure>', self.scale_window)

    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        remember_last_dir = settings_default.settings.get("remember_last_directory", False)
        self.model.open_workout_file(last_dir=remember_last_dir)
        self.model.print_test_console_info()
        self.root.mainloop()

    def get_item(self, e):
        self.model.next_plan_item(e)

    def scale_window(self, e):
        self.view.scale_timer()


if __name__ == '__main__':
    c = WorkoutApp()
    c.run()
