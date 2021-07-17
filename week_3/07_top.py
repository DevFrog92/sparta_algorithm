top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0 for _ in range(len(heights))]
    n = len(heights)
    for i in range(n):
        signal = heights.pop()
        for j in range(len(heights)-1,-1,-1):
            if heights[j] > signal:
                answer[n-1-i] = j+1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!