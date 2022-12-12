import subprocess
import re
import os
from functions import *


path = "/media/sf_Z_DRIVE/Specs/"
rev = 1
model_number = input("Model Number: ").upper()
og_model = model_number
counter = 0
# file_type = input("Do you need the specsheet, 3d model or what? ")
file_ext = ".pdf"
model_Array = model_number.split()


#If model_number has several inputs we will iterate through them one at a time.
for i in model_Array:
    model_number = i
    #file_ext = extension(file_type.lower())
    classic_part = model_number.split("-")[0]
    if classic_part == "053":
        classic_base_path = path + "053-XXXX-553-XXXX/"
        classic_list = os.listdir(classic_base_path)
        for i in classic_list:
            classic = i.split()
            new_Path = classic_base_path + model_number + "/current/" + model_number + f"_revA{file_ext}"
            if model_number == classic[0] and len(classic) <= 1:
                if os.path.exists(new_Path):
                    openPath(new_Path)
                    break
                else:
                    while not os.path.exists(new_Path):
                        new_Path = classic_base_path + model_number + "/current/" + model_number + f"_revA{rev}{file_ext}"
                        if rev == 60:
                            last_Path = classic_base_path + model_number + "/current/"
                            openPath(last_Path)
                            break
                        if os.path.exists(new_Path):
                            openPath(new_Path)
                            break
                        rev += 1
            elif len(classic) >= 2 and model_number == classic[0]:
                ext_Path = classic_base_path + model_number + " " + classic[1] + "/" + "current/" + model_number + f"_revA{file_ext}"
                if os.path.exists(ext_Path):
                    openPath(ext_Path)
                else:
                    while not os.path.exists(ext_Path):
                        ext_Path = classic_base_path + model_number + " " + classic[1] + "/" + "current/" + model_number + f"_revA{rev}{file_ext}"
                        if rev == 60:
                            print("Could not find")
                            last_Path = classic_base_path + model_number + " " + classic[1] + "/current"
                            openPath(last_Path)
                            break
                        if os.path.exists(ext_Path):
                            openPath(ext_Path)
                            extensive_Lookup(ext_Path, model_number)
                        rev += 1
            counter += 1
    else:
        base_file = lookup(model_number)
        full_path = path + base_file + "/" + model_number + "/current/" + model_number + f"_revA{file_ext}"
        if os.path.exists(full_path):
            openPath(full_path)
            extensive_Lookup(full_path, og_model)
        else:
            noFilePathHandling(model_number, file_ext)
            #extensive_Lookup(full_path)
        open_web(model_number)
