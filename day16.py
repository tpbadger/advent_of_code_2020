f = open("day16_input.txt", "r")
parts = f.read().split("\n\n")

fields = [(field.split(" ")[-3], field.split(" ")[-1]) for field in parts[0].split("\n")]
tickets = [x.split(",") for x in parts[-1].split("\n")[1:]]

def gen_range(chars):
  spl = chars.split("-")
  return list(range(int(spl[0]), int(spl[-1]) + 1))

valid_nums = []
for field in fields:
  v1, v2 = field
  valid_nums += gen_range(v1) + gen_range(v2)

inv_nums = []
for ticket in tickets:
  for num in ticket:
    if int(num) not in list(set(valid_nums)):
      inv_nums.append(int(num))

print("answer to part 1: {}".format(str(sum(inv_nums))))
       
