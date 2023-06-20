'''
# William Brandon
# CTI-110-1001
# P3HW2
# 6/15/2023
# This program calculates pay over hours worked taking into account over time
'''
employee_name = input("Enter employee's name: ")
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
print(f'{hours_worked:.1f}           {pay_rate:.1f}       {over_time:.1f}        {OT_pay:.2f}           ${reg_pay:.2f}       ${gross_pay:.2f}')    
