#!/usr/bin/env python3
import sys

def count_salary(salary,tax,found):
    if tax <= 0:
        tax_out = 0
        money = salary - tax_out - found 
    elif tax <= 1500:
        tax_out = tax * 0.03
        money = salary - tax_out - found 
    elif tax <= 4500:
        tax_out = tax * 0.1 - 105
        money = salary - tax_out - found 
    elif tax <= 9000:
        tax_out = tax * 0.2 - 555
        money = salary - tax_out - found 
    elif tax <= 35000:
        tax_out = tax * 0.25 - 1005
        money = salary - tax_out - found 
    elif tax <= 55000:
        tax_out = tax * 0.3 - 2755
        money = salary - tax_out - found 
    elif tax <= 80000:
        tax_out = tax * 0.35 - 5505
        money = salary - tax_out - found 
    else:
        tax_out = tax * 0.45 - 13505
        money = salary - tax_out - found 
    return(money)

l = len(sys.argv)
if l >= 2:
    for arg in sys.argv[1:]:
        number,gongzi = arg.split(':')
        try:
            salary = int(gongzi)
            found = salary * 0.165
            tax = salary - 3500 - found
        except ValueError: 
            print("Parameter Error")
            sys.exit()
        except NameError: 
            print("Parameter Error")
            sys.exit()
        money = count_salary(salary,tax,found)
       
        print(number+':{:.2f}'.format(money))
else:
    print("Parameter Error")

