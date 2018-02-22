import os


LAST_DIR = ""


def get_last_dir_from_path(full_path):
    global LAST_DIR
    if os.name == 'nt':
        return full_path.rsplit('\\', 1)[0]
    elif os.name == "posix":
        return full_path.rsplit('/', 1)[0]


def test():
    get_last_dir_from_path("/home/tobias/PycharmProjects/Workout-App/gui_version/workouts_csv/15_minutes_workout.csv")
    print(LAST_DIR)


if __name__ == "__main__": test()
