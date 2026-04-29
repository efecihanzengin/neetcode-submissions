def add_two_numbers() -> int:
    numbers = input().split(",")

    total = 0
    for i in numbers:
        total += int(i)

    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
