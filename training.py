class Workout(object):
    """  workout class
        name -   workout name,
        plan -   list of  repetitions and time for each excercise and set

                                      set   1                   2
                           name             repetitions, time   repetitions, time
                member [["jumpin jacks", [  [25,45],            [30, 60]]   ]

               plan[e] - consective excercise e block
               plan[e][0] - excercise e name
               plan[e][1] - excercise e matrix
               plan[e][1][s] - excercise e set s  list of blocks [reps, time]
               plan[e][1][s][0] - excercise e set s repetetions r
               plan[e][1][s][1] - excercise e set s time t

        break_excercise -   break between excercises in set (s)
        break_set -         break between sets (s)
    """
    _registry = []  # list of all instances
    _position = 0  # position(index) of selected workout in _registry

    def __init__(self, name="", plan=None, break_excercise=10, break_set=30, structure="circuit"):
        self._registry.append(self)
        self.name = name
        if plan == None:
            plan = [["push ups", [[10, 60], [10, 60]]]]
        self.plan = plan
        self.break_excercise = break_excercise
        self.break_set = break_set
        self.structure = structure
        self.nr_of_sets = max([len(x[1]) for x in self.plan])
        self.nr_of_exercises = len(self.plan)

    def GetExcerciseName(self, ex_nr, ser):
        return self.plan[ex_nr][0]

    def GetRepetitionsTime(self, ex_nr, set):
        return self.plan[ex_nr][1][set]

    def GetRepetitions(self, ex_nr, set):
        return self.plan[ex_nr][1][set][0]

    def GetTime(self, ex_nr, set):
        return self.plan[ex_nr][1][set][1]

    def GetPlan(self):
        return [x[0] for x in self.plan]

    def GetNrOfExcercises(self):
        self.nr_of_exercises = len(self.plan)
        return self.nr_of_exercises

    def GetNumberOfSets(self):
        self.nr_of_sets = max([len(x[1]) for x in self.plan])
        return self.nr_of_sets

    @classmethod
    def GetListOfWorkouts(cls):
        return list(cls._registry)

    @classmethod
    def GetNumberOfWorkouts(cls):
        return len(cls._registry)

    @classmethod
    def GetPosition(cls):
        return cls._position

    @classmethod
    def ChangeSelectionRight(cls):
        # switch workout right
        if cls._position == cls.GetNumberOfWorkouts() - 1:
            cls._position = 0
        else:
            cls._position += 1

    @classmethod
    def ChangeSelectionLeft(cls):
        # switch workout left
        if cls._position == 0:
            cls._position = cls.GetNumberOfWorkouts() - 1
        else:
            cls._position -= 1

    @classmethod
    def GetWorkout(cls):
        """ return workout object from list of all workouts (_registry)
        index is based on the _position class atribute
        """
        return cls._registry[cls._position]

    def printWorkout(self):
        """  print the informations about workout (times, repetitions, plan) """
        print("\t%-25s %s" % ("workout name:", self.name))
        print("\t%-25s %s" % ("structure:", self.structure))
        print("\t%-25s %s" % ("max. number of sets:", self.GetNumberOfSets()))
        print("\t%-25s %s" % ("number of excerices:", self.GetNrOfExcercises()))
        print("\t%-25s %s%s" % ("break between excercises:", self.break_excercise, "s"))
        print("\t%-25s %s%s" % ("break between sets:", self.break_set, "s"))
        # nr_of_sets = mself.nr_of_sets
        print("\n\t%-30s" % "set: ", end=' ')
        for x in range(self.nr_of_sets):
            print("%-16s" % (x + 1), end=" ")
        print("\n\t%-25s" % ("repetitions - time"), end=' ')
        for x in range(self.nr_of_sets):
            print("%-6s %-8s " % ("reps", "time"), end=" ")
        for row in self.plan:
            print("\n\t%-25s" % row[0], end=' ')
            for block in row[1]:
                if block[0] == -1:
                    rep = "hold"
                else:
                    rep = str(block[0]) + "x"
                time = str(block[1]) + "s"
                print("%-6s %-8s " % (rep, time), end=" ")
        print("\n")


oneFiveMin = Workout(name="15 minutes workout",
                     plan=[["jumpin jacks", [[25, 45], [30, 60], [35, 60]]], \
                           ["squats", [[25, 60], [30, 75], [35, 75]]], \
                           ["plank", [[-1, 25], [-1, 30], [-1, 35]]], \
                           ["lunges", [[20, 60], [24, 75], [28, 75]]], \
                           ["push ups", [[10, 30], [12, 45], [15, 45]]], \
                           ["crunches", [[25, 75], [30, 90], [35, 90]]]],
                     break_excercise=10,
                     break_set=30,
                     structure="circuit")

bodyTooningWorkout = Workout(name="body tooning workout",
                             plan=[["squats", [[25, 45]]], \
                                   ["push ups", [[30, 120]]], \
                                   ["burpees", [[30, 120]]], \
                                   ["crunches", [[30, 120]]], \
                                   ["dips", [[30, 120]]]],
                             break_excercise=60,
                             break_set=0,
                             structure="circuit")

rollWithIt = Workout(name="roll with it",
                     plan=[["roll ins", [[10, 60], [10, 60], [10, 60]]], \
                           ["push ups", [[10, 60], [10, 60], [10, 60]]], \
                           ["bridges", [[10, 60], [10, 60], [10, 60]]], \
                           ["crunches", [[20, 60], [20, 60], [20, 60]]], \
                           ["side crunches", [[20, 60], [20, 60], [20, 60]]], \
                           ["back ext.", [[20, 60], [20, 60], [20, 60]]]],
                     break_excercise=30,
                     break_set=120,
                     structure="circuit")

betterSleep = Workout(name="better sleep yoga",
                      plan=[["hero pose", [[-1, 20]]], \
                            ["child pose", [[-1, 20]]], \
                            ["upward dog", [[-1, 20]]], \
                            ["camel pose", [[-1, 20]]], \
                            ["butterfly fold", [[-1, 20]]], \
                            ["supine twis", [[-1, 20]]], \
                            ["bridge", [[-1, 20]]], \
                            ["knee-to-chest", [[-1, 20]]], \
                            ["corpse pose", [[-1, 20]]]],
                      break_excercise=10,
                      break_set=10,
                      structure="circuit")

fullBodyStretch = Workout(name="full body stretch",
                          plan=[["neck s.", [[-1, 40]]], \
                                ["shoulder s.", [[-1, 40]]], \
                                ["tricep s.", [[-1, 40]]], \
                                ["pelvic s.", [[-1, 40]]], \
                                ["quad s.", [[-1, 40]]], \
                                ["forward bend", [[-1, 40]]]],
                          break_excercise=10,
                          break_set=10,
                          structure="circuit")

dayBreak = Workout(name="daybreak",
                   plan=[["crapula shr.", [[10, 40], [10, 40], [10, 40], [10, 40]]], \
                         ["r. angels", [[10, 40], [10, 40], [10, 40], [10, 40]]], \
                         ["extensions", [[10, 40], [10, 40], [10, 40], [10, 40]]], \
                         ["r. prone", [[10, 40], [10, 40], [10, 40], [10, 40]]], \
                         ["quad s.", [[10, 40], [10, 40], [10, 40], [10, 40]]], \
                         ["forward bend", [[10, 40], [10, 40], [10, 40], [10, 40]]]],
                   break_excercise=20,
                   break_set=120,
                   structure="classic")

if __name__ == "__main__":
    for workout_object in Workout._registry:
        workout_object.printWorkout()
        print()
