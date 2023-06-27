'''
# William Brandon
# CTI-110-1001
# P4HW2 - Salary Calculator
# 6/15/2023
# This program calculates pay over hours worked taking into account OT pay.
# The program uses a while loop with a string condition to allow for
# for multiple data entries
'''


def main(): 
  employee_name = input("Enter employee's name or type 'Done' to terminate: ")  
  total_NE = 0
  total_POT = 0
  total_RP = 0
  total_GP = 0

  while employee_name != 'Done' and employee_name != 'done': 
    hours_worked = float(input('Enter number of hours worked: '))
    pay_rate = float(input("Enter employee's pay rate: "))
    
    if hours_worked > 40:
        over_time = hours_worked - 40
        OT_pay = over_time * (pay_rate * 1.5)
        reg_pay = pay_rate * 40
        gross_pay = reg_pay + OT_pay
    else:
        over_time = 0
        OT_pay = 0
        reg_pay = hours_worked * pay_rate
        gross_pay = reg_pay
    
    print('----------------------------------------')
    
    print('Employee name:  ', employee_name)
    print()
    print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
    print('--------------------------------------------------------------------------------')
    print(f'{hours_worked:.1f}           {pay_rate:.2f}       {over_time:.1f}        {OT_pay:.2f}           ${reg_pay:.2f}       ${gross_pay:.2f}')
    
    total_NE += 1
    total_POT += OT_pay
    total_RP += reg_pay
    total_GP += gross_pay

    print()
    employee_name = input("Enter employee's name or type 'Done' to terminate: ") 
    
  else: 
    print()
    print('Total number of employees entered:', total_NE)
    print(f'Total amount paid for overtime: ${total_POT:.2f}')
    print(f'Total amount paid for regular hours: ${total_RP:.2f}')
    print(f'Total amount paid in gross: ${total_GP:.2f}')


main()

