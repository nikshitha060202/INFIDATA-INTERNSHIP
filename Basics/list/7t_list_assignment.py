ls = [22,23,25,46,55]
print(ls)
even = 0
odd = 0
for i in ls:
    if i % 2 == 0:
        even +=1
    else:
        odd +=1
print(even,"numbers are even in the list")
print(odd,"numbers are odd in the list")
