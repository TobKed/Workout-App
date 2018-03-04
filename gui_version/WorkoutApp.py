#!/usr/bin/python3

from files.settings_lib import *
from files.view import *
from files.workout_model import *
from tkinter import *
from datetime import datetime
from datetime import timedelta

SETTINGS_DEFAULT = "settings_default.ini"
SETTINGS_USER = "settings.ini"


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
        if self.model.open_workout_file(last_dir=set.remember_last_directory):
            self.root.deiconify()
            self.root.focus_force()
            self.model.print_test_console_info()
            self.root.mainloop()
        else:
            self._quit()

    def _quit(self):
        self.root.quit()
        self.root.destroy()
        exit()

    def get_next_ex(self, e):
        self.current_ex, self.next_ex = self.model.next_plan_item()
        self.start_countdown()

    def scale_window(self, e):
        self.view.scale_timer()

    def start_countdown(self):
        current_ex_time = int(self.current_ex.get("time", 0))
        if current_ex_time:
            time_start = datetime.now()
            self.current_ex_end_time = time_start + timedelta(seconds=current_ex_time+1)  # +1s for correct display
            self.current_ex_delta_time = self.current_ex_end_time - time_start
            self.view.update_ex(self.current_ex, self.next_ex)
            self.update_timer()

    def update_timer(self):
        self.time_to_end = self.current_ex_end_time - datetime.now()
        # ring angle calculated by dividing time in microseconds
        angle_to_end = ((self.time_to_end.seconds*1000000)+self.time_to_end.microseconds) / \
                       (self.current_ex_delta_time.seconds*1000000)
        angle_to_end = -(360 - (angle_to_end*360))
        # if self.time_to_end.seconds:
        if self.current_ex_end_time >= datetime.now():
            self.current_ex.update({"time": self.time_to_end.seconds})
            self.view.update_ex(self.current_ex, self.next_ex, angle_to_end)
        else:
            self.get_next_ex(0)
        self.root.after(50, self.update_timer)


if __name__ == '__main__':
    c = WorkoutApp()
    set = Settings(SETTINGS_DEFAULT)
    c.run()
