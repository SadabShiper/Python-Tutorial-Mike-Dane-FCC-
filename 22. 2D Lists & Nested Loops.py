number_grid = [
    [1, 2, 3],
    [5, 3, 2],
    [1, 3, 2],
    [0]   
]


print(number_grid)

# way - 1
print("way-1")
for row in number_grid:
    for num in row:
        print(num)

# way - 2
print("way-2")
for row in number_grid:
    for i in range(len(row)):
        print(row[i])
        