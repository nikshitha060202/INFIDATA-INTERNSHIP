odd_dict={i:i+2 for i in range(1,10,2)} # 1 is starting number, 10 is end number 2 is steps or increament
print(odd_dict)
square_dict={i:i**2 for i in range(1,7)}
print(square_dict)
even_square={i:i*i for i in range(1,10)if i%2==0} # the symbol(**)double star means power or square
print(even_square)
odd_square={i:i*i for i in range(1,10)if i%2!=0}
print(odd_square)