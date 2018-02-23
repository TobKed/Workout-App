#!/usr/bin/python3

from files.workout_lib import *
import settings_default


def main():
    remember_last_dir = settings_default.settings.get("remember_last_directory", False)
    x = Workout()
    x.open_workout_file(last_dir=remember_last_dir)
    x.print_test_console_info()


if __name__ == "__main__":
    main()
