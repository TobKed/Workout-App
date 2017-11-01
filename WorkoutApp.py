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
                exit()
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
            if  x <= 3:
                winsound.Beep(2500, 500)
                time.sleep(0.5)
            else:
                time.sleep(1)
            os.system('cls')
            key_pressed = kbfunc()
            if key_pressed == 32:   #space
                break
            if key_pressed== 27:   #escape
                exit()
            if key_pressed == 112:   #P
                pause = True
            while pause == True:
                key_pressed = kbfunc()
                # if key_pressed == 112:  # P
                if key_pressed != 0:  # P
                    pause = False
                if key_pressed == 27:  # escape
                    exit()
                print("\n\n")
                printASCII("   PAUSE")
                time.sleep(0.5)
                os.system('cls')

def Duration(start, end):
    duration = end - start
    minutes = str((duration % 3600) // 60).zfill(2)
    seconds = str(duration % 60).zfill(2)
    return "  " + minutes + ":" + seconds

def doWorkout(workout):
    nr_of_exercises = workout.nrOfExs()
    timeStart = int(time.time())
    printer(timer=workout.break_excercise,
            ex_reps=" ",
            ex_name="get ready",
            next_ex_reps=workout.exReps(0, 0),
            next_ex_name=workout.exName(0, 0) )
    for serie in range(workout.nr_of_sets+1):
        for ex_nr in range(nr_of_exercises):
            if ex_nr == (nr_of_exercises-1) and serie ==(workout.nr_of_sets):    # lest, finish fater that
                printer(timer =         workout.exTime(ex_nr, serie),
                        ex_reps =       workout.exReps(ex_nr, serie),
                        ex_name =       workout.exName(ex_nr, serie),
                        next_ex_reps =  "",
                        next_ex_name =  "the end",
                        info="  END OF SET NR:{0}, NEXT:  ".format(serie+1))
                timeStop = int(time.time())
                printer(timer =         0,
                        ex_reps =       "",
                        ex_name =       "  GOOD JOB",
                        next_ex_reps =  "TIME: " + Duration(timeStart, timeStop),
                        next_ex_name =  "",
                        info="  YOUR WORKOUT TIME:  ")

            elif ex_nr == (nr_of_exercises-1):                          # last in set
                printer(timer =         workout.exTime(ex_nr, serie),
                        ex_reps =       workout.exReps(ex_nr, serie),
                        ex_name =       workout.exName(ex_nr, serie),
                        next_ex_reps =  "",
                        next_ex_name =  "long break",
                        info="  END OF SET NR:{0}, NEXT:  ".format(serie+1))
                printer(timer =         workout.break_set,
                        ex_reps =       " ",
                        ex_name =       "long break",
                        next_ex_reps =  workout.exReps(0, serie+1),
                        next_ex_name =  workout.exName(0, serie+1),
                        info="  SET NR:{0} WILL START, NEXT:  ".format(serie+2))

            else:                                                       # rest
                printer(timer =         workout.exTime(ex_nr, serie),
                        ex_reps =       workout.exReps(ex_nr, serie),
                        ex_name =       workout.exName(ex_nr, serie),
                        next_ex_reps =  "",
                        next_ex_name =  "break",
                        info="  SET NR:{0}, NEXT:  ".format(serie+1))
                printer(timer =         workout.break_excercise,
                        ex_reps =       " ",
                        ex_name =       "break",
                        next_ex_reps =  workout.exReps(ex_nr+1, serie),
                        next_ex_name =  workout.exName(ex_nr+1, serie),
                        info="  SET NR:{0}, NEXT:  ".format(serie+1))

def kbfunc():
    x = msvcrt.kbhit()
    if x:
        ret = ord(msvcrt.getch())
    else:
        ret = 0
    return ret

while True:
    print("\n")
    printASCII("  WORKOUT APP")
    print("\n \t {0:<15} - start workout, jump to break/excercise".format("SPACE"))
    print("\t {0:<15} - pause".format("P"))
    print("\t {0:<15} - exit \n".format("ESCAPE"))
    oneFiveMin.printWorkout()
    key = kbfunc()
    if key in [13, 32]:
        doWorkout(oneFiveMin)
    elif key == 27:
        exit()
    time.sleep(1)
    os.system('cls')
