a = int(input("Enter value of a: "))
count = a if a % 2 != 0 else a - 1
result = [2 * i + 1 for i in range((count + 1) // 2)]
print(", ".join(map(str, result)))
