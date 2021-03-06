import pickle
import subprocess
import re
import os
import os.path
from os import listdir
import subprocess


# save basic python variables/data to a pickle file (.p)
def pickle_save(filename, data):
    with open(filename, 'wb') as fp:
        pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
    
    print("Saved data to file: " + filename)

# load a pickle file to python instance (.p)
def pickle_load(filename):
    data = {}
    with open(filename, 'rb') as fp:
        data = pickle.load(fp)
    
    print("Loaded File: ", data)

    return data

# get current pwd using python
def get_current_pwd():
    output2 = subprocess.check_output("pwd", shell=True)
    pwd_path = str(output2).replace("b'", "")
    pwd_path = pwd_path[:-3]
    pwd_path = pwd_path + "/"

    return pwd_path

# get a list of all the pickle file(s) paths
def find_all_pickle_files(path):
    path = str(path)

    command = "find $(pwd) -type f | grep '.pickle'"

    if(os.path.isfile(path) and path != "." and path != "./"):
        command = "find " + path + " -type f | grep '.pickle'"

    output = subprocess.check_output(command, shell=True)

    pickle_files = str(output).replace("b'", "")
    pickle_files = pickle_files[:-3]
    pickle_files = pickle_files.split("\\n")

    pwd_path = get_current_pwd()

    for i in range(len(pickle_files)):
        pickle_files[i] = pickle_files[i].replace(pwd_path, "./")

    return pickle_files

def move_to_saves():
    ideal_directory = "2d-l-system"

    ideal_directory.replace("/", "")

    current_pwd = get_current_pwd()

    aoi = current_pwd[-1*int(len(ideal_directory)+1):]

    aoi = aoi.replace("/", "")

    ls_output = subprocess.check_output("ls -a", shell=True)
    ls_output = ls_output.decode('ascii')

    there_pickle = ".pickle" in ls_output

    if(aoi == ideal_directory):
        if(os.path.isdir(current_pwd + "saves")):
            if(there_pickle):
                os.system("mv *.pickle ./saves")
                print("Moved Every .pickle File In Project To saves/")
                return True
            else:
                print("Failed To Move .pickle, there are no .pickle files to move")
        else:
            print("Failed To Move .pickle, there is no saves/ directory")
    else:
        print("Failed To Move .pickle, PATH not in set ideal_directory: " + str(ideal_directory))
    
    return False


