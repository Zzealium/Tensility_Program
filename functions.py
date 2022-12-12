import subprocess
import re
import os
import fitz
import pandas as pd
import webbrowser


def get_Path(model_number):
    path = "/media/sf_Z_DRIVE/Specs/"
    rev = 1
    og_model = model_number.upper()
    counter = 0
    file_ext = ".PDF"
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
                        # openPath(new_Path) # This was used before GUI. Same with similar functions below.
                        return new_Path
                        break
                    else:
                        while not os.path.exists(new_Path):
                            new_Path = classic_base_path + model_number + "/current/" + model_number + f"_revA{rev}{file_ext}"
                            if rev == 60:
                                last_Path = classic_base_path + model_number + "/current/"
                                # openPath(last_Path)
                                return last_Path
                                break
                            if os.path.exists(new_Path):
                                return new_Path
                                # openPath(new_Path)
                                break
                            rev += 1
                elif len(classic) >= 2 and model_number == classic[0]:
                    ext_Path = classic_base_path + model_number + " " + classic[
                        1] + "/" + "current/" + model_number + f"_revA{file_ext}"
                    if os.path.exists(ext_Path):
                        # openPath(ext_Path)
                        return ext_Path
                    else:
                        while not os.path.exists(ext_Path):
                            ext_Path = classic_base_path + model_number + " " + classic[
                                1] + "/" + "current/" + model_number + f"_revA{rev}{file_ext}"
                            if rev == 60:
                                last_Path = classic_base_path + model_number + " " + classic[1] + "/current"
                                # openPath(last_Path)
                                create_logs(last_Path)
                                return last_Path
                                break
                            if os.path.exists(ext_Path):
                                return ext_Path
                                # openPath(ext_Path)
                                # extensive_Lookup(ext_Path, model_number)
                            rev += 1
                counter += 1
        elif pushpull == '51':
            base_file = lookup(model_number)
            if os.path.exists(path + base_file):
                full_path = path + base_file + '/' + model_number
                if os.path.exists(full_path):
                    full_path = full_path + '/current/' + model_number + '_revA.pdf'
                    return full_path
                else:
                    full_pathM = full_path + '.M'
                    if os.path.exists(full_pathM):
                        full_pathM = full_pathM
                        openPath(full_pathM + '/current/' + model_number + '.M_revA.pdf')
                        full_pathD = full_path + '.52'
                        if os.path.exists(full_pathD):
                            openPath(full_pathD + '/current/' + model_number + '.52_revA.pdf')
                        else:
                            full_pathD = full_pathD + '.42'
                            openPath(full_pathD + '/current/' + model_number + '.42_revA.pdf')


        else:
            base_file = lookup(model_number)
            full_path = path + base_file + "/" + model_number + "/current/" + model_number + f"_revA{file_ext}"
            if os.path.exists(full_path):
                return full_path
                # openPath(full_path)
                # extensive_Lookup(full_path, og_model)
            else:
                print("Failed")
                test = noFilePathHandling(model_number, file_ext)
                return test
                # extensive_Lookup(full_path)
            # open_web(model_number)


# Opens given filepath
def openPath(path):
    subprocess.call(["xdg-open", path])


