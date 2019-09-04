num = [6, 32, 11, 15,]
num_two = [2, 4, 6, 8]
new_num = []
index = 0

while index < len(num_two):
    for n in num:
        result = n * num_two[index]
        index += 1
        new_num.append(result)
        
print(new_num)
