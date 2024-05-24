import csv

def load(Quiz_csv):
    quiz = []
    with open(Quiz_csv, 'r') as Quiz:
        reader = csv.DictReader(Quiz)
        for row in reader:
            quiz.append(row)
    return quiz

def ask_questions(quiz):
    score = 0
    for question in quiz:
        user_answer = input(f"{question['Question']} ")
        if user_answer.lower() == question['Answer'].lower():
            score += 1
    return score

def save_result(user_name, score):
    with open('results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_name, score])
def main ():
    quiz = load ('Quiz.csv')  
    user_name = input("Enter your name: ")   
    user_score = ask_questions(quiz)  
    print(f"Your score: {user_score}")
    save_result(user_name, user_score)
main ()









