import fileinput

def convert_instruction_count(instruction_count):
    if instruction_count[0] == '-':
        return -int(instruction_count[1:])
    return int(instruction_count[1:])

def get_instructions():
    return [[instruction.strip().split(" ")[0], convert_instruction_count(instruction.strip().split(" ")[1]), False] 
           for instruction in fileinput.input()]

instructions_mut = get_instructions() 

inf = False
acc = 0
line = 0

def update_line(current_line):
    if instructions_mut[current_line][0] == "acc":
        return (instructions_mut[line][1], 1)
    if instructions_mut[line][0] == "jmp":
        return (0, instructions_mut[line][1])
    else:
        return(0, 1)

while not inf:
    if instructions_mut[line][-1]:
        inf = True
    else:
        instructions_mut[line][-1] = True
        acc_plus, line_plus = update_line(line)
        acc += acc_plus
        line += line_plus

print("answer to part 1: {}".format(str(acc)))
