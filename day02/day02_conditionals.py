try:
    # 1. Take score input and convert to integer
    score = int(input("Enter your test score (0-100): "))

    # 2. Check for the bonus perfect score first
    if score == 100:
        print("Perfect Score! 🌟 You got an A+!")
    
    # 3. Check standard grade boundaries
    elif 80 <= score <= 99:
        print("Grade: A")
    elif 60 <= score <= 79:
        print("Grade: B")
    elif 40 <= score <= 59:
        print("Grade: C")
    elif 33 <= score <= 39:  # Fixed the syntax error here
        print("Grade: D")
    elif 0 <= score < 33:
        print("Grade: Fail")
    else:
        print("Invalid score! Please enter a number between 0 and 100.")

except ValueError:
    # This catches the error if the user types words instead of numbers
    print("Error: Please enter a valid whole number.")
