## 변환 시점을 알겠는데, 어떻게 구현해야할 지 모르겠어서 힌트를 참조하여 풀이했다.
## 막연하게 변환되는 시점을 잡고, 0을 1로 또는 1을 0으로 바꾸어 주어야 한다는 생각에 갇혔는데,
## 경우에 대해 모두 계산 후 최소값을 찾는다면 숫자를 바꾸지 않더라도 답을 구할 수 있었다.

input_words = '010110'

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    all_zero =0
    all_one = 0
    prev ='0'
    for char in string:
        if char != prev:
            if prev =='0':
                all_zero+=1
            else:
                all_one+=1
            prev = char

    return min(all_one,all_zero)

result = find_count_to_turn_out_to_all_zero_or_all_one(input_words)
print(result)