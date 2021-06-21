# Class

# Class는 atrribute와 method를 가진 객체이다.
# 객체는 세상에 존재하는 유일무이한 사물이다.

# 클래스에는 생성자(Constructor)라는게 있는데, 객체를 생성할 때 데이터를 넣어주거나,
# 내부적으로 원하는 행동을 실행하게 할 수 있다. 객체를 생성할 때 사용하는 함수이다.

class Person:
    def __init__(self,param_name):
        self.name = param_name

    def talk(self):
        return f'안녕하세요. 저는 {self.name}입니다.'

## Person 의 ()은 Person 내부의 init을 실행시키는 것이다.
person_1 = Person('유재석')
print(person_1.talk())
person_2 = Person('노홍철')
print(person_2.talk())

## self 란?
## 자기 자신을 넘겨준다.