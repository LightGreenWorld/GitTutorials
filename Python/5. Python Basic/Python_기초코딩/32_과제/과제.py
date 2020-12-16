# 실습 평가 1) 학생의 정보를 입력 받아 출력하는 프로그램을 작성하시오
# 학생 정보는 이름, 나이, 국어점수, 수학점수, 영어점수로 구성된다.
#
# 출력양식)
# 이름 : 홍길동
# 나이 : 30세
# 국어점수 : 80점
# 수학점수 : 70점
# 영어점수 : 60점
# 총점 : 200점
# 평균 : 70점
# ------------------------------
# 이름 : 최길동
# 나이 : 28세
# 국어점수 : 90점
# 영어점수 : 90점
# 수학점수 : 80점
# 총점 : 200점
# 평균 : 60점
# -----------------------------
# 전체 총점 : 1000점
# 전체 평균 : 80점



import pickle

# 학생 정보를 담을 클래스
class student :

    def __init__(self, name, age, kr, en, math, ttl, avg) :
        self.name = name
        self.age = age
        self.kr = kr
        self.en = en
        self.math = math
        self.ttl = ttl
        self.avg = avg

    # 학생 정보를 출력하는 함수
    def showInfo(self) :
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'국어점수 : {self.kr}')
        print(f'영어점수 : {self.en}')
        print(f'수학점수 : {self.math}')
        print(f'총점 : {self.ttl}')
        print(f'평균 : {self.avg}')

# 메뉴를 출력하는 함수
def showMenu() :
    print('-----메뉴-----')
    print('1. 정보입력')
    print('2. 정보출력')
    print('3. 종료')
    a1 = input('메뉴를 선택해주세요: ')
    return int(a1)

#  정보를 입력 받는다.
def input_info() :
    print('-------정보 입력-------')
    name = input('이름: ')
    age = input('나이: ')
    kr = input('국어점수 : ')
    en = input('영어점수 : ')
    math = input('수학점수 : ')
    ttl = input('총점 : ')
    avg = input('평균 : ')

    # 객체 생성
    student = Student(name, age, kr, en, math, ttl, avg)
    #파일에 저장한다.
    with open('student.dat', 'ab') as fp :
        pickle.dump(student, fp)

# 정보 출력
def showAllAnimal() :
    #파일에서 객체들을 가져온다.
    with open('student.dat', 'rb') as fp :
        # try ~ except :
        # try 부분에서 오류가 발생하면 프로그램을 중단시키지 않고
        # except 부분을 수행해준다.
        student_list = []
        try:
            while True :
                a1 = pickle.load(fp)
                student_list.append(a1)
        except :
           pass

    ttl_total = 0

    for obj in animal_list :
        print('--------------------')
        print(f'이름: {obj.name}')
        print(f'나이: {obj.age}살')
        print(f'식사량: {obj.eat}kg')
        # 식사량을 누적한다.
        eat_total = eat_total + int(obj.eat)

    print('------------------------')
    print(f'동물 수: {len(animal_list)}')
    print(f'전체 식사량: {eat_total}')
    print(f'식사량 평균: {eat_total // len(animal_list)}')

if __name__ == '__main__' :
    while True :
        # 메뉴 처리
        menu = showMenu()
        if menu == 1:
            input_info()
        elif menu == 2:
            showAllAnimal()
        elif menu == 3:
            break
        else :
            print('잘못 입력하셨습니다.')

    pass