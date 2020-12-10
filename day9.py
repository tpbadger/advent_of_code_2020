import fileinput

seq = [int(num.strip()) for num in fileinput.input()]

preamble_size = 25

def can_be_made(target, seq_slice):
    for num in seq_slice:
        complement = target-num
        if complement in seq_slice:
            return True
    return False

window_start = 0
window_end = preamble_size
for index in range(preamble_size, len(seq)):
   target = seq[index]
   seq_slice = seq[window_start: window_end]
   if not can_be_made(target, seq_slice):
       print("answer to part 1: {}".format(str(target)))
       break
   window_start += 1
   window_end += 1




