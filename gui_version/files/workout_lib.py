# handling workout object
import csv
from os import getcwd
from tkinter import filedialog

import files.utilities


class Exercise:
    def __init__(self, exercise_name = "", rep_time_plan=[]):
        self.exercise_name = exercise_name
        self.rep_time_plan = self.rep_time_plan_parse(rep_time_plan)
        # self.rep_time_plan = rep_time_plan
        self.nr_of_sets = self.nr_of_sets()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.idx is not None: pass
        except:
            self.idx = 0
        try:
            item = self.rep_time_plan[self.idx]
            self.idx += 1
        except IndexError:
            self.idx = 0
            raise StopIteration()
        return item

    def nr_of_sets(self):
        return len(self.rep_time_plan)

    @staticmethod
    def rep_time_plan_parse(raw_list):
        tmp = list(map(lambda s: s.replace(" ", "").split(",") if s else None, raw_list))
        return [x for x in tmp if x is not None]


class Break_:
    def __init__(self, break_type, break_time=0):
        self.type = break_type
        self.time = break_time


class Workout:
    def __init__(self, workout_name="", exercises=[], break_exercise=10, break_set=30, structure="circuit"):
        self.workout_name = workout_name
        self.exercises = exercises
        self.break_exercise = Break_(break_type="short break", break_time=break_exercise)
        self.break_set = Break_(break_type="long break", break_time=break_exercise)
        self.structure = structure

    def open_workout_file(self, last_dir = True):
        if last_dir:
            files.utilities.get_last_dir()
            init_dir = files.utilities.LAST_DIR
        else:
            init_dir = getcwd()
        print(init_dir)
        self.filename = filedialog.askopenfilename(initialdir=init_dir, title="Open workout csv file",
                                                   filetypes=(("csv file", "*.csv"), ("all files", "*.*")),
                                                   multiple=False)
        if last_dir:
            files.utilities.LAST_DIR = files.utilities.save_last_dir(self.filename)
        if self.filename:
            try:
                self.parse_workout_file()
            except Exception as e:
                print("Error during parsing csv file:\n\t{}".format(e))

    def parse_workout_file(self):
        with open(self.filename) as csvDataFile:
            csv_reader = csv.reader(csvDataFile, delimiter=';')
            self.workout_name = csv_reader.__next__()[1]
            self.structure = csv_reader.__next__()[1]
            break_exercise = csv_reader.__next__()
            self.break_exercise = Break_(break_type=break_exercise[0], break_time=break_exercise[1])
            break_set = csv_reader.__next__()
            self.break_set = Break_(break_type=break_set[0], break_time=break_set[1])
            for x in range(2): csv_reader.__next__()
            for row in csv_reader:
                self.exercises.append(Exercise(row[0], row[1:]))

    def print_test_console_info(self):
        print()
        print("workout exercises:")
        for i in self.exercises:
            print(i.exercise_name, i.rep_time_plan, i.nr_of_sets)

        print()
        print("workout breaks:")
        print(self.break_exercise.type, self.break_exercise.time)
        print(self.break_set.type, self.break_set.time)

        print()
        print("exercise iterator test (exercise sets {}) (range 10):".format(self.exercises[0].nr_of_sets))
        for test_counter in range(10):
            try:
                print(self.exercises[0].exercise_name, self.exercises[0].__next__())
            except StopIteration:
                break

