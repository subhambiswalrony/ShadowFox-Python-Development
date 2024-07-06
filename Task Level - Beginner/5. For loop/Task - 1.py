'''
Using a for loop, simulate rolling a sixsided die multiple times (at least 20
times).
Count and print the following statistics:
How many times you rolled a 6
How many times you rolled a 1
How many times you rolled two 6s in a row
'''


rolls = 20
count_6 = 0
count_1 = 0
count_double_6 = 0
last_roll_was_6 = False

for i in range(rolls):

    roll = (i % 6) + 1
    if roll == 6:
        count_6 += 1
        if last_roll_was_6:
            count_double_6 += 1
        last_roll_was_6 = True
    else:
        last_roll_was_6 = False
        if roll == 1:
            count_1 += 1

print(f"Number of times rolled a 6: {count_6}")
print(f"Number of times rolled a 1: {count_1}")
print(f"Number of times rolled two 6s in a row: {count_double_6}")
