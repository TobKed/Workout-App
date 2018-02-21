#!/usr/bin/python3

from files.workout_lib import *


def main():
    x = Workout()
    x.open_workout_file()
    x.parse_workout_file()


if __name__ == "__main__": main()

