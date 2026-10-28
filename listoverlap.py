L1 = input("Enter a list of numbers: ").split()
L2 = input("Enter another list of numbers: ").split()

for i in L1:
    if i in L2:
        print(i, "is present in both lists.")