class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer multiple-choice or fill-in-the-blank questions to test your knowledge.")
        print("Let's begin!\n")

    def present_quiz_questions(self):
        for index, question in enumerate(self.questions, start=1):
            print(f"Question {index}: {question['question']}")
            if 'choices' in question:
                for choice_index, choice in enumerate(question['choices'], start=1):
                    print(f"{choice_index}. {choice}")
            user_answer = input("Your answer: ").strip().lower()
            self.evaluate_user_answer(user_answer, question['answer'])
            print()

    def evaluate_user_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {correct_answer}\n")

    def display_final_results(self):
        print("Quiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        print("Thank you for playing!")

def main():
    quiz_questions = [
        {
            'question': "who invented c language?",
            'answer': "Dennis Ritchie"
        },
        {
            'question': "Who wrote the play 'Romeo and Juliet'?",
            'answer': "William Shakespeare"
        },
        {
            'question': "which team won the the FIFA World Cup 2022?",
            'answer': "Argentina"
        }
        # Add more questions here
    ]

    quiz_game = QuizGame(quiz_questions)
    quiz_game.display_welcome_message()
    quiz_game.present_quiz_questions()
    quiz_game.display_final_results()

if __name__ == "__main__":
    main()
