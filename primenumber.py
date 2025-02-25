# Writing a code to print Whether a series of number is prime or not

# Taking input for number of elements
n = int(input("Enter the number of numbers: "))
# Taking input of numbers separated by spaces
numbers = input("Enter the numbers separated by spaces: ").split()
# Checking prime status and printing result
result = ""
for num in numbers:
    num = int(num)
    if num < 2:
        result += "np "
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result += "p "
        else:
            result += "np "

print(result.strip())