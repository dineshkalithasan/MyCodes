original_list = [10, 12, 17, 29, 4, 6]
new_list = []

for num in original_list:
    if num % 2 == 0:
        new_list.append(num)
# print(new)


r=5
for i in range(r):
    print("*" * r)

rows = 5
for i in range(1, rows + 1):  # Loop from 1 to 5
    for j in range(i):        # Loop 'i' times
        print("*", end=" ")
    print()

rows = 5
for i in range(1, rows + 1):
    # spaces = " " * (rows - i)
    stars = "* " * i
    print(stars)