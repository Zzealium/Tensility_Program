import re
import fitz
from functions import *

# example = "this is an example of txt that will have#$#$ a part 10-04952 number or two. )&*also 30-02701 special 10-04801 character s$$%$%T )(()AS10-04801(D A)(SDIk 10-01060 ))"
# test = " 10-04801 "

doc = fitz.open("053-0109R_revA2.pdf")
page = doc[0]
words = page.get_text("words")
ct = -1

count = range(1,len(words))


array = []
og_model = "10-02880"

for i in count:
    ct += 1
    if words[ct][4] in array:
        continue
    else:
        array.append(words[ct][4])


###Working Code
if og_model in array:
    print(array)
    array.remove(og_model)
    print(array)
array = ''.join(array)

list = use_regex(array)

while('' in list):
    list.remove('')
print(f"This is the list of part numbers {list}")
