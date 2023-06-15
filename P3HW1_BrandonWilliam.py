'''
# This program takes a number grade , determines average and displays letter
grade for average.
# William Brandon
# 6 / 15 / 2023
# CTI - 110 - 1001
'''

# Enter in grades for 6 modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
avg_of_grades = sum_of_grades / len(grades)

print()

#Display results
print('-----------------Results-----------------')
print(f'Lowest Grade:         {lowest_grade:.1f}')
print(f'Highest Grade:        {highest_grade:.1f}')
print(f'Sum of Grades:        {sum_of_grades:.1f}')
print(f'Average:              {avg_of_grades:.2f}')
print('------------------------------------------')
# determine letter grade for average


if avg_of_grades >= 90:
    print('Your grade is: A')
elif avg_of_grades >= 80:
    print('Your grade is: B')
elif avg_of_grades >= 70:
    print('Your grade is: C')
elif avg_of_grades >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')





