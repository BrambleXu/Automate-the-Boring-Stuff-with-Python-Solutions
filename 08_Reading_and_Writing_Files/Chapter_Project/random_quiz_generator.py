'''
项目：生成随机的测验试卷文件
假如你是一位地理老师，班上有35名学生，你希望进行美国各州首府的一个小测验。不妙的是，班里有几个坏蛋，你无法确信学生不会作弊。你希望随机调整问题的次序，这样每份试卷都是独一无二的，这让任何人都不能从其他人那里抄袭答案。当然，手工完成这件事又费时又无聊。好在，你懂一些Python。

下面是程序所做的事：

创建35份不同的测验试卷。
为每份试卷创建50个多重选择题，次序随机。
为每个问题提供一个正确答案和3个随机的错误答案，次序随机。
将测验试卷写到35个文本文件中。
将答案写到35个文本文件中。
这意味着代码需要做下面的事：

将州和它们的首府保存在一个字典中。
针对测验文本文件和答案文本文件，调用open()、write()和close()。
利用random.shuffle()随机调整问题和多重选项的次序。
'''
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.


import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quiz_num in range(35):
    # TODO: Create the quiz and answer key files.
    quiz_file = open('capitalsquiz%s.txt' % (quiz_num + 1), 'w')
    answer_key_file = open('capitalsquiz_answers%s.txt' % (quiz_num + 1), 'w')

    # TODO: Write out the header for the quiz.
    quiz_file.write('Name:\n\nData:\n\nPeriod:\n\n')
    quiz_file.write((' '*20) + 'State Capitals Quiz (Form %s)' % (quiz_num + 1))
    quiz_file.write('\n\n')

    # TODO: Sheffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for question_num in range(50):

        # Get right and wrong answer
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # TODO: Write the question and anser option to the quiz file.
        quiz_file.write('%s. What is the capital of %s?\n' % (question_num + 1, states[question_num]))
        for i in range(4):
            quiz_file.write(' %s. %s\n' % ('ABCD'[i], answer_options[i]))
            quiz_file.write('\n')

        # TODO: Write the anser key to a file.
        answer_key_file.write('%s. %s\n' % (question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))
    quiz_file.close()
    answer_key_file.close()
