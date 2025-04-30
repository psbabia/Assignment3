import math

# Step 1: Ask the user to enter a number
number = float(input("Enter a number: "))

# Step 2: Perform calculations using the math module
sqrt_result = math.sqrt(number)
log_result = math.log(number)         # Natural logarithm (base e)
sine_result = math.sin(number)        # Sine of the number (in radians)

# Step 3: Display the results
print('Results for the number ',number)
print('Square Root: ',sqrt_result)
print('Natural Logarithm (ln): ',log_result)
print('Sine (in radians): ',sine_result)
