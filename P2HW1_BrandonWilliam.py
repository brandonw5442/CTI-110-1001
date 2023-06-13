'''
#For assignment P2HW1, you will build on P1HW2 assignment . The only
 change you will be doing on P1HW2 is change how results are displayed,
 so a very easy assignment. The program calculates business expenses then
 calculates and displays travel expenses
#6-13-2023 
#CTI-110 P2HW1 - Travel
#William Brandon
'''

def main():
    print('This program calculates and displays travel expenses')
    budget = float(input('Enter Budget: '))
    location = input('Enter your travel destination: ')
    fuel_cost = float(input('How much do you think you will spend on gas? '))
    accomodation_cost = float(input('Approximately, how much will you need for accomodation/hotel? '))
    food_cost = float(input('Lastly how much will you need for food? '))
    leftover = budget - fuel_cost - accomodation_cost - food_cost
    print()
    print('------------Travel Expenses------------')
    print('Location:                ',  location)
    print(f'Initial Budget:           ${budget:.1f}')
    print(f'Fuel:                        ${fuel_cost:.1f}')
    print(f'Accomodation:        ${accomodation_cost:.1f}')
    print(f'Food Cost:              ${ food_cost:.1f}')
    print('-----------------------------------------')
    print()
    print(f'Remaining Balance:  ${leftover:.1f}')
    
main()
    
