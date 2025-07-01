a = int(input("Enter value of a: "))
result = [2 * i + 1 for i in range(a)]
print(", ".join(map(str, result)))
