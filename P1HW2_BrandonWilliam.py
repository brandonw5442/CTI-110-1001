# Program calculates and displays travel expenses

# 6-1-2023

# CTI-110 P1HW2 - Travel Expense

# William Brandon
''' Pseudocode:
    Input statement prompting user to enter their budget
    Input statement for travel destination
    Input statement for gas expenses
    Input statement for accommodation expenses
    Input statement for food expenses
    Input statement for additional expenses
    Subtracts expenses from budget
    Display
'''
print('This program calculates and displays travel expenses')
budget = float(input('Enter budget: '))
destination = input('Enter your travel destination: ')
fuel = float(input('How much do you think you will spend on gas? '))
accomodation = float(input('Approximately, how much will you need for accomodation/hotel? '))
food = float(input('Last, how much do you need for food? '))
print('------------Travel Expenses------------')
print('Location:', destination)
print('Initial budget:', budget)
print()
print('Fuel:', fuel)
print('Accomodation:', accomodation)
print('Food:', food)
total = fuel + accomodation + food
print()
print('Remaining Balance:', (budget - total)) 
