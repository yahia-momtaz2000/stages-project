# 7. Read File, Store Numbers in a List, and Calculate Sum and Average
def calculate_sum_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file]
            total_sum = sum(numbers)
            average = total_sum / len(numbers)
            return numbers, total_sum, average
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage:
file_name = 'C:\\MY_FILES\\read_data_numbers.txt'  # Replace 'numbers.txt' with your file name
num_list, total, avg = calculate_sum_average(file_name)
print(f"Numbers: {num_list}")
print(f"Total Sum: {total}")
print(f"Average: {avg}")