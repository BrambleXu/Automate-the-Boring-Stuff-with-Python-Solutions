"""
In this solution we obtain 2 different folder:
    1: quiz-papers folder that contains 35 different quizzes
    2: quiz-answers folder that contains answer keys to the each quizzes

Each quiz is different from the others in terms of question order and
options' order of the each question
"""
from random import shuffle
import random
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# creating a 'quiz-papers' folder for question papers
if not os.path.exists(os.getcwd() + '/quiz-papers'):
    os.mkdir('quiz-papers')
# creating a 'quiz-answers' folder contains answer keys for each question paper
if not os.path.exists(os.getcwd() + '/quiz-answers'):
    os.mkdir('quiz-answers')

quizFilesPath = os.getcwd() + '/quiz-papers'
quizAnswersPath = os.getcwd() + '/quiz-answers'
states = list(capitals.keys())

for i in range(35):

    # creating question papers and adding header to each one of them
    questionFile = open(quizFilesPath + '/quiz' + str(i + 1) + '.txt', 'w')
    questionFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    questionFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (i + 1))
    questionFile.write('\n\n')
    
    # creating answer key for each question paper
    answerFile = open(quizAnswersPath + '/quiz' + str(i + 1) + 'answers.txt', 'w')

    shuffle(states)
    questionNumber = 1

    for state in states:        
        questionFile.write('\n\nQ' + str(questionNumber) + ':\nWhat is the capital of the ' + str(state) + '?\n\n')
        answerFile.write('\n\nQ' + str(questionNumber) + ':\n' + str(capitals[state]) + '\n\n')
        questionNumber += 1
        capitalList = list(capitals.values())
        capitalList.remove(str(capitals[state]))

        # adding correct answer to the options
        choices = [str(capitals[state])]

        # adding 3 wrong answers to the options
        for i in range(3):
            randNum = random.randint(0, len(capitalList) - 1)
            choices.append(capitalList[randNum])
            del capitalList[randNum]

        shuffle(choices)
        for i in range(len(choices)):
            questionFile.write(str(choices[i]) + '\t')

        questionFile.write('\n')

questionFile.close()
answerFile.close()
