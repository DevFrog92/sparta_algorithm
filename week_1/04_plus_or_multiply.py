array = [0, 3, 5, 6, 1, 2, 4]

def plus_or_multiply(array):
    start = array[0]
    for index in range(1,len(array)): # array의 길이인 N번 연산된다
        if start <= 0 or array[index] <=1: # 비교연산 1회 진행
            # 함정에 대해서 다시 한번 생각해 보자
            start += array[index] # 뎟셈 연산 진행
        else:
            start *= array[index]
    return start

print("정답 = 728 현재 풀이 값 =", plus_or_multiply([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", plus_or_multiply([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", plus_or_multiply([1,1,1,3,3,2,5]))

