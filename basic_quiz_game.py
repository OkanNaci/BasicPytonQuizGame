print('Welcome to the Basic CS Quiz Game!')
playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    print("Okay, maybe next time!")
    quit()

print("Great! Let's get started.")
score = 0
total_questions = 25

questions = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What is the main function of RAM? ", "random access memory"),
    ("What does HTML stand for? ", "hypertext markup language"),
    ("Which language is known as the 'mother of all languages'? ", "c"),
    ("What is a variable in programming? ", "a named storage location"),
    ("What symbol is used for comments in Python? ", "#"),
    ("What does CSS stand for? ", "cascading style sheets"),
    ("What is the purpose of a loop in programming? ", "repetition"),
    ("Which data type stores true/false values in Python? ", "boolean"),
    ("What is the extension for Python files? ", ".py"),
    ("What does GUI stand for? ", "graphical user interface"),
    ("What is an algorithm? ", "a set of instructions"),
    ("What does SQL stand for? ", "structured query language"),
    ("What is the purpose of 'print' in Python? ", "output to console"),
    ("What is a function in programming? ", "a reusable block of code"),
    ("What does IDE stand for? ", "integrated development environment"),
    ("What is the binary number system base? ", "2"),
    ("What is the purpose of 'if' statements? ", "conditional execution"),
    ("Which operator is used for equality comparison in Python? ", "=="),
    ("What is a string in programming? ", "a sequence of characters"),
    ("What does API stand for? ", "application programming interface"),
    ("What is the purpose of a compiler? ", "translate code to machine language"),
    ("What is a database? ", "organized collection of data"),
    ("What does HTTP stand for? ", "hypertext transfer protocol"),
    ("What is the purpose of 'git' in version control? ", "track changes")
]

for i, (question, correct_answer) in enumerate(questions, 1):
    answer = input(f"Question {i}: {question}")
    if answer.lower() == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is '{correct_answer.title()}'.")

print(f"\nQuiz completed! Your score: {score}/{total_questions}")
percentage = (score / total_questions) * 100
print(f"Percentage: {percentage:.2f}%")
if percentage >= 80:
    print("Excellent job!")
elif percentage >= 60:
    print("Good effort!")
else:
    print("Keep practicing!")