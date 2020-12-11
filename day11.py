import fileinput
import numpy as np
seating = np.array([list(line.strip()) for line in fileinput.input()])
seating = np.pad(seating, 1, mode='empty')


height, width = seating.shape

def change_state(c1, c2, c3, c4, c5, c6, c7, c8, c9):
  adjacent = [s for s in [c1, c2, c3, c4, c6, c7, c8, c9] if s == "#"]
  if c5 == "L" and "#" not in [c1, c2, c3, c4, c6, c7, c8, c9]:
    return "#"
  if c5 == "#" and len(adjacent) >= 4:
    return "L"
  return c5

updates = np.empty_like(seating)

while True: 
  for i in range(1, height - 1):
    for j in range(1, width - 1):
      c1 = seating[i-1][j-1] 
      c2 = seating[i-1][j]
      c3 = seating[i-1][j+1]
      c4 = seating[i][j-1]
      c5 = seating[i][j]
      c6 = seating[i][j+1]
      c7 = seating[i+1][j-1]
      c8 = seating[i+1][j]
      c9 = seating[i+1][j+1]
      updates[i][j] = change_state(c1, c2, c3, c4, c5, c6, c7, c8, c9)
  if np.array_equal(seating[:height-1][:width-1], updates[:height-1][:width-1]):
    break
  else:
    seating[:height-1][:width-1] = updates[:height-1][:width-1]


print("answer to part 1 is: {}".format(str(np.sum(seating == "#"))))
