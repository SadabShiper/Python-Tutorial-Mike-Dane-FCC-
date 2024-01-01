# check the largest one between three numbers

li = [1, 2, 3]
if(li[0] > li[1] and li[0] > li[2]):
    print(str(li[0]) + " is the largest")
elif(li[1] > li[2] and li[1] > li[0]):
    print(str(li[1]) + " is the largest")
else:
    print(str(li[2]) + " is the largest")
    