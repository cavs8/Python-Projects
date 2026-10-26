n = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 0:
    print("Please enter a valid age.")
else:
    print(f"Hello, {n}! You are {age} years old."  )
    print("You'll turn 100 years old in the year", 2026 - age + 100)