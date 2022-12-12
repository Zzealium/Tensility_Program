
import re



path = "/media/sf_Z_DRIVE/Specs/"
pattern = re.compile(r"(\d\d-\d\d\d\d\d-\d\d-\d\d\d\d\d)?")

one = "51-00019"
two = "51-00019.52"
three = "51-00019.M"
expand = "51-00001-50-00100"


if one in expand:
    print("True")
else:
    print("False")
