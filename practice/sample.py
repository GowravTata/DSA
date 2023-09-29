'''
Given an input string  return an array with common numbers

Example 1:Input: ['1, 4, 7, 10, 11', '1, 3, 4, 11']
Expected Output :  [1,4,11]
'''

input_string = ['1, 4, 7, 10, 11', '1, 3, 4, 11']
 # Expected Output :  [1,4,11]

def commonNumbers(input_string):
    all_numbers = {x:list() for x in range(len(input_string))} 
    start = 0
    while start < len(input_string):
        for i in input_string[start].split(','):
            if i.strip().isdigit():
                all_numbers[start].append(int(i.strip()))
        start += 1
    common_numbers = [numbers for numbers in all_numbers[0] if numbers in all_numbers[1]]
    return common_numbers

# print(commonNumbers(input_string))


def common_numbers(input_string):
    translation_table = str.maketrans('', '', ',')
    new_list = []
    for string in input_string:
        numeric_string = string.translate(translation_table)
        new_list.append([int(i) for i in numeric_string.split()])
    commonNumbers = [numbers for numbers in new_list[0] if numbers in new_list[1]]
    return commonNumbers

# print(common_numbers(sample))


records = [['chi',20],['beta',50],['alpha',50]]
def second_highest(input_list):
    first_least = input_list[0][1]
    second_least = 0
    i=0
    for each in records:
        if each[1] <= first_least:
            first_least = each[1]
        if each[1] > first_least and each[1] <= second_least:
            second_least =each[1]
        i+=1
    for elem in records:
        if elem[1] == second_least:
            print(elem[0])
    return second_least

print(second_highest(records))
