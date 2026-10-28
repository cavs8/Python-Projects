n = int(input("Enter a number: "))
divisors = []

for _ in range(1,n):
    if n % _ == 0:
        divisors.append(_)

print("The divisors of", n, "are:", divisors)
