price = int(input("enter the price"))
tax = 0
if(price>100000):
    tax = price * 15%100
    print("road tax is",tax)
elif(price>50000 and price<=100000):
    tax = price - 50000 * 10%100
    print("road tax is",tax)
elif(price<=50000):
    tax = price * 5%100
    print("road tax is",tax)

