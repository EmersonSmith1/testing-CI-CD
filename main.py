import os
import sys

if len(sys.argv) > 1:
    max_x = sys.argv[1]
else:
    max_x = input('What is the max x?')

#max_x = input('What is the max x?')
print(max_x)
#max_x = os.getenv('MAX_X')
print()
for x in range(0, int(max_x)):
    print(x)