import glob
import json
import os


def get_ordered_files(dir_name):
    # Get list of all files only in the given directory
    list_of_files = filter(os.path.isfile, glob.glob(dir_name + '/*'))

    # Sort list of files based on name
    list_of_files = sorted(list_of_files)

    return list_of_files

def get_next_tn(dir_name):
    current_path = dir_name +"/current.json"
    with open(current_path, 'r') as openfile:
        current_tn = json.load(openfile)

    tns = get_ordered_files(dir_name)

    tn_name = ""
    for i, tn in enumerate(tns):
        if tn == current_tn["current"]:
            tn_name = tns[(i+1)%len(tns)]
            break

    if tn_name == current_tn["current"]:
        # nothing changed
        return None
    elif tn_name == "":
        # old thumbnail was not found in dir
        tn_name = tns[0]
    
    current_tn["current"] = tn_name

    with open(current_path, "r") as outfile:
        outfile.write(json.dumps(current_tn))

    return tn_name