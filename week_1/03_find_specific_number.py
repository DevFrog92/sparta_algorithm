input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for num in array: # array의 길이만큼 아래의 연산이 실행된다
        if number == num: # 비교 연산이 1번 실행된다.
            return True  # N*1 = N 만큼 실행되었다.
    else:
        return False


result = is_number_exist(3, input) # 운이 좋으면 0번재 요소가 3이어서 시작과 동시에 끝이 난다.
print(result) # 하지만 운이 안좋으면 마지막 요소가 3이고, 모든 array를 순회해야 끝이 난다.