def lookup(part_number):
    count = 0
    ext_index = [
        [range(1, 101), "00001-00100"],
        [range(101, 201), "00101-00200"],
        [range(201, 301), "00201-00300"],
        [range(301, 401), "00301-00400"],
        [range(401, 501), "00401-00500"],
        [range(501, 601), "00501-00600"],
        [range(601, 701), "00601-00700"],
        [range(701, 801), "00701-00800"],
        [range(801, 901), "00801-00900"],
        [range(901, 1001), "00901-01000"],
        [range(1001, 1101), "01001-01100"],  # 10
        [range(1101, 1201), "01101-01200"],
        [range(1201, 1301), "01201-01300"],
        [range(1301, 1401), "01301-01400"],
        [range(1401, 1501), "01401-01500"],
        [range(1501, 1601), "01501-01600"],
        [range(1601, 1701), "01601-01700"],
        [range(1701, 1801), "01701-01800"],
        [range(1801, 1901), "01801-01900"],
        [range(1901, 2001), "01901-02000"],
        [range(2001, 2101), "02001-02100"],  # 20
        [range(2101, 2201), "02101-02200"],
        [range(2201, 2301), "02201-02300"],
        [range(2301, 2401), "02301-02400"],
        [range(2401, 2501), "02401-02500"],
        [range(2501, 2601), "02501-02600"],
        [range(2601, 2701), "02601-02700"],
        [range(2701, 2801), "02701-02800"],
        [range(2801, 2901), "02801-02900"],
        [range(2901, 3001), "02901-03000"],
        [range(3001, 3101), "03001-03100"],  # 30
        [range(3101, 3201), "03101-03200"],
        [range(3201, 3301), "03201-03300"],
        [range(3301, 3401), "03301-03400"],
        [range(3401, 3501), "03401-03500"],
        [range(3501, 3601), "03501-03600"],
        [range(3601, 3701), "03601-03700"],
        [range(3701, 3801), "03701-03800"],
        [range(3801, 3901), "03801-03900"],
        [range(3901, 4001), "03901-04000"],
        [range(4001, 4101), "04001-04100"],  # 40
        [range(4101, 4201), "04101-04200"],
        [range(4201, 4301), "04201-04300"],
        [range(4301, 4401), "04301-04400"],
        [range(4401, 4501), "04401-04500"],
        [range(4501, 4601), "04501-04600"],
        [range(4601, 4701), "04601-04700"],
        [range(4701, 4801), "04701-04800"],
        [range(4801, 4901), "04801-04900"],
        [range(4901, 5001), "04901-05000"],
        [range(5001, 5101), "05001-05100"],  # 50
        [range(5101, 5201), "05101-05200"],
        [range(5201, 5301), "05201-05300"],
        [range(5301, 5401), "05301-05400"],
        [range(5401, 5501), "05401-05500"],
        [range(5501, 5601), "05501-05600"],
        [range(5601, 5701), "05601-05700"],
        [range(5701, 5801), "05701-05800"],
        [range(5801, 5901), "05801-05900"],
        [range(5901, 6001), "05901-06000"],
        [range(6001, 6101), "06001-06100"],  # 60
        [range(6101, 6201), "06101-06200"],
        [range(6201, 6301), "06201-06300"],
        [range(6301, 6401), "06301-06400"],
        [range(6401, 6501), "06401-06500"],
        [range(6501, 6601), "06501-06600"],
        [range(6601, 6701), "06601-06700"],
        [range(6701, 6801), "06701-06800"],
        [range(6801, 6901), "06801-06900"],
        [range(6901, 7001), "06901-07000"],
        [range(7001, 7101), "07001-07100"],  # 70
        [range(7101, 7201), "07101-07200"],
        [range(7201, 7301), "07201-07300"],
        [range(7301, 7401), "07301-07400"],
        [range(7401, 7501), "07401-07500"],
        [range(7501, 7601), "07501-07600"],
        [range(7601, 7701), "07601-07700"],
        [range(7701, 7801), "07701-07800"],
        [range(7801, 7901), "07801-07900"],
        [range(7901, 8001), "07901-08000"],
        [range(8001, 8101), "08001-08100"],  # 80
        [range(8101, 8201), "08101-08200"],
        [range(8201, 8301), "08201-08300"],
        [range(8301, 8401), "08301-08400"],
        [range(8401, 8501), "08401-08500"],
        [range(8501, 8601), "08501-08600"],
        [range(8601, 8701), "08601-08700"],
        [range(8701, 8801), "08701-08800"],
        [range(8801, 8901), "08801-08900"],
        [range(8901, 9001), "08901-09000"],
        [range(9001, 9101), "09001-09100"],  # 90
        [range(9101, 9201), "09101-09200"],
        [range(9201, 9301), "09201-09300"],
        [range(9301, 9401), "09301-09400"],
        [range(9401, 9501), "09401-09500"],
        [range(9501, 9601), "09501-09600"],
        [range(9601, 9701), "09601-09700"],
        [range(9701, 9801), "09701-09800"],
        [range(9801, 9901), "09801-09900"],
        [range(9901, 10001), "09901-10000"],
        [range(10001, 10101), "10001-10100"]  # 100

    ]
    while True:
        try:
            p = ext_index[count]
            partsplit = part_number.split("-")[1]
            catnumber = part_number.split("-")[0]
            if catnumber == "053":
                break
            ar = list(p[0])
            if int(partsplit) not in ar:
                count += 1
            if int(partsplit) in ar:
                split_ext = ext_index[count][1].split("-")
                first = split_ext[0]
                second = split_ext[1]
                complete = catnumber + "-" + first + "-" + catnumber + "-" + second
                return complete
                break
        except:
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
        full_path = path + base_file + "/" + model_number + "/current/" + model_number + f"_revA{file_ext}"
        if os.path.exists(full_path):
            openPath(full_path)
        else:
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
def extensive_Lookup(pdf_file_path, og_model):
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
    while ('' in array):
        array.remove('')
    for i in array:
        file_Open(i)


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


# Uses the file path to look for picture.
def open_picture(file_path, model_number):
    file_path = file_path + "/pictures/web/" + model_number + ".JPG"
    if os.path.exists(file_path):
        openPath(file_path)
    else:
        file_path = file_path + "/pictures/web/" + model_number + ".jpg"
        openPath(file_path)


def create_logs(error):
    log_path = "/home/tensility/Desktop/Scripts/Lookup/logs/logs.txt"
    if not os.path.exists(log_path):
        with open(log_path, 'x') as f:
            f.write(f"Error {error}")
    elif os.path.exists(log_path):
        logs = open(log_path, 'a')
        logs.write(f"Error {error} \n")
