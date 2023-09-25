input_string = ['1, 4, 7, 10, 11', '1, 3, 4, 11']
 # Expected Output :  [1,4,11]
start = 0
all_numbers = {0: [], 1: []}

common_numbers = []
while start < len(input_string):
    for i in input_string[start].split(','):
        if i.strip().isdigit():
            all_numbers[start].append(int(i.strip()))
    start += 1

common_numbers = [numbers for numbers in all_numbers[0] if numbers in all_numbers[1]]

print(common_numbers)
