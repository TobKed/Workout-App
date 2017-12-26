#!/usr/bin/env python 

import os
import time
import winsound
import msvcrt
from ascii import *
from training import *


def printer(timer=0, ex_reps ="", ex_name="", next_ex_reps="", next_ex_name="", info="  NEXT:  " ):
    os.system('cls')
    pause = False
    if timer == 0:
        while True:
            print("\n")
            printASCII("  " + str(ex_reps))
            printASCII("  " + ex_name)
            print(info.center(120, "."))
            print("\n")
            printASCII("  " + str(next_ex_reps))
            printASCII("  " + next_ex_name)
            key_pressed = kbfunc()
            if key_pressed == 32:  # space
                break
            if key_pressed == 27:  # escape
                MainMenu()
            time.sleep(0.4)
            os.system('cls')
    else:
        for x in range(timer, -1, -1):
            minutes = str((x%3600)//60).zfill(2)
            seconds = str(x%60).zfill(2)
            time_to_action = "  " + minutes + ":" + seconds
            print("\n")
            if ex_reps == " ":
                printASCII(" ")
            elif ex_reps == -1:
                printASCII("  hold")
            elif ex_reps == "":
                pass
            else:
                printASCII("  " + str(ex_reps) + " x")
            printASCII("  " + ex_name)
            printASCII(time_to_action)
            print(info.center(120, "."))
            print("\n")
            if next_ex_reps == " ":
                printASCII(" ")
            elif next_ex_reps == -1:
                printASCII("  hold")
            elif next_ex_reps == "":
                pass
            else:
                printASCII("  " + str(next_ex_reps) + " x")
            printASCII("  " + next_ex_name)
            if  x == 0:
                winsound.Beep(3500, 200)
                time.sleep(0.1)
                winsound.Beep(3500, 200)
                time.sleep(0.5)
            elif  x <= 4:
                winsound.Beep(2500, 500)
                time.sleep(0.5)
            else:
                time.sleep(1)
            os.system('cls')
            key_pressed = kbfunc()
            if key_pressed == 32:   #space
                break
            if key_pressed== 27:   #escape
                MainMenu()
            # if key_pressed == 112:   #P
            if key_pressed != 0:  # P
                pause = True
            while pause == True:
                key_pressed = kbfunc()
                if key_pressed == 27:  # escape
                    MainMenu()
                if key_pressed == 224:  # special (two character are returned)
                    kbfunc()
                    pause = False
                if key_pressed != 0:  # P
                    pause = False
                print("\n\n")
                printASCII("   PAUSE")
                time.sleep(0.5)
                os.system('cls')

def Duration(start, end):
    """ return string which contains time duration between start and end time (from int(time.time())
    return time format: MM:SS
    return example: "01:34"
    """
    duration = end - start
    minutes = str((duration % 3600) // 60).zfill(2)
    seconds = str(duration % 60).zfill(2)
    return "  " + minutes + ":" + seconds

def doWorkout(workout):
    nr_of_exercises = workout.GetNrOfExcercises()
    nr_of_sets = workout.GetNumberOfSets()
    start_time = int(time.time())
    printer(timer=workout.break_excercise,
            ex_reps=" ",
            ex_name="get ready",
            next_ex_reps=workout.GetRepetitions(0, 0),
            next_ex_name=workout.GetExcerciseName(0, 0),
            info="  SET {0}/{1} WILL START , NEXT:  ".format(1, nr_of_sets))
    if workout.structure == "circuit":
        for serie in range(nr_of_sets):
            for ex_nr in range(nr_of_exercises):
                if ex_nr == (nr_of_exercises-1) and serie ==(nr_of_sets-1):    # lest, finish fater that
                    printer(timer =         workout.GetTime(ex_nr, serie),
                            ex_reps =       workout.GetRepetitions(ex_nr, serie),
                            ex_name =       workout.GetExcerciseName(ex_nr, serie),
                            next_ex_reps =  "",
                            next_ex_name =  "the end",
                            info = "  SET {0}/{1}, EX({2}/{3}, NEXT:  ".format(serie + 1, nr_of_sets, ex_nr + 1, nr_of_exercises))
                    stop_time = int(time.time())
                    printer(timer =         0,
                            ex_reps =       "",
                            ex_name =       "  GOOD JOB",
                            next_ex_reps =  "TIME: " + Duration(start_time, stop_time),
                            next_ex_name =  "",
                            info="  YOU'VE JUST FINISHED " + workout.name + " :  ")

                elif ex_nr == (nr_of_exercises-1):                          # last in set
                    printer(timer =         workout.GetTime(ex_nr, serie),
                            ex_reps =       workout.GetRepetitions(ex_nr, serie),
                            ex_name =       workout.GetExcerciseName(ex_nr, serie),
                            next_ex_reps =  "",
                            next_ex_name =  "long break",
                            info="  SET {0}/{1}, EX({2}/{3}, NEXT:  ".format(serie + 1, nr_of_sets, ex_nr + 1, nr_of_exercises))
                    printer(timer =         workout.break_set,
                            ex_reps =       " ",
                            ex_name =       "long break",
                            next_ex_reps =  workout.GetRepetitions(0, serie+1),
                            next_ex_name =  workout.GetExcerciseName(0, serie+1),
                            info="  SET {0}/{1} EX({2}/{3}, WILL START , NEXT:  ".format(serie+2, nr_of_sets, ex_nr+1, nr_of_exercises))

                else:                                                       # rest
                    printer(timer =         workout.GetTime(ex_nr, serie),
                            ex_reps =       workout.GetRepetitions(ex_nr, serie),
                            ex_name =       workout.GetExcerciseName(ex_nr, serie),
                            next_ex_reps =  "",
                            next_ex_name =  "break",
                            info="  SET {0}/{1}, EX({2}/{3}, NEXT:  ".format(serie+1, nr_of_sets, ex_nr+1, nr_of_exercises))
                    printer(timer =         workout.break_excercise,
                            ex_reps =       " ",
                            ex_name =       "break",
                            next_ex_reps =  workout.GetRepetitions(ex_nr+1, serie),
                            next_ex_name =  workout.GetExcerciseName(ex_nr+1, serie),
                            info="  SET {0}/{1}, EX({2}/{3}, NEXT:  ".format(serie + 1, nr_of_sets, ex_nr+1, nr_of_exercises))

##################################################################################################################################################
##                CLASSIC STruCt
##################################################################################################################################################
    # if workout.structure == "classic":
    #     for serie in range(nr_of_sets):
    #         for ex_nr in range(nr_of_exercises):
    #             if ex_nr == (nr_of_exercises-1) and serie ==(nr_of_sets-1):    # lest, finish fater that
    #                 printer(timer =         workout.GetTime(ex_nr, serie),
    #                         ex_reps =       workout.GetRepetitions(ex_nr, serie),
    #                         ex_name =       workout.GetExcerciseName(ex_nr, serie),
    #                         next_ex_reps =  "",
    #                         next_ex_name =  "the end",
    #                         info="  END OF SET {0}/{1} , NEXT:  ".format(serie+1, nr_of_sets))
    #                 stop_time = int(time.time())
    #                 printer(timer =         0,
    #                         ex_reps =       "",
    #                         ex_name =       "  GOOD JOB",
    #                         next_ex_reps =  "TIME: " + Duration(start_time, stop_time),
    #                         next_ex_name =  "",
    #                         info="  YOU'VE JUST FINISHED " + workout.name + " :  ")
    #
    #             elif ex_nr == (nr_of_exercises-1):                          # last in set
    #                 printer(timer =         workout.GetTime(ex_nr, serie),
    #                         ex_reps =       workout.GetRepetitions(ex_nr, serie),
    #                         ex_name =       workout.GetExcerciseName(ex_nr, serie),
    #                         next_ex_reps =  "",
    #                         next_ex_name =  "long break",
    #                         info="  END OF SET {0}/{1} , NEXT:  ".format(serie+1, nr_of_sets))
    #                 printer(timer =         workout.break_set,
    #                         ex_reps =       " ",
    #                         ex_name =       "long break",
    #                         next_ex_reps =  workout.GetRepetitions(0, serie+1),
    #                         next_ex_name =  workout.GetExcerciseName(0, serie+1),
    #                         info="  SET {0}/{1} WILL START , NEXT:  ".format(serie+2, nr_of_sets))
    #
    #             else:                                                       # rest
    #                 printer(timer =         workout.GetTime(ex_nr, serie),
    #                         ex_reps =       workout.GetRepetitions(ex_nr, serie),
    #                         ex_name =       workout.GetExcerciseName(ex_nr, serie),
    #                         next_ex_reps =  "",
    #                         next_ex_name =  "break",
    #                         info="  SET {0}/{1}, EX({2}/{3}, NEXT:  ".format(serie+1, nr_of_sets, ex_nr, nr_of_exercises))
    #                 printer(timer =         workout.break_excercise,
    #                         ex_reps =       " ",
    #                         ex_name =       "break",
    #                         next_ex_reps =  workout.GetRepetitions(ex_nr+1, serie),
    #                         next_ex_name =  workout.GetExcerciseName(ex_nr+1, serie),
    #                         info="  SET {0}/{1} , NEXT:  ".format(serie+1, nr_of_sets))


def kbfunc():
    """ return Unicode code of pressed button
    return 0 if no button pressed
    """
    x = msvcrt.kbhit()
    if x:
        ret = ord(msvcrt.getch())
    else:
        ret = 0
    return ret

def KeyPress():
    key = kbfunc()
    if key in [13, 32]:  # enter, space
        current_workout = Workout.GetWorkout()
        doWorkout(current_workout)
    elif key == 27:  # escape
        exit()
    elif key == 224:  # special key prefix
        key_2 = kbfunc()
        # time.sleep(0.0)
        if key_2 == 77:  # right
            Workout.ChangeSelectionRight()
        if key_2 == 75:  # left
            Workout.ChangeSelectionLeft()
    return key

def MainMenu():

    def PrintSelectionList():
        selection_list = ["|__| "] * Workout.GetNumberOfWorkouts()
        selection_list[Workout.GetPosition()] = "|##| "
        selection = "".join(selection_list)
        print("\t < {0:<15} > \n".format(selection))

    while True:
        print()
        printASCII("  WORKOUT APP")
        print("\n \t {0:<15} - start workout, jump to break/excercise".format("SPACE"))
        print("\t {0:<15} - exit ".format("ESCAPE"))
        print("\t {0:<15} - pause \n".format("P _any other ;)"))
        PrintSelectionList()
        Workout.GetWorkout().printWorkout()
        # time.sleep(0.1)

        while True:
            if KeyPress() != 0:
                break

        os.system('cls')

MainMenu()
