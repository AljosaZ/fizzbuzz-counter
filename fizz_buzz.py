print("Welcome to fizzbuzz counter!\n")

count_limit = int(input("Please enter a number you want the counter to count up to: "))

for i in range(1, count_limit + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
