# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:24:34 2019

@author: admin
"""


portion_down_payment = 0.25
current_savings = 0
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percentage of your salary: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
monthly_salary = annual_salary/12
months_count = 0
r = 0.04
while current_savings <= (portion_down_payment*total_cost):
    current_savings += current_savings*r/12 + monthly_salary*portion_saved
    months_count += 1
    if months_count in range(0, 1000, 6):
        monthly_salary += monthly_salary*semi_annual_raise
print("Number of months:",months_count)