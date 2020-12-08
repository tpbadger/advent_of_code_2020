import fileinput
import re

def get_input():
    return [line.strip() for line in fileinput.input()]


inpt = get_input()
bag_combs = [re.findall(r'\w+\s\w+(?=\s*bag[^/])', bag) for bag in inpt]

deps = ["shiny gold"]
ind = 0 
old_dep = None
new_dep = "shiny gold"

while old_dep != new_dep:
    for bag_comb in bag_combs:
        if deps[ind] in bag_comb[1:] and bag_comb[0] not in deps:
            deps.append(bag_comb[0])
    ind += 1
    old_dep = new_dep
    if ind <= len(deps) - 1:
        new_dep = deps[ind] 


print("answer to part 1: {}".format(str(len(deps[1:]))))
