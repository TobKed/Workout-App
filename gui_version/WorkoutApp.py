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
        self.root.bind('<space>', self.get_next_ex)
        self.root.bind('<Configure>', self.scale_window)

    def run(self):
        self.root.title("WorkoutApp")
        self.root.withdraw()
        remember_last_dir = settings_default.settings.get("remember_last_directory", False)
        if self.model.open_workout_file(last_dir=remember_last_dir):
            self.root.deiconify()
            self.root.focus_force()
            self.model.print_test_console_info()
            self.root.mainloop()
        else:
            self.root.destroy

    def get_next_ex(self, e):
        current_ex, next_ex = self.model.next_plan_item(e)
        self.view.update_ex(current_ex, next_ex)

    def scale_window(self, e):
        self.view.scale_timer()


if __name__ == '__main__':
    c = WorkoutApp()
    c.run()
