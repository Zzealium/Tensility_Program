import subprocess
import re
import os
import fitz
import pandas as pd
import webbrowser
import shutil
import datetime


def get_Path(model_number):
    path = "/media/sf_Z_DRIVE/Specs/"
    rev = 1
    og_model = model_number.upper()
    counter = 0
    file_ext = ".pdf"
    model_number = model_number.upper()
    model_Array = model_number.split()

    # If model_number has several inputs we will iterate through them one at a time.
    for i in model_Array:
        model_number = i
        # file_ext = extension(file_type.lower())
        classic_part = model_number.split("-")[0]
        pushpull = model_number.split('-')[0]

        if classic_part == "053":
            classic_base_path = path + "053-XXXX-553-XXXX/"
            classic_list = os.listdir(classic_base_path)
            for i in classic_list:
                classic = i.split()
                new_Path = classic_base_path + model_number + "/current/" + model_number + f"_revA{file_ext}"
                if model_number == classic[0] and len(classic) <= 1:
                    if os.path.exists(new_Path):
                        return new_Path
                        break
                    else:
                        while not os.path.exists(new_Path):
                            new_Path = classic_base_path + model_number + "/current/" + model_number + f"_revA{rev}{file_ext}"
                            if rev == 60:
                                last_Path = classic_base_path + model_number + "/current/"
                                return last_Path
                                break
                            if os.path.exists(new_Path):
                                return new_Path
                                break
                            rev += 1
                elif len(classic) >= 2 and model_number == classic[0]:
                    ext_Path = classic_base_path + model_number + " " + classic[
                        1] + "/" + "current/" + model_number + f"_revA{file_ext}"
                    if os.path.exists(ext_Path):
                        return ext_Path
                    else:
                        while not os.path.exists(ext_Path):
                            ext_Path = classic_base_path + model_number + " " + classic[
                                1] + "/" + "current/" + model_number + f"_revA{rev}{file_ext}"
                            if rev == 60:
                                last_Path = classic_base_path + model_number + " " + classic[1] + "/current"
                                create_logs(last_Path)
                                return last_Path
                                break
                            if os.path.exists(ext_Path):
                                return ext_Path
                            rev += 1
                counter += 1
        elif pushpull == '51':
            # 51's sometimes have nothing at the end. So split breaks the code.
            # If the model number has nothing at the end it fails and moved to the
            # except and handles it.
            try:
                strip = model_number.split('.')
                aft = strip[1]
                base_file = lookup(strip[0])
                print(base_file) # = 51-00001 - 51-00100
                print(aft) # = M or 42 or 51
                fullpath = path + base_file + "/" + model_number +"/current/" + model_number + "_revA.pdf"
                if os.path.exists(fullpath):
                    return fullpath
                else:
                    count = 1
                    while not os.path.exists(fullpath):
                        fullpath = path + base_file + "/" + model_number +"/current/" + model_number + f"_revA{str(count)}.pdf"
                        if os.path.exists(fullpath):
                            return fullpath
                            break
                        elif count == 60:
                            break
                        count += 1
                        print(fullpath)
            except IndexError:
                base_file = lookup(model_number)
                fullpath = path + base_file + "/" + model_number + "/current/" + model_number + "_revA.pdf"
                print(fullpath)
                if os.path.exists(fullpath):
                    return fullpath
                else:
                    count = 1
                    while not os.path.exists(fullpath):
                        fullpath = path + base_file + "/" + model_number + "/current/" + model_number + f"_revA{str(count)}.pdf"
                        if os.path.exists(fullpath):
                            return fullpath
                            break
                        elif count == 60:
                            break
                        count += 1
                        print(fullpath)

        else:
            base_file = lookup(model_number)
            full_path = path + base_file + "/" + model_number + "/current/" + model_number + f"_revA.PDF"
            if os.path.exists(full_path):
                return full_path

            else:
                test = noFilePathHandling(model_number, file_ext)
                return test

