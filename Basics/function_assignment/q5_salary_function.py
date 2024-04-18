def salary():
    salary=int(input("enter ur salary"))
    service=int(input("enter yor time period of service"))
    if service>10:
        bonus = 0.1
        netbonus = salary * bonus
        print("netbonus of {0} and {1} is {2}".format(salary, bonus, netbonus))
    elif service>=6 and service<=10:
        bonus = 0.08
        netbonus = salary * bonus
        print("netbonus of {0} and {1} is {2}".format(salary, bonus, netbonus))
    elif service > 6:
        bonus = 0.05
        netbonus = salary * bonus
        print("netbonus of {0} and {1} is {2}".format(salary,bonus,netbonus))
salary()
