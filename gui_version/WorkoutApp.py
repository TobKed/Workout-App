#!/usr/bin/python3

from files.workout_lib import *
from files.utilities import *


def main():
    x = Workout()
    x.open_workout_file()
    x.parse_workout_file()

    for i in x.exercises:
        print(i.exercise_name, i.rep_time_plan, i.nr_of_sets)


if __name__ == "__main__": main()

