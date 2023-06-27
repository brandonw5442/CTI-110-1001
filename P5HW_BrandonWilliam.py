import random

def adding_numbers():
  num1 = random.randint(0,99)
  num2 = random.randint(0, 99)
  answer = num1 + num2

  print(f'  {num1}')
  print(f'+ {num2}')
  print()
  print('Enter answer.')
  user_answer = int(input())
  user_tries = 0

  while user_answer != answer:
    if user_answer < answer:
      user_tries += 1
      print('Sorry guess is too low')
      print()
      user_answer = int(input('Try again: '))
    if user_answer > answer:
      user_tries += 1
      print('Sorry guess is too high')
      print()
      user_answer = int(input('Try again: '))
  else:
    user_tries += 1
    print('Congratulations!!!! Your answer is correct')
    print('Number of guesses:', user_tries)

  print()
  print()
def subtracting_numbers():
    num1 = random.randint(0,99)
    num2 = random.randint(0, 99) 

    if num2 > num1:
      temp = num2
      num2 = num1
      num1 = temp
    else:
      num1 = num1
      num2 = num2
      
    answer = num1 - num2

    print(f'  {num1}')
    print(f'- {num2}')
    print()
    print('Enter answer.')
    user_answer = int(input())
    user_tries = 0

    if user_answer == answer:
        user_tries += 1
        print('Congratulations!!!! Your answer is correct')
        print('Number of guesses:', user_tries)
      
    while user_answer != answer:
      if user_answer < answer:
        user_tries += 1
        print('Sorry guess is too low')
        print()
        user_answer = int(input('Try again: '))
      elif user_answer > answer:
        user_tries += 1
        print('Sorry guess is too high')
        print()
        user_answer = int(input('Try again: '))
    else:
      user_tries += 1
      print('Congratulations!!!! Your answer is correct')
      print('Number of guesses:', user_tries)
    
    print()
    print()
  
def main():
  menu_option = 1
  while (menu_option != 3):
    print('Welcome to Math Quiz')
    print()
    print()
    print()
    print('MAIN MENU')
    print('------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()
    
    menu_option = int(input('Please choose one of the menu options: '))
  
    if menu_option == 1:
      adding_numbers()
    elif menu_option == 2:
      subtracting_numbers()
    elif menu_option == 3:
      print('Thank you for playing...')
      print('Bye!!')
    else:
      print('Invalid entry. Try again')
      print()
        
main()
