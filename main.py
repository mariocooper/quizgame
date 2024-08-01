questions = [
    {
        "prompt": "What country is NOT in the United Kingdom?",
        "options": ["A: England", "B: Scotland", "C: Ireland", "D: Wales"],
        "answer": "C"
    },
    {
        "prompt": "Which of the following foods is a carbohydrate?",
        "options": ["A: Bread", "B: Beef", "C: Butter", "D: Salmon"],
        "answer": "A"
    },
    {
        "prompt": "What country is NOT in Europe?",
        "options": ["A: Italy", "B: Portugal", "C: Albania", "D: Morocco"],
        "answer": "D"
    },
    {
        "prompt": "Which of the following is NOT a country singer?",
        "options": ["A: Luke Combs", "B: Victor Leksell", "C: Morgan Wallen", "D: Bailey Zimmerman"],
        "answer": "B"
    },
]

def quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Please enter your answer: ").upper()
        if answer == question["answer"]:
            print("Correct answer!\n")
            score += 1
        else:
            print(f'Incorrect answer! The correct answer was {question["answer"]}.\n')
    print(f"You got {score} correct answers out of a total of {len(questions)}!")

quiz(questions)
