num={1:10,2:20,3:30,4:40}
print(2 in num)
print(5 in num)
print(2 not in num)
print(5 not in num)
print(40 in num) # it takes as key  #output is False
print(40 in num.values()) # it takes as values # output is True
print(40 not in num)
print(40 not in num.values())