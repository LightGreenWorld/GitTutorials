#튜플 생성
a1 = 10, 20, 30, 40, 50

for value in a1 :
    print('for 1', value)


print('_____________________________________')

#만약 컨테이너가 관리하는 값을 받고 싶지 않다면 변수 대신 _ 를 사용
for _ in a1 :
    print('for 2')

print('_____________________________________')

#range: 시작, 종료, 증가값을 지정하여 그 범위의 값을 가지고 있는 컨테이너타입을 만들 수 있다.
#범위: 0 ~ n-1까지

#범위 0 ~ 10-1
r1= range(10)
print('r1:', tuple(r1))

#범위 2 ~ 13-1
r2= range(2, 13)
print('r2:', tuple(r2))

#거꾸로 범위 > 비어있다
r3= range(13, 2)
print('r3:', tuple(r3))

#증감
#2 ~ 13-1까지 2씩 증가
r4 = range(2, 13, 2)
print('r4:', tuple(r4))

#13 ~ 2까지 2씩 감소
r5 = range(13, 2, -2)
print('r5:', tuple(r5))


#리스트, 튜플을 for으로 순회한다.
list1 = [10, 20, 30, 40, 50]
tuple1 = 10, 20, 30, 40, 50

#enumerate를 사용하면 (인덱스, 값)의 형태로 되어있는 튜플들이 들어있다.
#for문은 수평 나열이 아니라 수직 나열(줄바꿈형태)로 나열

e1 = enumerate(list1)
print('e1:', list(e1))

for e1 in enumerate(list1) :
    print('e1:', list(e1))

for e2 in enumerate(list1) :
    print('e2:', e2)

# enumerate를 활용하여 for문을 사용하면 값 뿐만 아니라 반복회차를 파악할 수 있다.
# for idx, value in enumerate(list1):
#         print('idx:', idx)
#         print('value:', value)

for idx, value in enumerate(list1) :
    print('idx:', idx)
    print('value:', value)

print('--------------------------------------------')
#딕셔너리를 for문으로 운영한다.
dict1 = { 'a1' : 100,
          'a2' : 200,
          'a3' : 300
         }
print(dict1)

# 딕셔너리는 키가 아닌 값이 출력된다.
for value in dict1.values() :
    print('dict1 value:', value)

for key in dict1:
    print('dict1:', dict1[key])

for key, value in dict1.items():
    print('dict1 key:', key)
    print('dict1 value:', value)







