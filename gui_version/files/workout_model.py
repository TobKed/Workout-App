# handling workout object
import csv
from os import getcwd
from tkinter import filedialog

import files.utilities


class Exercise:
    def __init__(self, exercise_name = "", rep_time_plan=[]):
        self.exercise_name = exercise_name
        self.rep_time_plan = self.rep_time_plan_parse(rep_time_plan)
        self.nr_of_sets = self.nr_of_sets()
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self, ex_nr=0, nr_of_exs=1):
        try:
            item = {"name": self.exercise_name, "repetitions": self.rep_time_plan[self.idx][0],
                    "time": self.rep_time_plan[self.idx][1],
                    "set_nr": self.idx+1,
                    "nr_of_sets": self.nr_of_sets,
                    "ex_nr": ex_nr,
                    "nr_of_exs": nr_of_exs}
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

    def get_break(self):
        return {"name": self.type, "time": self.time}


class Workout:
    def __init__(self, workout_name="", exercises=[], break_exercise=10, break_set=30, structure="circuit"):
        self.workout_name = workout_name
        self.break_start = Break_(break_type="get ready!", break_time=10)
        self.break_exercise = Break_(break_type="short break", break_time=break_exercise)
        self.break_set = Break_(break_type="long break", break_time=break_set)
        self.structure = structure
        self.exercises = exercises
        self.plan = []
        self.plan_idx = 0
        self.filename = ""
        self.max_nr_of_sets = 0

    def open_workout_file(self, last_dir=True):
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
                return True
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
            self.set_max_nr_of_sets()
            self.fill_plan()

    def set_max_nr_of_sets(self):
        if self.structure == "classic":
            self.max_nr_of_sets = len(self.exercises)
        elif self.structure == "circuit":
            self.max_nr_of_sets = (max(list(ex.nr_of_sets for ex in self.exercises)))

    #TODO
    def verify_workout_file(self):
        pass

    def fill_plan(self):
        self.plan.append(self.break_start.get_break())
        self.plan[0].update({"ex_nr":-1})
        nr_of_exs = len(self.exercises)
        if self.structure == "classic":
            for ex_obj in self.exercises:
                for set_counter in range(ex_obj.nr_of_sets):
                    self.plan.extend([ex_obj.__next__(ex_nr=self.exercises.index(ex_obj)+1, nr_of_exs=nr_of_exs),
                                      self.break_exercise.get_break()])
                del self.plan[-1]
                self.plan.append(self.break_set.get_break())
            del self.plan[-1]
        elif self.structure == "circuit":
            for set_counter in range(self.max_nr_of_sets):
                ex_counter = 0
                for ex_obj in self.exercises:
                    if ex_obj.idx < ex_obj.nr_of_sets:
                        ex_counter += 1
                        self.plan.extend([ex_obj.__next__(ex_nr=ex_counter, nr_of_exs=nr_of_exs),
                                          self.break_exercise.get_break()])
                del self.plan[-1]
                self.plan.append(self.break_set.get_break())
            del self.plan[-1]

    def next_plan_item(self):
        if self.plan_idx < len(self.plan):
            self.plan_idx += 1
            if self.plan_idx-1 < len(self.plan)-1:
                return self.plan[self.plan_idx-1], self.plan[self.plan_idx]
            else:
                return self.plan[self.plan_idx-1], {"name": "END"}
        else:
            self.plan_idx = 0
            return {'ex_nr':-1}, {}


    def print_test_console_info(self):
        print()
        print("structure:", self.structure)
        print("max_nr_of_sets", self.max_nr_of_sets)

        print()
        print("workout exercises:")
        for i in self.exercises:
            print(i.exercise_name, i.rep_time_plan, i.nr_of_sets)

        # print()
        # print("workout breaks:")
        # print(self.break_exercise.type, self.break_exercise.time)
        # print(self.break_set.type, self.break_set.time)

        # print()
        # print("exercise iterator test")
        # for ex in self.exercises[0]:
        #     print(ex)
        #
        # print()
        # print("exercise iterator test (exercise sets {}) (range 10):".format(self.exercises[0].nr_of_sets))
        # for test_counter in range(10):
        #     try:
        #         print(self.exercises[0].exercise_name, self.exercises[0].__next__())
        #     except StopIteration:
        #         break

        print()
        print("plan")
        print(self.plan)
        # for plan_obj in self.plan:
        #     if isinstance(plan_obj, Break_):
        #         print(plan_obj.type)
        #     if isinstance(plan_obj, Exercise):
        #         print(plan_obj.exercise_name)

        # for plan_obj in self.plan:
        #     print(plan_obj)

        # print()
        # print("self/exercises:")
        # for i in self.exercises:
        #     print(i.exercise_name)




