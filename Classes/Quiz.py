from QuestionBank import quiz
from Classes.Question import Question
import random


class Quiz:
    def __init__(self):
        self.questions = self.get_questions()
        self.shuffle_quiz()

    def get_questions(self):
        bank = []
        for key in quiz:
            question = key
            if isinstance(quiz[key], list):
                choices = quiz[key][1:]
                answer = quiz[key][0]
            else:
                choices = None
                answer = quiz[key]
            bank.append(Question(question=question, answer=answer, choices=choices))
        return bank

    def shuffle_quiz(self):
        random.shuffle(self.questions)

    def start_quiz(self):
        for question in self.questions:
            print("=============================================================================================")
            question.ask_question()
        print("=============================================================================================")
        self.grade_quiz()

    def grade_quiz(self):
        correct = 0
        total = len(self.questions)
        for question in self.questions:
            if question.answer == question.response:
                correct += 1
        print("You got a total of " + str(correct) + "/" + str(total) + " questions correct.")
