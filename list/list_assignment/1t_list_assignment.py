print("largest number in the list using without built in function")
ls = [23, 6, 12, 56, 32, 2]
lnum = ls[0]
for i in ls:
    if i > lnum:
        lnum = i
        print(i,'largest number')


