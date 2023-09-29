def print_func(number):
    if number % 2 != 0 or (number % 2 == 0 and 6 <= number <= 20):
        return 'Weird'
    if (number > 20 and number % 2 == 0) or (2 <= number <= 5 and number % 2 == 0):
        return 'Not Weird'


def swap_case(input_string: str):
    new_string = ''
    for i in input_string:
        if i.isupper():
            new_string += i.lower()
        else:
            new_string += i.upper()
    return new_string


def second_highest(number_list: list):
    number_list.sort()
    return number_list[1]


def some_operations(input_list: list, element: int, index: int):
    input_list.insert(index, element)
    print(input_list)
    input_list.remove(element)
    input_list.append(element)
    input_list.sort()
    input_list.pop()
    return input_list[::-1]


s = 'ABCDCDC'
find = 'CDC'

counter = 0
for i in range(0, len(s)):
    for j in range(1, len(s) + 1):
        if s[i:j] == find:
            counter += 1

magazine = 'give me one grand today night'

note = 'give one grand today'

magazine = magazine.split()
note = note.split()


for i in magazine:
    if i in note:
        note.remove(i)
print(note)


