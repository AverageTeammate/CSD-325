# Jacob Cannamela
# CSD 205
# 10/5/24

# Recursive function to print numbers from 1 to n
def recursive_print(n):

    # Recursive function to print numbers from 1 to n.
    # It calls itself with (n - 1) until it reaches 1, then prints in reverse order.
    if n > 0:
        
        # Recursive call
        recursive_print(n - 1) 

        # Print current number for recursion
        print(n, end=' ')  

# Non-recursive function to print numbers from 1 to n
def non_recursive_print(n):

    # Non-recursive function to print numbers from 1 to n.
    # It uses a simple for loop to iterate and print each number.
    for i in range(1, n + 1):
        print(i, end=' ')

# Main function to validate input and run the test
def main():

    # Loop for input validation
    while True:
        try:
            n = int(input("Enter a positive integer greater than 0: "))
            if n <= 0:
                print("Please enter a valid positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    # Call and display output for recursive function
    print("\nInvoking the recursive function:")
    recursive_print(n)
    print("\nEnd of recursive function output.\n")

    # Call and display output for non-recursive function
    print("Invoking the non-recursive function:")
    non_recursive_print(n)
    print("\nEnd of non-recursive function output.")

main()