import random

n = random.randint(3, 20)
print(n)
result = ''
for i in range(1, 21):
    for j in range(i + 1, 21):
        if n % (i + j) == 0:
            result = result + str(i) + str(j)

print(result)
