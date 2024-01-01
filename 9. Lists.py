friends = ["inza", 2, False] # valid declaration --> a list can have many datatypes like string, boolean and number
friends = ["inza", "dipto", "ifti", "rafin", "salvi"]

print(friends)
print(friends[0])
print(friends[1])
print(friends[-1])
print(friends[-2])
print(friends[1:]) # index-1 upto last
print(friends[:1]) # 0 upto (1-1) 
print(friends[:4]) # 0 upto (4-1) 
print(friends[1:3]) # 1 upto (3-1) 
friends[0] = "inzamam"
print(friends)