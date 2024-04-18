print("smallest number in list using without built in function")
ls = [23,5,16,8,15,26,6]
snum = ls[0]
for i in ls:
    if i < snum:
        snum = i
        print(i," is smallest number")