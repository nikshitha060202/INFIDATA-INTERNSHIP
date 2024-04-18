print("check key is their in given dictionary")
d1={1:"python",2:"java",3:"web",4:"c"}
print(d1)
key=int(input("enter the key:"))
if key in d1:
    print(key,"already exit in dictionary")
else:
    print(key,"not exit in dictionary")