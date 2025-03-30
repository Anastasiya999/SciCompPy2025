# Make a loop over integer numbers from 1 to 40.
# If x is divided by 5 then print a message 'x is divided by 5'.
# If x is divided by 7 then print a message 'x is divided by 7'.
# If x is divided by 5 and 7 then print a message 'x is divided by 5 and 7'.
# Skip x = 13.
# If x is not divided by 5 and x is not divided by 7
# then print a message 'x is not important'.
# Prepare two solutions with 'while' and 'for' loops.

# 1. while loop
x = 1
while x <= 40:
    if x == 13:
        x += 1
        continue

    if x % 5 == 0 and x % 7 == 0:
        print(f"{x} is divided by 5 and 7")
    elif x % 5 == 0:
        print(f"{x} is divided by 5")
    elif x % 7 == 0:
        print(f"{x} is divided by 7")
    else:
        print(f"{x} is not important")

    x += 1

# 2. for loop
for x in range(1, 41):
    if x == 13:
        continue

    if x % 5 == 0 and x % 7 == 0:
        print(f"{x} is divided by 5 and 7")
    elif x % 5 == 0:
        print(f"{x} is divided by 5")
    elif x % 7 == 0:
        print(f"{x} is divided by 7")
    else:
        print(f"{x} is not important")
