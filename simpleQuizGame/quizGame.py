# Simple Quiz Game 🎮
# Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆

questions = [
    {'question': 'What is the capital city of Kenya?',
     'options': ['Nairobi', 'Kisumu', 'Nakuru'],
     'answer': 'Nairobi'},
    {'question': 'What is the IUPAC name for water?',
     'options': ['H2O', 'Oxidane', 'Aqua'],
     'answer': 'Oxidane'},
    {'question': 'Which of the following is not considered as a planet?',
     'options': ['Earth', 'Jupiter', 'Pluto'],
     'answer': 'Pluto'}
]

def quizGame():
    score = 0

    for question in questions:
        print(question['question'])

        for i, option in enumerate(question['options']):
            print(f'{i+1}. {option}')

        userAnswer = input('Enter your answer(1, 2, 3 or 4):')

        if userAnswer == str(question['options'].index(question['answer']) + 1):
            score += 1
            print('Correct!')
        else:
            print('Incorrect.')

    print(f'Your final score is: {score}/{len(questions)}')

playAgain = input('Do you want to play again? (yes/no):')
if playAgain.lower() == 'yes':
    quizGame()