def lookup(number):
    path1 = "/media/sf_Z_DRIVE/Specs/"
    pattern = re.compile(r"(\d\d-\d\d\d\d\d-\d\d-\d\d\d\d\d)?", re.IGNORECASE)
    # Spot collects all the folder
    spot = os.listdir(path1)
    #This looks for the pattern above.
    hope = pattern.findall(str(spot))
    # Cleans the list of results form Regex
    while '' in hope:
        hope.remove('')
    # Tries to match the input with a range.
    for m in hope:
        numbersplit = number.split("-")
        complete = m
        a = m.split("-")
        val = range(int(a[1]), int(a[3]))
        if int(numbersplit[1]) in val:
            # returns folder name ie = 10-02301-10-2400
            return complete
            break


# Input to check if user is looking for spec or model.
# This is not being used.
def extension(ext):
    spec_answers = [
        "spec",
        "specsheet",
        "",
        "specs",
        "pdf",
        "specs"
    ]
    model_answers = [
        "model",
        "3d",
        "3d model",
        "3dmodel",
        "step"
    ]
    if ext in spec_answers:
        return ".pdf"
    elif ext in model_answers:
        return ".STEP"


def noFilePathHandling(model_number, file_ext):
    rev_counter = 1
    path = "/media/sf_Z_DRIVE/Specs/"
    base_file = lookup(model_number)
    full_path = path + base_file + "/" + model_number + "/current/" + model_number + f"_revA{file_ext}"
    half_path = path + base_file + "/" + model_number
    quater_path = path + base_file
    while not os.path.exists(full_path):
        full_path = path + base_file + "/" + model_number + "/current/" + model_number + f"_revA{str(rev_counter)}{file_ext}"
        if rev_counter == 60:
            last_Path = path + base_file + "/" + model_number + "/current"
            if os.path.exists(last_Path):
                # openPath(last_Path)
                create_logs(last_Path)
                return last_Path
                break
            elif os.path.exists(half_path):
                # openPath(half_path)
                create_logs(half_path)
                return half_path
                break
            elif os.path.exists(quater_path):
                # openPath(quater_path)
                create_logs(quater_path)
                return quater_path
                break
            else:
                break
        if os.path.exists(full_path):
            return full_path
            # openPath(full_path)
            # extensive_Lookup(full_path, model_number)
            break
        rev_counter += 1


# looks for spec on given model number.
# This function also has a rev counter.
# If it can't find a file path it starts adding 1 to the rev.
# If it can't find the spec after 60 tried it will open the previous folder.
# It will do this until it has a valid file path.
def file_Open(model_number):
    file_ext = ".PDF"
    path = "/media/sf_Z_DRIVE/Specs/"
    base_file = lookup(model_number)
    try:
        full_path = path + base_file + "/" + model_number + "/current/" + model_number + f"_revA.PDF"
        if os.path.exists(full_path):
            openPath(full_path)
        else:
            rev_counter = 1
            path = "/media/sf_Z_DRIVE/Specs/"
            base_file = lookup(model_number)
            full_path = path + base_file + "/" + model_number + "/current/" + model_number + f"_revA.PDF"
            half_path = path + base_file + "/" + model_number
            quater_path = path + base_file
            while not os.path.exists(full_path):
                full_path = path + base_file + "/" + model_number + "/current/" + model_number + f"_revA{str(rev_counter)}.PDF"
                if rev_counter == 60:
                    last_Path = path + base_file + "/" + model_number + "/current"
                    if os.path.exists(last_Path):
                        create_logs(last_Path)
                        openPath(last_Path)
                        break
                    elif os.path.exists(half_path):
                        create_logs(half_path)
                        openPath(half_path)
                        break
                    elif os.path.exists(quater_path):
                        create_logs(quater_path)
                        openPath(quater_path)
                        break
                    else:
                        break
                if os.path.exists(full_path):
                    openPath(full_path)
                    break
                rev_counter += 1
    except:
        1 == 1


# Reads part number pdf and finds sub part numbers. Once found it opens pdfs on those sub parts.
def extensive_Lookup(pdf_file_path, og_model, qa=False):
    openPath(pdf_file_path)
    pattern = re.compile(r"(\d\d-\d\d\d\d\d)?", re.IGNORECASE)
    doc = fitz.open(pdf_file_path)
    page = doc[0]
    words = page.get_text("words")
    count = range(1, len(words))
    array = []
    ct = 0
    for i in count:
        ct += 1
        if words[ct][4] in array:
            continue
        else:
            array.append(words[ct][4])
    if og_model in array:
        array.remove(og_model)
    array = ''.join(array)
    array = pattern.findall(array)
    while '' in array:
        array.remove('')
    array = list(set(array))
    for i in array:
        if qa:
            continue
        file_Open(i)
    if qa:
        return separate_array(array)

