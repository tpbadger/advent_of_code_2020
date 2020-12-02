def parse_input():
    f = open("./day2_input.txt", "r")
    inpt = [x.strip() for x in f.readlines()]
    return inpt 


def part1():
    inpt = parse_input()
    parsed = [i.replace(":", "").replace("-", " ").split(" ") for i in inpt]
    total_valid = 0
    for i in parsed:
        cnt = i[3].count(i[2])
        if int(i[0]) <= cnt <= int(i[1]):
            total_valid += 1
    return total_valid

def part2():
    inpt = parse_input()
    parsed = [i.replace(":", "").replace("-", " ").split(" ") for i in inpt]
    total_valid = 0
    for i in parsed:
        if i[3][int(i[0]) - 1] == i[2] and i[3][int(i[1]) - 1] != i[2]:
            total_valid += 1

        elif i[3][int(i[1]) - 1] == i[2] and i[3][int(i[0]) - 1] != i[2]:
            total_valid += 1 

    return total_valid
        


def main():
    print("Answer for part 1: {}".format(str(part1())))
    print("Answer for part 2: {}".format(str(part2())))

if __name__ == "__main__":
    main()
