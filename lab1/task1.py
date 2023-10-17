numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total_sum = 0
missing_element_index = None

for i, number in enumerate(numbers):
    if number is not None:
        total_sum += number
    else:
        missing_element_index = i

numbers[missing_element_index] = total_sum / (len(numbers))

print("Измененный список:", numbers)
