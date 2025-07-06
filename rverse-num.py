def reverse_number(n):
    # Handle negative numbers
    sign = -1 if n < 0 else 1
    n = abs(n)
    
    # Reverse the digits
    reversed_num = int(str(n)[::-1])
    
    return sign * reversed_num

# Get user input
try:
    num = int(input("Enter a number: "))
    result = reverse_number(num)
    print(f"Reversed number: {result}")
except ValueError:
    print("Invalid input! Please enter an integer.")


#########################################
# method-2 without converting to sstring- 
def reverse_number(n): 
    sign = -1 if n<0 else 1
    n = abs(n)
    reversed_num = 0
    while n!=0:
        reversed_num = reversed_num*10 + n%10
        n = n//10
        return sign * reversed_num
    
# Get user input
try:
    num = int(input("Enter a number: "))
    result = reverse_number(num)
    print(f"Reversed number: {result}")
except ValueError:
    print("Invalid input! Please enter an integer.")
