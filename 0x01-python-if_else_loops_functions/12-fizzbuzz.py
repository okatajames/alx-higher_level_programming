#!/usr/bin/python3
i = [p for p in range(1, 100)]
print(i)
for integ in i:
    if integ % 3 == 0 and integ % 5 == 0:
        print("FizzBuzz")
    elif integ % 3 == 0:
        print("Fizz")
    elif integ % 5 == 0:
        print("Buzz")
    else:
        print(integ)
