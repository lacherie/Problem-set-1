# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:46:28 2019

@author: admin
"""

portion_down_payment = 0.25
r = 0.04 # interest rate
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
monthly_salary = annual_salary / 12
down_payment = portion_down_payment * total_cost

months_count = 0
current_savings = 0
while current_savings < down_payment:
    current_savings += current_savings * r / 12 + monthly_salary * portion_saved
    months_count += 1

print("Number of months: ", months_count)
