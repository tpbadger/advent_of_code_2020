import fileinput
import re 

strings = []
string = ""



inpt = open("./day4_input.txt", "r")
strings = inpt.read().split("\n\n")

passports = []
for string in strings:
    passports.append([{key: value for key, value in re.findall(r'(\w+):([^\s]+)', string)}])

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid = 0
for passport in passports:
    if all(field in passport[0] for field in fields):
        valid += 1
print("answer to part 1: {}".format(str(valid)))


def check_valid(key, val):
    if key == "byr":
        return val.isnumeric() and len(val) == 4 and 1920 <= int(val) <= 2002 
    elif key == "iyr":
        return val.isnumeric() and len(val) == 4 and 2010 <= int(val) <= 2020
    elif key == "eyr":
        return val.isnumeric() and 2020 <= int(val) <= 2030
    elif key == "hgt":
        if val[-2:] == "cm":
            return  val[:-2].isnumeric() and 150 <= int(val[:-2]) <= 193
        elif val[-2:] == "in":
            return val[:-2].isnumeric() and 59 <= int(val[:-2]) <= 76
        return False 
    elif key == "hcl":
        return re.match(r'#[a-f0-9]+$', val) is not None and len(val) == 7 
    elif key == "ecl":
        return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif key == "pid":
        return val.isnumeric() and len(val) == 9
    elif key == "cid":
        return True
    else:
        return False

num_invalid = 0
num_passports = len(passports)

for passport in passports:
    for key, value in passport[0].items():
        if not all(field in passport[0] for field in fields) or not check_valid(key, value):
            num_invalid += 1
            break

print("answer to part 2: {}".format(str(num_passports - num_invalid)))


