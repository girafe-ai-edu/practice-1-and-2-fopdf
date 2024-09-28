# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
weight = input()
height = input()

#code here

weight_float = float(weight)
height_float = float(height)

if (weight_float > 0) and (height_float > 0):
    BMI = weight_float/height_float**2
    print(f'Your BMI: {round(BMI,2)}') 
else:
    print('Enter valid height and weight')