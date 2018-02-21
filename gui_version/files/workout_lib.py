# handling workout object
import csv
from os import getcwd
from tkinter import filedialog


class Excercise():
    def __init__(self, workout_name = "", rep_time_plan=[]):
        self.workout_name = workout_name
        self.rep_time_plan = rep_time_plan
        self.nr_of_sets = self.nr_of_sets()

    def nr_of_sets(self):
        return len(self.rep_time_plan)


class Workout():

    def __init__(self, name="", plan=None, break_excercise=10, break_set=30, structure="circuit"):
        self._registry.append(self)
        self.name = name
        if plan == None:
            plan = [["push ups", [[10, 60], [10, 60]]]]
        self.plan = plan
        self.break_excercise = break_excercise
        self.break_set = break_set
        self.structure = structure

    def open_workout_file(self):
        self.filename = filedialog.askopenfilename(initialdir=getcwd(), title="Open workout csv file",
                                                        filetypes=(("csv file", "*.csv"), ("all files", "*.*")),
                                                        multiple=False)

    def parse_workout_file(self):
        with open(self.filename) as csvDataFile:
            csv_reader = csv.reader(csvDataFile, delimiter=';')
            self.workout_name = csv_reader.__next__()[1]
            self.structure = csv_reader.__next__()[1]
            self.break_excercise = csv_reader.__next__()[1]
            self.break_set = csv_reader.__next__()[1]
            for x in range(2): csv_reader.__next__()
            for row in csv_reader:
                print(row)



