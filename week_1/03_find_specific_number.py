input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for num in array:
        if number == num:
            return True
    else:
        return False


result = is_number_exist(3, input)
print(result)

n = 9217
array = []
while n>0:
    array = [n%10] + array
    n //= 10

a = [1,2,3,4]
a.insert(0,10)
print(type(int(''.join(map(str,a)))))
print(array)

a = 157.153//1
b = 157.153%1
array = []
array2 = []
print(a,b)
while a >0:
    array =[a%10] + array
    a //= 10
count = 1
bb = 10

print(''+1)