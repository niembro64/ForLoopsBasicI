for x in range (0, 10, 2):
    print(x)

print()
print()
for x in 'Hello':
    print(x)

print()
print()
# Create a Python file called for_loop_basic1.py that performs the following tasks.
# Basic - Print all integers from 0 to 150.
for x in range (0, 150):
    print(x)

print()
print()
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for x in range (5, 1001, 5):
    print(x)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range (1, 100):
    if (x % 10 == 0):
        print("Coding Dojo")
    elif(x % 5 == 0):
        print("Coding")
    else:
        print(x, end=' ')

print()
print()
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range (0, 500000):
    sum += x
print(f"Sum: %d" % sum)

print()
print()
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range (2018, 1, -4):
    print(f"In range %d" %  x)

print()
print()
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3

for x in range (2, highNum + 1):
    if (x % mult == 0):
        # print(x)
        print(f"Flexible Counter: %d" % x)

        