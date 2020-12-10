import fileinput
from collections import Counter

adapters = [int(adapter.strip()) for adapter in fileinput.input()]
adapters += [0, max(adapters) + 3]
adapters.sort()

diffs = list(Counter([j - i for i, j in zip(adapters[:-1], adapters[1:])]).values())

print("answer to part 1: {}".format(str(diffs[0] * diffs[1])))
