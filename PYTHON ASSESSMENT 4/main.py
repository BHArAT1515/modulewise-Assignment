import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\nMenu:")
    print("1. Quiz Master Operations")
    print("2. Quiz Cracker")
    print("3. Exit")

def quiz_master_menu(questions):
    while True:
        print("\nQuiz Master Menu:")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Delete Question")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_question(questions)
        elif choice == '2':
            view_questions(questions)
        elif choice == '3':
            delete_question(questions)
        elif choice == '4':
            print("Exiting Quiz Master Menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def quiz_cracker_menu(questions):
    while True:
        print("\nQuiz Cracker Menu:")
        print("1. Display Questions")
        print("2. Check Answer")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_questions(questions)
        elif choice == '2':
            check_answer(questions)
        elif choice == '3':
            print("Exiting Quiz Cracker Menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def add_question(questions):
    question_id = input("Enter Question ID: ")
    question_text = input("Enter Question: ")
    options = input("Enter Options (comma-separated): ").split(',')

    # Add the question to the dictionary
    questions[question_id] = {'question': question_text, 'options': options}

    print("Question added successfully!")

def view_questions(questions):
    print("\nAll Questions:")
    for question_id, question_info in questions.items():
        print(f"ID: {question_id}, Question: {question_info['question']}, Options: {', '.join(question_info['options'])}")

def delete_question(questions):
    view_questions(questions)

    question_id = input("Enter Question ID to delete: ")

    if question_id in questions:
        del questions[question_id]
        print(f"Question with ID {question_id} deleted successfully!")
    else:
        print(f"Question with ID {question_id} not found.")

def display_questions(questions):
    view_questions(questions)

def check_answer(questions):
    question_id = input("Enter Question ID to answer: ")

    if question_id in questions:
        correct_answer = input(f"Options: {', '.join(questions[question_id]['options'])}\nEnter correct answer: ")
        if correct_answer.lower() == 'exit':
            return
        elif correct_answer in questions[question_id]['options']:
            print("Correct answer!")
        else:
            print("Incorrect answer.")
    else:
        print(f"Question with ID {question_id} not found.")

def save_to_log(data):
    with open('log.txt', 'a') as log_file:
        log_file.write(data + '\n')

def main():
    questions = {}

    while True:
        clear_screen()
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            quiz_master_menu(questions)
        elif choice == '2':
            quiz_cracker_menu(questions)
        elif choice == '3':
            print("Exiting the Quiz Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
