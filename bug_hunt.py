count = 1
total = 0

# BUG: The while statement was missing a colon at the end, so I added one.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The original print tried to concatenate a string and an integer, so I used a comma.
print("Sum of 1 to 5 is:", total)
