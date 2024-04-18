print("raise keyword demo")
try:
    raise ZeroDivisionError ("Demo message")  # raise is used for to give explicit call to except block
except ZeroDivisionError as e:
    print("am at ZeroDivitionError except block")
    print("e value",e)
print("end")
