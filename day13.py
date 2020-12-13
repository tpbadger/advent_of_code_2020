import fileinput
from operator import itemgetter

notes = [line.strip() for line in fileinput.input()]

arrival = int(notes[0])
busses = [int(x) for x in notes[1].split(",") if x.isnumeric()]

bus_id, wait = min(enumerate([bus_id - (arrival%bus_id) for bus_id in busses]), key=itemgetter(1))

print("answer to part 1: {}".format(str(wait * busses[bus_id])))

