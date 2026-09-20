def add_two_numbers() -> int:
    line = input()
    values = line.split(',')
    sum=0
    for i in range(len(values)):
        sum+=int(values[i])
    return sum


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
