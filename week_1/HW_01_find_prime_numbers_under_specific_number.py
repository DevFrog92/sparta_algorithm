input_number = 20

# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.

# 소수의 특징
## 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
## N이 N의 제곱근 보다 크지 않은 어떤 소수로도 나눠지지 않는다.
## 수가 수를 나누면 몱이 발생하는데, 몫과 나누는 수 둘 중 하나는 반드시
## N의 제곱근 이하이다.
# def find_prime_list_under_number(number):
#     all_numbers = [True]*(number+1)
#     answer = []
#
#     for index in range(2,number+1): # n <- 2 ~ num
#         # 소수인지 아닌지 판별해야 한다.
#         if all_numbers[index]:
#             for index2 in range(2,number//index+1):
#                 all_numbers[index*index2] = False
#     for index,num in enumerate(all_numbers):
#         if index > 1 and num:
#             answer.append(index)
#
#     return answer

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2,number+1):
        for i in prime_list:
            if n%i == 0 and i*i <= number:
                break
        else:
            prime_list.append(n)
    return prime_list

result = find_prime_list_under_number(input_number)
print(result)
'''
input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1): # n 의 범위 : 2부터 number 까지
        # 만약 n =19
        # i = 2, 3, 4, 5, ... , 18
        # 여기서 2와 3일때 나누어 떨어진다는 것은 2와 3의 합성수로도 나누어진다는 것이다.
        # 연산량을 증
        for i in range(2, n): #  i 의 범위 : 2부터 n-1까지
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)

'''


'''
input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list: # 계속해서 추가해준 소수의 리스트를 활용해서 비교한다.
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
'''

