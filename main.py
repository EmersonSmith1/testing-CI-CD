import os
import sys

if len(sys.argv) > 1:
    max_x = sys.argv[1]
else:
    max_x = input('What is the max x?')

if len(sys.argv) > 1:
    max_y = sys.argv[1]
else:
    max_y = input('What is the max y?')

#max_y = input('max y')
#print(max_y)

#max_x = input('What is the max x?')
print(max_x)
#max_x = os.getenv('MAX_X')
print()
for x in range(0, int(max_x)):
    print(x)