import fileinput

instructions = [[line[0], int(line.strip()[1:])] for line in fileinput.input()]

total_north = sum([instruction[-1] for instruction in instructions if instruction[0] == "N"]) - sum([instruction[-1] for instruction in instructions if instruction[0] == "S"]) 
total_east = sum([instruction[-1] for instruction in instructions if instruction[0] == "E"]) - sum([instruction[-1] for instruction in instructions if instruction[0] == "W"]) 

remaining_instructions = [instruction for instruction in instructions if instruction[0] not in ["N", "E", "S", "W"]]

heading = 90

def map_heading(heading):
  if heading < 0:
    return heading + 360
  if heading >= 360:
    return heading - 360
  return heading

def update_heading(instruction, current_heading):
  if instruction[0] == "L":
    new_heading = current_heading - instruction[1]
  else:
    new_heading = current_heading + instruction[1]
  return map_heading(new_heading)


for instruction in remaining_instructions:
  if instruction[0] in ["L", "R"]:
    heading = update_heading(instruction, heading)
  else:
    if heading == 0 or heading == 360:
      total_north += instruction[1]
    elif heading == 180:
      total_north -= instruction[1]
    elif heading == 90:
      total_east += instruction[1]
    elif heading == 270:
      total_east -= instruction[1]

print("answer to part 1: {}".format(str(abs(total_north) + abs(total_east))))

