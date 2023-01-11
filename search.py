
import re
import os
def lookup(part_number):
    number = input("enter a item part number: ")
    path = "/media/sf_Z_DRIVE/Specs/"
    pattern = re.compile(r"(\d\d-\d\d\d\d\d-\d\d-\d\d\d\d\d)?", re.IGNORECASE)
    ab = 4801
    # Spot collects all the folder
    spot = os.listdir(path)
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
            print(complete)
            break


