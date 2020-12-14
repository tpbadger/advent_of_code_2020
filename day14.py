import fileinput

mem = {}
mask = ''
for line in fileinput.input():
  splt = line.strip().split(" ")
  if len(splt[-1]) == 36:
    mask = splt[-1]
  else:
    loc, val = (int(splt[0].split("[")[1].replace("]", "")), int(splt[-1]))
    bin_val = ['0' for _ in range(36 - len(bin(val).replace("0b","")))] + list(bin(val).replace("0b", ""))
    for idx, bit in enumerate(reversed(bin_val)):
      if mask[idx] == "1" and bin_val[idx] == "0":
        bin_val[idx] = "1"
      elif mask[idx] == "0" and bin_val[idx] == "1":
        bin_val[idx] = "0"
    mem[loc] = int(''.join(bin_val), 2)
    
print("answer to part 1: {}".format(str(sum(list(mem.values())))))
