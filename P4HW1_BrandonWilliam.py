def score_keeper(num_of_scores):
    list_of_scores = []
    i = 0
    for i in range(num_of_scores):
        score = float(input(f'Enter score #{i + 1}: '))
        if score >= 0:
            list_of_scores.append(score)
        else:
            print()
            print('INVALID Score entered!!!')
            print('Score should be between 0 and 100')
            while score <= 0:
              score = float(input(f'Enter score #{i + 1} again: '))
              if score >= 0:
                list_of_scores.append(score)
        
    return list_of_scores

def grade_calculator(score_average):
    if score_average >= 90:
        grade = 'A'
    elif score_average >= 80:
        grade = 'B'
    elif score_average >= 70:
        grade = 'C'
    elif score_average >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    return grade
    

def main():
    num_of_scores = int(input('How many scores do you want to enter? '))
    print()
    list_of_scores = score_keeper(num_of_scores)

    min_score = min(list_of_scores)
    list_of_scores.remove(min_score)
    score_average = sum(list_of_scores) / len(list_of_scores)
    grade = grade_calculator(score_average)
    
      
    print()
    print()
    print('---------------Results---------------')
    print(f'Lowest Score   : {min_score}')
    print(f'Modified List  : {sorted(list_of_scores)}')
    print(f'Scores Average : {score_average:.2f}')
    print(f'Grade          : {grade}')
    print('-------------------------------------')
    
main()
