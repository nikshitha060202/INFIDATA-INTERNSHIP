quize=input("are you ready for a quize?(y/n):").lower()
if(quize=='y'):
    print("ok,here it comes!")
    score=0
    q1=int(input("what is the capital of alaska? 1:melbourne 2:anchorage 3:juneau"))
    if(q1==3):
        print("that's right!")
        score+=1
    else:
        print("sorry its wrong")
        q2=int(input("can you store the value cat in a variable of type int? 1:yes 2:no"))
        if(q2==1):
            print("sorry cat is a string ints can only store numbers")
        else:
            print("its right")
            score+=1
            q3=int(input("what is the result of 9+6/3?1:5 2:11 3:15/3"))
            if(q3==2):
                print("that's correct!")
                score+=1
            else:
                print("not correct")
                print("total score is",score)
