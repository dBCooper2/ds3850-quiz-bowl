# Friday Project 4: Quiz Bowl

# Author: Trevor Rowland

'''
We need a program that will allow us, as students, to study test questions. The program should
display questions from a dictionary. Users should then have a chance to answer; after they
answer, the program should provide feedback on whether the answer is correct or not.
'''

import random as r
import time
import sys
  
def quizBowl():

  # SET VARIABLES
  numCorrect = 0
  questions = {
  "Which country has won the most World Cups?":"Brazil",
  "Simone Biles is famous for her skill in what sport?":"Gymnastics",
  "What do you call it when a bowler makes three strikes in a row?":"Turkey",
  "What was the first name of Argentinian soccer star Maradona?":"Diego",
  "What sporting event has a strict dress code of all white?":"Wimbledon"
  }

  # WELCOME MESSAGE
  print(f'Welcome to the Quiz Bowl! You will be asked {len(questions)} questions', end='')
  
  for i in range(3):
    time.sleep(0.3)
    print('.', end='', flush=True)
    time.sleep(0.1)
  
  print()
  
  # THE GAME
  for i in range(len(questions)):
    q = r.choice(list(questions.keys())) # You need to order the list of keys, dicts are not ordered
    print(q)
    
    ans = str(input(': ')).lower()
    
    if ans == questions[q].lower():
      print('Correct!')
      numCorrect += 1
	
    questions.pop(q)
    print()
    
  print(f'Well Done! You finished the Quiz Bowl with a score of: {numCorrect}')
  
  print('Exiting', end='')
  
  for i in range(3):
    time.sleep(0.3)
    print('.', end='', flush=True)
    time.sleep(0.1)

  exit()
  
# RUN THE PROGRAM
quizBowl()
