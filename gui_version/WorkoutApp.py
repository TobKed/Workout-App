#!/usr/bin/python3

from files.workout_lib import *
import settings_default

def main():
    x = Workout()
    x.open_workout_file(last_dir=settings_default.settings.get("remember_last_directory", False))

    for i in x.exercises:
        print(i.exercise_name, i.rep_time_plan, i.nr_of_sets)

    for test_counter in range(10):
        try:
            print(x.exercises[0].exercise_name, x.exercises[0].__next__())
        except:
            break


if __name__ == "__main__": main()
