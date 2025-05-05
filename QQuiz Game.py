import random

def ask_question(question, options, correct_answer):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            answer = int(input("Enter the number of your answer (1-4): "))
            if 1 <= answer <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    if options[answer-1] == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Wrong! The correct answer was: {correct_answer}")
        return 0

def main():
    print("Welcome to the Bangladesh History Guessing Game!")
    print("Answer 10 multiple-choice questions about Bangladesh's history.")
    print("Score at least 6 points to win and be called 'Deshi'!\n")

    # List of questions, options, and correct answers
    questions = [
        {
            "question": "In which year did Bangladesh gain independence from Pakistan?",
            "options": ["1965", "1971", "1975", "1981"],
            "correct": "1971"
        },
        {
            "question": "What was Bangladesh called when it was part of Pakistan?",
            "options": ["East Bengal", "West Pakistan", "East Pakistan", "Baluchistan"],
            "correct": "East Pakistan"
        },
        {
            "question": "Who was the leader of the Bengali Language Movement and later the first President of Bangladesh?",
            "options": ["Ziaur Rahman", "Sheikh Mujibur Rahman", "Hussain Muhammad Ershad", "Khaleda Zia"],
            "correct": "Sheikh Mujibur Rahman"
        },
        {
            "question": "Which empire ruled Bengal before the British East India Company took control after the Battle of Plassey in 1757?",
            "options": ["Maurya Empire", "Gupta Empire", "Mughal Empire", "Maratha Empire"],
            "correct": "Mughal Empire"
        },
        {
            "question": "What was the old name of Dhaka, changed in 1982?",
            "options": ["Jahangirnagar", "Dacca", "Bikrampur", "Sonargaon"],
            "correct": "Jahangirnagar"
        },
        {
            "question": "Which movement in 1952 led to Bengali being recognized as an official language of Pakistan?",
            "options": ["Swadeshi Movement", "Non-Cooperation Movement", "Bengali Language Movement", "Quit India Movement"],
            "correct": "Bengali Language Movement"
        },
        {
            "question": "Which river, originating in Tibet, is a major river in Bangladesh?",
            "options": ["Ganges", "Brahmaputra", "Meghna", "Padma"],
            "correct": "Brahmaputra"
        },
        {
            "question": "Who was the British officer after whom Cox's Bazar is named?",
            "options": ["Captain Hiram Cox", "Lord Curzon", "Robert Clive", "Warren Hastings"],
            "correct": "Captain Hiram Cox"
        },
        {
            "question": "Which sultanate, founded by Fakhruddin Mubarak Shah, ruled Bengal from the 14th century?",
            "options": ["Delhi Sultanate", "Bengal Sultanate", "Tughlaq Sultanate", "Mamluk Sultanate"],
            "correct": "Bengal Sultanate"
        },
        {
            "question": "Which Indian Lieutenant General accepted the Pakistani surrender in Dhaka on December 16, 1971?",
            "options": ["J. F. R. Jacob", "J. S. Aurora", "Sam Manekshaw", "K. M. Cariappa"],
            "correct": "J. S. Aurora"
        }
    ]

    # Shuffle questions to randomize order
    random.shuffle(questions)

    score = 0
    for i, q in enumerate(questions[:10], 1):  # Ensure exactly 10 questions
        print(f"Question {i}:")
        score += ask_question(q["question"], q["options"], q["correct"])

    # Display final score and result
    print("\nGame Over!")
    print(f"Your final score: {score}/10")
    if score >= 6:
        print("Congratulations! You are a true Deshi!")
    else:
        print("Sorry, you didn't score enough to be called Deshi. Try again!")

if __name__ == "__main__":
    main()