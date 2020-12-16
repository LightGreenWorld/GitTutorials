a = 'Enjoy'
b = ' python'
c = a + b
print(c)

print(a * 3)

student1 = [90, '95', 85, 80]
print(student1)

print(student1[0])
print(student1[1])
print(student1[2])
print(student1[3])
print(student1[-1])
print(student1[-2])


student1[1] = 2000
print(student1)

myfriends = ['현준', '메리', '현선', '연재']
print(myfriends)

mixedList = [0, 2, 3.14, 'python', 'program', True, myfriends]
print(mixedList)

list_con1 = [1,2,3,4]
list_con2 = [5,6,7,8]
list_con = list_con1 + list_con2
print(list_con)

list_con1 = [1,2,3,4]
list_con3 = list_con1 * 3
print(list_con3)

list_data = [1,2,3,4,5,6,7,8,9]
print(list_data)
print(list_data[0:3])
print(list_data[1:3])
print(list_data[:3])
print(list_data[::3])
print(list_data[3:])

print(list_data)
del list_data[6]
print(list_data)

list_data1 = [1,2,3,4,5]
print( 5 in list_data1)
print( 9 in list_data1)


myfriends = ['현준', '메리', '현선', '연재']
myfriends.append('뭘')
print(myfriends)

myfriends = ['현준', '메리', '현선', '연재']
myfriends.insert(2, '뭘')
print(myfriends)

myfriends = ['현준', '메리', '현선', '연재']
myfriends.extend([2, '뭘'])
print(myfriends)

myfriends = ['현준', '메리', '현선', '현준', '연재']
myfriends.remove('현준')
print(myfriends)

myfriends = ['현준', '메리', '현선', '연재']
popmyfriends = myfriends.pop()
print(popmyfriends, myfriends)

myfriends = ['현준', '메리', '현선', '현준', '연재']
indexmyfriends = myfriends.index('현준')
print(indexmyfriends)

myfriends = ['현준', '메리', '현선', '현준', '연재']
countmyfriends = myfriends.count('현준')
print(countmyfriends)

myfriends = ['현준', '메리', '현선', '현준', '연재']
myfriends.sort()
print(myfriends)

myfriends = ['현준', '메리', '현선', '현준', '연재']
myfriends.sort()
print('오름차순 정렬:', myfriends)

myfriends = ['현준', '메리', '현선', '현준', '연재']
myfriends.sort(reverse=True)
print('내림차순 정렬:', myfriends)

tuple1 = (1, 2, 3, 4)
print(tuple1)

print(tuple1[2])

tuple3 = (1)
print(tuple3)

#tuple5 = (1, 2, 3, 4)
#tuple5.sort(reverse=True)
#print('내림차순 정렬:', tuple5)

set1 = {1, 2, 3}
set1a = {3,1,2,3,3,3,3}

print(set1)
print(set1a)

A = {1,2,3,4,5}
B = {4,5,6,7,8,9,10}
st1 = A.intersection(B)
st11 = A & B
print(st1)
print(st11)

st2 = A.union(B)
st22 = A|B
print(st2)
print(st22)

st3 = A.difference(B)
st33 = A - B
print(st3)
print(st33)

a =  [1,2,3,4,5]
print(type(a))

b = tuple(a)
print(b)
print(type(b))

c = set(b)
print(c)
print(type(c))

d = list(c)
print(d)
print(type(d))

country_capital = {"영국":"런던", "프랑스":"파리", "스위스":"베른", "호주":"멜버른", "덴마크":"코펜하겐"}
print(country_capital)

print(country_capital["영국"])

country_capital["독일"] = "베를린"
print(country_capital)

country_capital["한국"] = "서울"
print(country_capital)

del country_capital["한국"]
print(country_capital)

asd=country_capital.pop("베트남","없음")
print(asd)
print(country_capital)

