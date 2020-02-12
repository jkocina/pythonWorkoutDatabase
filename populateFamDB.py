import sys
from exercise.dbUtil, exercise.writeToAllExercise, workout.writeToAllWorkouts, workout.dbUtil import *

dbChoices(sys.arg[0])

def dbChoices(arg):
    choicer = {
        1: callAllExerciseReset,
        2: callAllWorkoutReset,
        3: writeExercises,
        4: writeWorkouts
        }

    //TODO: if multiple arguments are passed, loop through each function
    func2Run = choicer.get(arg , lambda: "")

    func2Run()
