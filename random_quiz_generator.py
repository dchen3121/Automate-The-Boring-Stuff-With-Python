#! python3

# random_quiz_generator.py - Creates quizzes with questions and answers
# in random order, along with the answer key
# This particular version creates 20 quizzes on Canadian provincial
# capitals.
# This in general can be used a template for creating matching & MC quizzes
# as long as a set is input.

import sys
import os
import random
import shutil

if len(sys.argv) == 1:
    number_of_quizzes = 20
else:
    try:
        number_of_quizzes = int(sys.argv[1])
    except ValueError:
        raise Exception('Expected an integer input greater than 1.')

capitals = {'British Columbia': 'Victoria',
            'Alberta': 'Calgary',
            'Saskatchewan': 'Regina',
            'Manitoba': 'Winnipeg',
            'Ontario': 'Toronto',
            'Quebec': 'Quebec City',
            'New Brunswick': 'Fredericton',
            'Nova Scotia': 'Halifax',
            'Prince Edward Island': 'Charlottetown',
            'Newfoundland and Labrador': 'St. John\'s',
            'Yukon': 'Whitehorse',
            'Northwest Territories': 'Yellowknife',
            'Nunavut': 'Iqaluit'}

shutil.rmtree('C:\\Users\\dchen\\Onedrive\\Desktop\\Projects\\'
              'Automate the Boring Stuff with Python\\Generated Quizzes')
os.makedirs('C:\\Users\\dchen\\Onedrive\\Desktop\\Projects\\'
            'Automate the Boring Stuff with Python\\Generated Quizzes')
os.chdir('C:\\Users\\dchen\\Onedrive\\Desktop\\Projects\\'
         'Automate the Boring Stuff with Python\\Generated Quizzes')

# Generate 20 quiz files.
for quizNum in range(number_of_quizzes):
    quizFile = open('capitals_quiz_v%d.txt' % (quizNum + 1), 'w')
    answerFile = open('capitals_quiz_answer_v%d.txt' % (quizNum + 1), 'w')
    # Writing Name and Date
    quizFile.write('Name:\n\nDate:\n\n\n')
    # Writing Quiz Title
    quizFile.write('Canadian Provincial Capital Cities Quiz Version %d\n\n' % (quizNum + 1))
    quizFile.write('Section 1: Fill in the blanks\n'
                   'Please write the corresponding capital city of each'
                   'province or territory.\n\n')
    answerFile.write('Answers for quiz version %d\n' % (quizNum + 1))
    answerFile.write('\nFill in the blanks section:\n')
    # Shuffle the order of the states and write them in the file
    newVersionCapitals = list(capitals.keys())
    random.shuffle(newVersionCapitals)
    count = 0
    for count in range(0, 4):
        quizFile.write('%d. ' % (count + 1))
        quizFile.write(str(newVersionCapitals[count]))
        quizFile.write(' ____________________\n')
        answerFile.write('%d. ' % (count + 1))
        answerFile.write(capitals[newVersionCapitals[count]])
        answerFile.write('\n')
    newVersionCapitals = newVersionCapitals[4:]
    quizFile.write('\nSection 2: Multiple Choice\n'
                   'Please circle the correct answer\n\n')
    answerFile.write('\nMultiple choice section:\n')
    for count in range(0, 4):
        quizFile.write('%d. ' % (count + 1))
        rand = random.randint(0, len(newVersionCapitals) - 1)
        province = newVersionCapitals[rand]
        correctAns = capitals[province]
        wrongAns = list(capitals.values())
        wrongAns.remove(correctAns)
        random.shuffle(wrongAns)
        listofAns = wrongAns[:3]
        rand = random.randint(0, 3)
        listofAns.insert(rand, correctAns)
        ans = 'ABCD'[rand]
        quizFile.write('The capital city of ' + province + ' is:\n')
        quizFile.write('\tA. ' + listofAns[0] + '\n')
        quizFile.write('\tB. ' + listofAns[1] + '\n')
        quizFile.write('\tC. ' + listofAns[2] + '\n')
        quizFile.write('\tD. ' + listofAns[3] + '\n\n')
        answerFile.write('%d. %s\n' % ((count + 1), ans))
        del newVersionCapitals[rand]
    quizFile.close()
    answerFile.close()

print(str(number_of_quizzes) + ' quizzes and their answer keys have been generated and stored in a file.')
# end of program
