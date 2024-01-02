str = input("Enter a string to translate: ")

vowels = "AaEeIiOoUu"
translate = ""
flag = False

for char in str:
    for v in vowels:
        if char == v:
            flag = True
            break
    if flag == True:
        translate += "g"
    else:
        translate += char
    
    flag = False

print(translate)
    
        
        