import numpy as np
import math

def get_input():
    f = open("./day3_input.txt", "r")
    data = []
    for line in f.readlines():
        data.append([i for i in line.strip().replace("'", "")])
    return data


def main():
    print("answer to part 1: {}".format(str(part1())))
    print("answer to part 2: {}".format(str(part2())))

def part1():
    arr = generate_arr(3)
    return calc_num_trees([1,3], arr)


def part2():
    slopes = [[1,1], [1,3], [1,5], [1,7], [2,1]]
    trees = []
    for slope in slopes:
        arr = generate_arr(slope[1])
        trees.append(calc_num_trees(slope, arr))

    prod = 1
    for num in trees:
        prod *= num

    return prod

def calc_num_trees(slope, arr):
    row = 0
    col = 0
    row_max, col_max = arr.shape
    num_trees = 0
    while row < row_max and col < col_max:
        if arr[row][col] == "#":
            num_trees += 1
        row += slope[0]
        col += slope[1]
    return num_trees

def generate_arr(num_right):
    inpt = get_input()
    block = np.array(inpt)
    num_blocks = math.ceil(float(block.shape[0] / float(block.shape[1]/num_right)))
    return np.tile(block, num_blocks)
    

if __name__ == "__main__":
    main()
