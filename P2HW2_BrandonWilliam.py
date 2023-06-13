# CTI-110
# P2HW2 - List
# William Brandon
# 6-13-2023

def main():
    module1 = float(input('Enter grade for Module 1: '))
    module2 = float(input('Enter grade for Module 2: '))
    module3 = float(input('Enter grade for Module 3: '))
    module4 = float(input('Enter grade for Module 4: '))
    module5 = float(input('Enter grade for Module 5: '))
    module6 = float(input('Enter grade for Module 6: '))
    grades = [module1, module2, module3, module4, module5, module6]
    lowest_grade = min(grades)
    highest_grade = max(grades)
    sum_of_grades = sum(grades)
    average = sum(grades) / len(grades) 
    print()
    print('------------Results------------')
    print(f'Lowest Grade:               {lowest_grade:.1f}')
    print(f'Highest Grade:               {highest_grade:.1f}')
    print(f'Sum of Grades:              {sum_of_grades:.1f}')
    print(f'Average:                        {average:.2f}')
    print('--------------------------------')
    
main()
    
