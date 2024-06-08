import os
#max_x = input('What is the max x?')
max_x = os.getenv('MAX_X')
print()
for x in range(0, int(max_x)):
    print(x)