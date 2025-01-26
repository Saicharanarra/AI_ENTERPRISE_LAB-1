def is_even(num: int) -> bool:
    return num % 2 == 0
try:    
    test_number = int(input("Enter an integer to check: "))
    if is_even(test_number):
        print(f"{test_number} is an even number.")
    else:
        print(f"{test_number} is an odd number.")
except ValueError:
    print("Please enter a valid integer to check for even or odd.")

