input_number = 20

def find_prime_list_under_number(number):
    all_numbers = [True]*(number+1)
    answer = []

    for index in range(2,number+1):
        if all_numbers[index]:
            for index2 in range(2,number//index+1):
                all_numbers[index*index2] = False
    for index,num in enumerate(all_numbers):
        if index > 1 and num:
            answer.append(index)

    return answer

result = find_prime_list_under_number(input_number)
print(result)