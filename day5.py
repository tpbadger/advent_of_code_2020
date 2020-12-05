import fileinput

def decode(low, high, low_char, high_char, string):
    nums = [num for num in range(low, high + 1)]
    for character in string:
        if character == low_char:
            nums = nums[:int(len(nums)/2)]
        else:
            nums = nums[int(len(nums)/2):]
    return nums[0]

max_seat_id = 0

seat_ids = [((8 * decode(0, 127, 'F', 'B', pass_id.strip()[:-3])) + decode(0, 7, 'L', 'R', pass_id.strip()[-3:])) for pass_id in fileinput.input()]

print("answer to part 1: {}".format(str(max(seat_ids))))

sorted_seat_ids = sorted(seat_ids)

missing_seat_ids = set(range(sorted_seat_ids[0], sorted_seat_ids[-1])) - set(sorted_seat_ids)

print("answer to part 2: {}".format(str(list(missing_seat_ids)[0])))

