class Workout(object):
    """
    workout class
               plan[e] - consective excercise e block
               plan[e][0] - excercise e name
               plan[e][1] - excercise e matrix
               plan[e][1][s] - excercise e set s  list of blocks [reps, time]
               plan[e][1][s][0] - excercise e set s repetetions r
               plan[e][1][s][1] - excercise e set s time t
    """
    def __init__(self):
        self.name = ""
        self.plan = [   ["", [ [None, None], [None, None] ] ] ]
        self.break_excercise =   10
        self.break_set =         30
        self.nr_of_sets = max( [len(x[1]) for x in self.plan] )
        self.nr_of_exercises = len(self.plan)
    def exName(self, ex_nr, ser):
        return self.plan[ex_nr][0]
    def repsTime(self, ex_nr, set):
        return self.plan[ex_nr][1][set]
    def exReps(self, ex_nr, set):
        return self.plan[ex_nr][1][set][0]
    def exTime(self, ex_nr, set):
        return self.plan[ex_nr][1][set][1]
    def exList(self):
        return [x[0] for x in self.plan]
    def nrOfExs(self):
        return len(self.plan)
    def nrOfSets(self):
        max([len(x[1]) for x in self.plan])
    def printWorkout(self):
        print("\t%-25s %s" %("workout name:", self.name))
        print("\t%-25s %s" %("snumber of sets:", self.nr_of_sets+1))
        print("\t%-25s %s" %("number of excerices:", self.nrOfExs()))
        print("\t%-25s %s%s" %("break between excercises:", self.break_excercise, "s"))
        print("\t%-25s %s%s" %("break between sets:", self.break_set, "s"))
        # nr_of_sets = mself.nr_of_sets
        print("\n\t%-30s" %"set: " , end=' ')
        for x in range(self.nr_of_sets+1):
            print("%-16s" %(x+1), end=" ")
        print("\n\t%-25s" % ("repetitions - time"), end=' ')
        for x in range(self.nr_of_sets+1):
            print("%-6s %-8s " % ("reps", "time"), end=" ")
        for row in self.plan:
            print("\n\t%-25s" %row[0], end=' ')
            for block in row[1]:
                if block[0] == -1: rep = "hold"
                else: rep = str(block[0])+"x"
                time = str(block[1])+"s"
                print("%-6s %-8s " % (rep, time), end=" ")
        print("\n")

oneFiveMin = Workout()
oneFiveMin.name = "15 minutes workout"
oneFiveMin.plan= [      ["jumpin jacks",   [   [25, 45], [30, 60], [35, 60]]   ],\
                        ["squats",         [   [25, 60], [30, 75], [35, 75]]   ],\
                        ["plank",          [   [-1, 25], [-1, 30], [-1, 35]]   ],\
                        ["lunges",         [   [20, 60], [24, 75], [28, 75]]   ],\
                        ["push ups",       [   [10, 30], [12, 45], [15, 45]]   ],\
                        ["crunches",       [   [25, 75], [30, 90], [35, 90]]   ] ]
oneFiveMin.break_excercise =   10
oneFiveMin.break_set =         30