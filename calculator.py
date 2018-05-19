#!/usr/bin/env python
import sys
l = len(sys.argv)
if l == 2:
    try:
        salary = int(sys.argv[1])
        tax = salary - 3500
    except ValueError: 
        print("Parameter Error")
    except NameError: 
        print("Parameter Error")
    if tax <= 0:
        money = 0
    elif tax <= 1500:
        money = tax * 0.03
    elif tax <= 4500:
        money = tax * 0.1 - 105
    elif tax <= 9000:
        money = tax * 0.2 - 555
    elif tax <= 35000:
        money = tax * 0.25 - 1005
    elif tax <= 55000:
        money = tax * 0.3 - 2755
    elif tax <= 80000:
        moeny = tax * 0.35 - 5505
    else:
        money = tax * 0.45 - 13505
    print("{:.2f}".format(money))
else:
    print("Parameter Error")
