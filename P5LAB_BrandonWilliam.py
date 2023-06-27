def is_leap_year(user_year):
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_feb(user_year):
    if is_leap_year(user_year):
        return 29
    else:
        return 28



if __name__ == '__main__':
    year_input = int(input())
    days_in_february = days_in_feb(year_input)
    print(year_input, 'has', days_in_february, 'days in February.')
    
    
    
    

