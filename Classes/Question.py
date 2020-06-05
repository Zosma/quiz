from Misc.ClearScreen import clear_screen


class Question:
    def __init__(self, question, answer, choices=None):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.response = ""

    def ask_question(self):
        clear_screen()
        print(self.question + "\n")
        if self.choices is not None:
            for i in range(0, len(self.choices)):
                print("\t" + str(i) + ") " + self.choices[i])
        self.response = input("Answer: ")
        if self.response.upper() == self.answer.upper():
            print("CORRECT!")
        else:
            print("WRONG! THE ANSWER IS: " + self.answer)

