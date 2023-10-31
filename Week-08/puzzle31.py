input = []
for i in range(1000):
    input.append(i)

output = []

for i in range(len(input)):
    output += list(map(int, str(input[i])))


print(output)              
sum_first_1000_chars = sum(output[0:1001])
print(sum_first_1000_chars)