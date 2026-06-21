try:
    # 1. Take score input and convert to integer
    score = int(input("Enter your test score (0-100): "))

    # 2. Check for the bonus perfect score first
    if score == 100:
        print("Perfect Score! 🌟 You got an A+!")
    
    # 3. Check standard grade boundaries
    elif score >= 80:
        print("Grade: A")
    elif score >= 60:
        print("Grade: B")
    elif score >= 40:
        print("Grade: C")
    elif score >= 33:
        print("Grade: D")
    elif 0 <= score < 33:
        print("Grade: Fail")
    else:
        print("Invalid score! Please enter a number between 0 and 100.")

except ValueError:
    # This catches the error if the user types words instead of numbers
    print("Error: Please enter a valid whole number.")# Determine student grades based on their test marks

try:
    marks = int(input("What marks did you get? "))
    
    if marks < 0 or marks > 100:
        print("Please enter a valid mark between 0 and 100.")
    else:
        if marks >= 80:
            grade, message = "A", "You have passed the test"
        elif marks >= 60:
            grade, message = "B", "You can do better"
        elif marks >= 40:
            grade, message = "C", "You need to improve"
        else:
            grade, message = "D", "You have failed"

        print(f"{message}, you got {grade}.")

except ValueError:
    print("Invalid input! Please enter a whole number.")
