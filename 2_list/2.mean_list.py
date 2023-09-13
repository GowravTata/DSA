def find_mean(input_list):
    sum = 0
    counter = 0
    for i in input_list:
        counter += 1
        sum += i
    return sum / counter


print(find_mean(list(range(1, 5))))
