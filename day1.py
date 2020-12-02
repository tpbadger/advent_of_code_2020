def main():
    print("answer to part 1 is {}".format(str(pt1())))
    print("answer to part 2 is {}".format(str(pt2())))

def pt1():
    f = open("./day1_input.txt", "r")
    inpt = [int(x.strip()) for x in f.readlines()]
    num1, num2 = find_pair(2020, inpt)
    return num1 * num2

def pt2():
    f = open("./day1_input.txt", "r")
    inpt = [int(x.strip()) for x in f.readlines()]
    ans = find_triplet(2020, inpt)
    tot = 1
    for i in ans:
        tot *= i
    return tot

    
def find_triplet(target, numbers):
    numbers.sort()
    for i in range(0, len(numbers) - 2):
        left_mark = i + 1
        right_mark = len(numbers) - 1

        while left_mark < right_mark: 
            if numbers[i] + numbers[left_mark] + numbers[right_mark] == target:
                return [numbers[i], numbers[left_mark], numbers[right_mark]]
            elif numbers[i] + numbers[left_mark] + numbers[right_mark] < target:
                left_mark += 1 # too small so increment left marker
            else:
                right_mark -= 1

    return



def find_pair(target, numbers):
    for i, number in enumerate(numbers[:-1]):
        comp = target - number
        if comp in numbers[i+1:]:
            return (comp, number)

if __name__ == "__main__":
    main()



