# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""

print('Enter 4-digit number')
num = input()

try:
    num_int = int(num)

    if ((num_int > 999) and (num_int < 10000)):
        list_digit = [int(i) for i in str(num_int)]
        sum = list_digit[0]+list_digit[1]+list_digit[2]+list_digit[3]  
        print(f'Sum of digits: {sum}')
    else: 
        print('Enter valid number')

except ValueError:
    print('Enter valid number')