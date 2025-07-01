nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
multiples = {i: 0 for i in range(1, 10)}

for i in range(1, 10):
    for n in nums:
        if n % i == 0:
            multiples[i] += 1

print(multiples)