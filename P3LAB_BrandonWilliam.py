is_leap_year = False
   
input_year = int(input())

if (input_year % 4) == 0:
    is_leap_year = True
else:
    is_leap_year = False
    
    
if (input_year % 100) == 0:
    is_leap_year = False
if (input_year % 100) == 0 and (input_year % 400) == 0:
    is_leap_year = True


if is_leap_year == 1:
    print(input_year, '- leap year')
else:
    print(input_year, '- not a leap year')

    
