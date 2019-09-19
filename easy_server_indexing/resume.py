import os
from pathlib import Path

def resume_code(root_path,error_path):
    flag = False
    path_list =[]
    for root, dirs, files in os.walk(root_path):
        for name in files:
            if str(error_path) in os.path.join(root, name):
                #print(os.path.join(root, name))
                flag = True
            if flag == True:
                h = Path(os.path.join(root, name))
                path_list.append(h)

    return path_list


