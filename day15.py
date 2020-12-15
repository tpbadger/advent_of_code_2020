nums = [18, 11, 9, 0 , 5, 1]

mem = {num: 1 for num in nums}

def find_prev_spoken(nums, num):
  return [ind + 1 for ind, val in enumerate(nums) if val == num]

while len(nums) < 2020:
  num = nums[-1]
  if num in mem.keys() and mem[num] == 1:
    add = 0
  else:
    prev_spoken = find_prev_spoken(nums, num)
    diff = prev_spoken[-1] - prev_spoken[-2]
    add = diff
  nums.append(add)
  if add in mem.keys():
    mem[add] += 1
  else:
    mem[add] = 1

print("answer to part 1: {}".format(str(nums[-1])))
