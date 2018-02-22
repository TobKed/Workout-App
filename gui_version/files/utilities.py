import os
import pickle

LAST_DIR = ""


def get_dir_from_path(full_path):
    if full_path:
        if os.name == 'nt':
            return full_path.rsplit('\\', 1)[0]
        elif os.name == "posix":
            return full_path.rsplit('/', 1)[0]


def save_last_dir(path):
    global LAST_DIR
    LAST_DIR = path
    try:
        if path:
            with open("files/last_dir.pkl", "wb") as f:
                pickle.dump(get_dir_from_path(path), f)
                print("Last workout directory saved. Directory:", get_dir_from_path(path))
    except Exception as e:
        print("Error during saving last directory. Error:\n\t{}".format(e))


def get_last_dir():
    global LAST_DIR
    try:
        with open("files/last_dir.pkl", "rb") as f:
            LAST_DIR = pickle.load(f)
            print("Last workout directory retrieved. Directory:", LAST_DIR)
    except Exception as e:
        print("Error retrieving last directory from file. Error:\n\t{}".format(e))
