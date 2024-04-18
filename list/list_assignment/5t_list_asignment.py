print("find given list is ascending order or not")
ls = [24,26,57,89,99]
print(ls)
tlist = ls[:]
ls.sort()
if tlist == ls:
    print("ascending order")
else:
    print("not in ascending order")
