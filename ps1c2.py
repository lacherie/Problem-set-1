# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:17:26 2019

@author: admin
"""
semi_annual_raise = 0.07
annual_return = 0.04
down_payment = 250000
annual_salary = int(input("Enter the starting salary: "))
num_steps = 0
low = 0
high = 10000
portion_saved = (high + low) // 2
current_savings = 0
epsilon = 10000
monthly_salary = annual_salary / 12
possible = True
while abs(current_savings - down_payment) > epsilon and possible == True:
    current_savings = 0
    for months_count in range(0, 36):
        current_savings += current_savings*annual_return / 12
        current_savings += monthly_salary*(portion_saved / 10000)
        if months_count % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    if current_savings < down_payment :
       low = portion_saved
    else:
       high = portion_saved
    if portion_saved == 9999:
        print("It is not possible to pay the down payment in three years.")
        possible = False
    portion_saved = (high + low) // 2
    num_steps += 1
    monthly_salary = annual_salary / 12
if possible == True:
    best_savings_rate = portion_saved / 10000
    print("Best savings rate: ", best_savings_rate)
    print("Steps in bisection search: ", num_steps)
