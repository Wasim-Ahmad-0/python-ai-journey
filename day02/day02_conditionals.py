# Determine student grades based on their test marks

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
