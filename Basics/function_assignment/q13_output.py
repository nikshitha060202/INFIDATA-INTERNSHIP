def test(a,b=5,c=10):
    print('a is',a,'and b is', b,'and c is',c)

test(3,7)
test(25,c=24)
test(c=50,a=100)