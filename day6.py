f = open("day6_input.txt", "r")
groups = f.read().split("\n\n")

# part 1

num_yes = sum([len(list(set(group.replace("\n","")))) for group in groups])
print("answer to part 1: {}".format(str(num_yes)))


# part 2

split = [group.strip().split("\n") for group in groups]
sets = []

for i in split: 
    sets.append([set(x) for x  in i])

num_all_yes = sum([len(list(set.intersection(*s))) for s in sets])

print("answer to part 2: {}".format(str(num_all_yes)))