# Separates the list of parts into their categories
# The == 50 needs to be worked on. we have 54, 55, and so on for cons.
def separate_array(array):
    print(array)
    array = list(set(array))
    count = 0
    con = []
    mold = []
    wire = []
    for i in array:
        cat = i.split('-')
        print(cat)
        if cat[0] == '30':
            wire.append(i)
        elif cat[0] == '50':
            con.append(i)
        elif cat[0] == '24':
            mold.append(i)
        count += 1
    print(f"This is wire {wire}")
    return con, mold, wire

# Simple regex for locating part numbers.
def use_regex(input_text):
    pattern = re.compile(r"(\d\d-\d\d\d\d\d)?", re.IGNORECASE)
    return pattern.findall(input_text)


# Determines what category the part number belongs to.
def open_web(model_number):
    # Splits the part number to see first two digits for category.
    cat = model_number.split("-")[0]
    # Different cat numbers lead to cable-assemblies.
    cA = ["10", "12", "", "053"]
    # Different cat numbers lead to connectors.
    con = ["50", "55", "56", "60"]
    # 51 will lead to push-pull-connectors
    ppc = ["51"]
    if cat in cA:
        url = f"https://tensility.com/cable-assemblies/{model_number.lower()}"
        webbrowser.open(url)
    elif cat == "11":
        url = f"https://tensility.com/ac-power-cords/{model_number}"
        webbrowser.open(url)
    elif cat == "16":
        url = f"https://tensility.com/power-supplies/{model_number}"
        webbrowser.open(url)
    elif cat == "30" or cat == "31":
        url = f"https://tensility.com/wire/{model_number}"
        webbrowser.open(url)
    elif cat in con:
        url = f"https://tensility.com/connectors/{model_number}"
        webbrowser.open(url)
    elif cat in ppc:
        split = model_number.split(".")
        split = ("-".join(split))
        url = f"https://tensility.com/connectors/push-pull-connectors/{split}"
        print(url)
        webbrowser.open(url)


# Uses the file path to look for picture.
def open_picture(file_path, model_number):
    #file_path = file_path + "/pictures/web/" + model_number + ".JPG"
    if model_number.split('-')[0] == '12':
        led_file_path = file_path + "/pictures/web/" + model_number + "_ON.JPG"
        openPath(led_file_path)
    elif os.path.exists(file_path):
        file_path = file_path + "/pictures/web/" + model_number + ".JPG"
        openPath(file_path)
    else:
        file_path = file_path + "/pictures/web/" + model_number + ".jpg"
        openPath(file_path)


def create_logs(error_message):
    log_path = "/home/tensility/Desktop/Scripts/Lookup/logs/logs.txt"
    if not os.path.exists(log_path):
        with open(log_path, 'x') as f:
            f.write(f"{error_message}")
    elif os.path.exists(log_path):
        logs = open(log_path, 'a')
        logs.write(f"{error_message} \n")

# Opens given filepath
def openPath(path):
    subprocess.call(["xdg-open", path])

# WIP
def version_control(version):
    #Check current version compare to master version on server. If old version update files.
    main_version_path = "/home/tensility/Documents/Lookup/version"
    main_path = "/home/tensility/Documents/Lookup"
    main_version = float(open(main_version_path, "r").read())
    version_path = "version"
    version_file = open(version_path, 'r')
    version_number = float(version_file.read())
    print(float(version_number))
    if main_version > version_number:
        print("We need to update the program. Please wait...")
        new_files = os.listdir(main_path)
        print(new_files)
        shutil.copytree(main_path, old_path, dirs_exist_ok=True)


def classic_search(model_number):
    path = "/media/sf_Z_DRIVE/Specs/"
    classic_base_path = path + "053-XXXX-553-XXXX/"
    classic_list = os.listdir(classic_base_path)
    print(model_number)
    for i in classic_list:
        classic_split = i.split()
        print(classic_split[0])
        if classic_split[0] == model_number.upper():
            ending = " ".join(classic_split)
            print(classic_base_path + ending)
            return classic_base_path + ending
            break