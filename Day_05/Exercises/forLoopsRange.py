target=int(input("Number goes here: "))

target = target +2

total = 0
for number in range(0,target,2):
    total += number
print(total)