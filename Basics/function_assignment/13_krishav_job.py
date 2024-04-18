pay=int(input("enter pay amount"))
location=input("enter location")
if location == "mumbai":
    print("i will take it")
elif location == "chennai":
    if pay < 100000:
        print("no way")
    else:
        print("i am willing")
elif location == "delhi" and pay >40000:
    print("i am happy to join")
elif pay > 60000:
    print("i accept the offer")
else:
    print("no thanks, i can find something better")


