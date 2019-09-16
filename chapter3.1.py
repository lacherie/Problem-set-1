## -*- coding: utf-8 -*-
#"""
#Created on Thu Sep 12 09:27:10 2019
#
#@author: admin
#"""
#
#Finger exercise: Write a program that asks the user to enter an integer and prints
#two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to 
#the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.

#i = int(input("Enter an integer: "))
#root = 0
#pwr = 0
#for pwr in range(0,6):
#    if i == root**pwr:
#        print("Root is",root)
#        print("Power is",pwr)
#        break
#    else:
#        root += 1
#else:
#    print("no such pair of integers exists.")
    

#i = int(input("Enter an integer: "))
#root = 0
#pwr = 0
#for root in range (-1000, 1000):
#    for pwr in range(0,7):
#        if i == root ** pwr:
#            print("Root is",root)
#            print("Power is",pwr)
#            break
#else:
#   print("No such pair of integers exists.")

#    i = int(input("Enter an integer: "))
#root = 0
#pwr = 0
#for root in range (-i, i):
#    for pwr in range(1, 6):
#        if i == root ** pwr:
#            print("Root is",root)
#            print("Power is",pwr)     
#            root = i + 1

i = int(input("Enter an integer: "))
root = -i
z = 0
while root in range(-i, i):
    for pwr in range(1, 6):
        if i == root ** pwr:
            if i > 0:
                    print("Root is",abs(root))
            else:
                    print("Root is",root)
            print("Power is",pwr)     
            z = 1
    if z == 1:
        break
    root += 1
if z != 1:
    print("No such pair of integers exists.")


