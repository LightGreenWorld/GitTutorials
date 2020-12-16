#기본/단일 조건문
x= 95

if x >= 90 :
    print("축하합니다")
    print("당신은 합격입니다.")


#if ~ elif ~ else 구조
x= 85

if x >= 90 :
    print("Very good")
elif (x > 80) and (x < 90) :
    print("Good")
else :
    print("Bad")

for a in [0,1,2,3,4,5] :
    print(a)

for myfriends in ["현선", "현준", "연재", "소영"] :
    print(myfriends)

myfriends1 = ["현선", "현준", "연재", "소영"]
for myfriends11 in myfriends1 :
    print(myfriends11)

#while문: 조건에 만족하는 동안 계속 반복하는 반복문

a1 = 0

while a1 < 10 :
    print("while:", a1)
    break