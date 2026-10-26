n = int(input("Enter a number: "))

if n % 2 == 0:
    print(f"{n} is even.")
else:
    print(f"{n} is odd.")

if n % 4 == 0:
    print(f"{n} is divisible by 4.")
else:
    pass

num = int(input("Enter another number: "))
check = int(input("Enter a one more number: "))

if num % check == 0:
    print(f"{num} is divisible by {check}.")
else:
    print(f"{num} is not divisible by {check}.")