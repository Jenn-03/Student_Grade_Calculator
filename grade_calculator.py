def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent! Outstanding performance! 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good Job! You can do even better! 😊"
    elif 60 <= marks <= 69:
        return "D", "Keep Working Hard! Improvement is possible! 💪"
    else:
        return "F", "Don't give up! Practice and try again! 📚"


name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid input! Marks must be between 0 and 100.")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", name.upper() + ":")
print("Marks:", str(marks) + "/100")
print("Grade:", grade)
print("Message:", message)
