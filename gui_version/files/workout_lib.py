# handling workout object
import csv
from os import getcwd
from tkinter import filedialog

import utilities


class Exercise():
    def __init__(self, exercise_name = "", rep_time_plan=None):
        self.exercise_name = exercise_name
        self.rep_time_plan = self.rep_time_plan_parse(rep_time_plan)
        self.nr_of_sets = self.nr_of_sets()

    def nr_of_sets(self):
        return len(self.rep_time_plan)

    @staticmethod
    def rep_time_plan_parse(raw_list):
        return list(map(lambda s: s.replace(" ", "").split(","), raw_list))


class Workout():
    def __init__(self, workout_name="", exercises=None, break_exercise=10, break_set=30, structure="circuit"):
        self.workout_name = workout_name
        self.exercises = exercises
        self.break_exercise = break_exercise
        self.break_set = break_set
        self.structure = structure

    def open_workout_file(self, last_dir = True):
        if last_dir and utilities.LAST_DIR:
            init_dir = utilities.LAST_DIR
        else:
            init_dir = getcwd()
        print(init_dir)
        self.filename = filedialog.askopenfilename(initialdir=init_dir, title="Open workout csv file",
                                              filetypes=(("csv file", "*.csv"), ("all files", "*.*")), multiple=False)
        utilities.LAST_DIR = utilities.get_last_dir_from_path(self.filename)

    def parse_workout_file(self):
        with open(self.filename) as csvDataFile:
            csv_reader = csv.reader(csvDataFile, delimiter=';')
            self.workout_name = csv_reader.__next__()[1]
            self.structure = csv_reader.__next__()[1]
            self.break_exercise = csv_reader.__next__()[1]
            self.break_set = csv_reader.__next__()[1]
            for x in range(2): csv_reader.__next__()
            for row in csv_reader:
                self.exercises.append(Exercise(row[0], row[1:]))





