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
    print("Error: Please enter a valid whole number.")
