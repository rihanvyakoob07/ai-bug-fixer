def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

# Main program
data = [10, 20, 30, 40, 50]

# Intentional defect: 'dataa' is misspelled
result = calculate_average(dataa)
print("The average is:", result)
