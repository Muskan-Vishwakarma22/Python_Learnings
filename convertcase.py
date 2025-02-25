st = input("Enter the string: ")

def lowercase(a):
    return a.lower()

def uppercase(a):
    return a.upper()

if st.isnumeric():
    print("Invalid Input")
elif st.isalpha():  # Checking for alphabetic input instead of alphanumeric
    ch = input("Enter your choice\n1. Convert to UPPERCASE \n2. Convert to lowercase\n")
    
    if ch.isdigit():  # Ensuring input is a number before converting
        ch = int(ch)
        if ch == 1:
            print(uppercase(st))
        elif ch == 2:
            print(lowercase(st))
        else:
            print("Invalid choice")
    else:
        print("Invalid input, please enter a number.")
else:
    print("Invalid Input")
