# recursive function
def count_down(number):
    # 재귀함수는 반드시 탈출조건이 있어야 한다.
    if number < 0:
        return
    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)