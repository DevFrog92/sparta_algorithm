shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):

    for menu in shop_orders:
        if menu not in menus:
            return False
    return True

def is_available_to_order_by_binary(menus, orders):
    menus.sort()

    for menu in orders: # N 번의 연산
        state = binary_search(menus,menu) # 최대 log(N)
        if not state:
            return False
    return True

def binary_search(menus,menu):
    left = 0
    right =  len(menus) - 1
    while left < right:
        middle = (left+right) // 2
        if menus[middle] == menu or menus[left] == menu or menus[right] == menu:
            return True
        if menus[middle] > menu:
            right = middle -1
        else:
            left = middle + 1
    return False


result = is_available_to_order(shop_menus, shop_orders)
result2 = is_available_to_order_by_binary(shop_menus, shop_orders) # 시간 복잡도 N*log(N)이 될까??
print(result,result2)
