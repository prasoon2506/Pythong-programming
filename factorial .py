def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

user_input = input("Enter numbers separated by commas: ")


numbers = [int(num) for num in user_input.split(',')]


factorial_results = [factorial(num) for num in numbers]

print(','.join(map(str, factorial_results)))
