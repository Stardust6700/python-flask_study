#**은 승을 나타내며 다음과 같은 코드에서 2의 3승을 나타낸다
print(2**3)

#//은 몫을 나타내며 다음과 같은 코드에서 12를 5로 나눈 몫을 나타낸다
print(12//5)

#비교연산도 나타낼 수 있으며, 값은 True 또는 False로 출력된다
print(10>3)
print(4>7)
print(3==3)
print(3!=3)

#AND연산은 and 혹은 &로 나타낼 수 있고
#OR연산은 or 혹은 |로 나타낼 수 있다
print((5>3) & (9>6))
print((5>3) | (9<6))

#abs()를 통해 절댓값을 나타낼 수 있다
print(abs(-7))

#pow()를 통해서도 제곱 연산을 나타낼 수 있다
print(pow(3,3))

#max()를 통해 입력값 중 최댓값을 출력할 수 있다
#min()를 통해 입력값 중 최솟값을 출력할 수 있다
print(max(5,12))
print(min(5,12))

#round()를 통해 소수점 아래 값을 반올림 할 수 있다
print(round(3.14))

#from 함수 import *을 통해 제공하는 함수를 이용할 수 있다

#math 함수
from math import *
print(sqrt(36))

#random 함수
from random import *

#다음은 0.0 ~ 1.0에 해당하는 수 중 무작위로 하나를 출력한다
print (random())

#random 뒤에 *를 통해 범위를 변경할 수 있고
#() 뒤에 +를 통해 시작하는 수를 변경할 수 있고
#int를 통해 출력을 정수 형태로 변경할 수 있다
print(random()*10)
print(int(random()*10))
print(int(random()*10+1))

#randrange, randint를 통해 지정한 범위에서의 무작위 정수형 자료의 출력이 가능하다
#randrange는 마지막이 열린 구간이며, randint는 마지막이 닫힌 구간이다
print(randrange(1,45))
print(randint(1,46))