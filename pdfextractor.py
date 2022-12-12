#The purpose of this is to grab the sub part numbers to the original spec.
import fitz
import pandas as pd
from functions import *

file_Path = "10-02973_revA.pdf"
new_File_Path = "/media/sf_Z_DRIVE/Specs/10-04801-10-04900/10-04801/current/10-04801_revA23.PDF"

doc = fitz.open(new_File_Path)

page1 = doc[0]
words = page1.get_text("words")
count = range(1,210)
ct = 0
array = []
for i in count:
    ct += 1
    if words[ct][4] in array:
        continue
    else:
        array.append(words[ct][4])
for i in array:
    file_Open(i)
#print(array)
    #file_Open(words[ct][4])
