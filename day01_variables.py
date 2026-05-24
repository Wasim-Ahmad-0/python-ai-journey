# writing the code to get the name and of the user and print the name and age + 10 as a result

user_name = input("What is your name? ").strip().title()
user_age = int(input("What is your age? "))

print(f"My name is {user_name} and I will be {user_age + 10} in ten years")
# this will print the name and the age after ten years
