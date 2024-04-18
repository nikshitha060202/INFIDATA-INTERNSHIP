quize=input("are you ready for a quize?(y/n):").lower()
if(quize=='y'):
    print("ok,here it comes!")
    questions=[{"q":"1.what is the capital of alaska?",
                "options":["1.melbourne","2.anchorage","3.juneau"],
                "correct_ans":"3"},
               {"q":"2.can you store the value cat in a variable of type int?",
                "options":["1.yes","2:no"],
                "correct_ans":"2"},
               {"q":"3.what is the result of 9+6/3?",
                "options":["1.5","2.11","3.15/3"],
                "correct_ans":"2"},]
