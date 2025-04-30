# Step 1: Define a recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive call

# Step 2: Call the function with a sample number
sample_number = 5
result = factorial(sample_number)

# Step 3: Print the output
print('The factorial of ',sample_number,' is ',result)
