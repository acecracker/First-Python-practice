# 2-1 숫자 자료형
# print (5)
# print (-10)
# print (3.14)
# print (1000)
# print (5+3)
# print (2*3)
# print (3*(3+1))

# 2-2 문자열 자료형
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)

# 2-3 boolen 자료형
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not(5>10))


# 2-4 변수
# 애완동물을 소개하기 예제
# animal = '강아지'
# name = '깜순이'
# age = 4
# hobby ='애교부리기'
# is_adult = age >= 3

# print('우리집'+animal+'의 이름은' + name + '이예요')
# print(name+'는' +str(age)+'살이며,'+hobby+'를 아주 좋아해요')
# print(name+'는 어른일까요?' +str(is_adult))
# #print(name+'는 어른일까요?')



# 2-5 주석 
# 여러줄의 주석처리는 컨트롤 + 슬래쉬 이다. 
# 동시에 여러줄을 지정해서 주석처리 할때는 컨트롤 키를 누른 상태에서 /를 눌러주면 된다.

# """   또는  '''  동시에 세개의 작은따옴표 or 큰따움표
# 여러줄의 문장을 입력할때 사용하는 구분자 
# 쌍따움표 세개를 통해 여러줄의 문자열을 변수에 입력   '''  여기서부터 ''' 여기까지는 여러줄도 다 주석처리 된다.
# ex)
'''ㅅㄷㄴㅅ'''
"""ㅇㄻㄹㅇㅁㄹ"""
# 위의 경우 다 주석처리 된다.



# 2-6 퀴즈 #1
# 퀴즈) 변수를 이용하여 다음 문장을 출력하시요
# 변수명 
# : station
# 변수값
# : "사당", "신도림","인천공항" 순서대로 입력
# 출력문장 
# : xx행 열차가 들어오고 있습니다.

# station = "사당"
# station1 = "신도림"
# station2 = "인천공항"

# print(station + "행 열차가 들어오고 있습니다.")
# print(station1+ "행 열차가 들어오고 있습니다.")
# print(station2+ "행 열차가 들어오고 있습니다.")




# 3-1 연산자
# print(1+1) #2  더하기
# print(3-2) #1  빼기
# print(5*2) #10  곱하기
# print(6/3) #2  나누기

# print(2**3) # 2^3 = 8
# print(5%3)  # 나머지 구하기 2
# print(10%3) # 1 나머지 구하기
# print(5//3) # 1  몫을 구하기
# print(10//3) # 3  몫을 구하기

# print(10 > 3) # True
# print(4 >= 7) # False
# print(10 < 3) # False
# print(5 <= 5) # True

# print (3 == 3) # True
# print (4 ==2) # False
# print (3 + 4 == 7) # True

# print(1 !=3) #True
# print(not(1 !=3)) #False


# print((3>0) and (3<5)) #True
# print((3>0) & (3<5)) #True

# print((3>0) or (3>5)) #True
# print((3>0) | (3>5)) #True

# print(5 > 4 > 3) #True
# print(5 > 4 > 7) #False



# 3-2 간단한 수식
# print(2+3*4) #14
# print((2+3)*4) #20
# number = 2 + 3 * 4 #14
# print(number)

# number = number +2 #16
# print(number)

# number += 2 # 18
# print(number)

# number *= 2 # 36
# print(number)

# number /= 2 #18
# print(number)

# number -= 2 #16
# print(number)

# number %= 5 #1
# print(number)


# 3-3 숫자처리함수
# print(abs(-5)) #5
# print(pow(4,2)) # 4^2 = 4*4 = 16
# print(max(5,12)) #12
# print(min(5,12)) #5
# print(round(3.14)) #3
# print(round(4.99)) #5

# from math import *
# print(floor(4.99)) #내림 4
# print(ceil(3.14)) # 올림 4
# print(sqrt(16)) #제곱근


# 3-4 랜덤함수
# from random import *
# print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
# print((random() *10))  # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() *10))  # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() *10)+1)  # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() *45)+1)  # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1,46)) # 1~46 미만의 임의의 값 생성
# print(randint(1,45)) # 1~45 이하의 임의의 값 생성


# 3-5 모임날짜 랜덤 지정 예제
# from random import *
# date=randint(4,28)
# print("오프라인 모임날짜는 매월"+str(date)+"일로 선정되었습니다.")


# 4-1 문자열
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요."
# print(sentence2)
# sentence3 = """
# 여러줄의 문장을 입력할때 사용하는 구분자 
# 쌍따움표 세개를 통해 여러줄의 문자열을 변수에 입력
# 여러줄의 주석처리는 컨트롤 + 슬래쉬 이다. ㅎ 
# """
# print(sentence3)


# 4-2 슬라이싱
# jumin = "990120-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) #0부터 2 직전까지 0,1 번째까지 가져옴
# print("월 : " + jumin[2:4]) #2부터 3 까지 
# print("일 : " + jumin[4:6]) #4부터 5 까지
# print("생년월일 : " + jumin[:6]) #처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:14]) #7 부터 14 직전까지
# print("뒤 7자리 : " + jumin[7:]) #7부터 끝까지
# print("뒤 7자리(뒤에부터) : " + jumin[7:]) #위와 같으나 뒤로부터 -1 인덱스로 가져옴 (맨뒤에서부터 7번째까지 뒤로부터 가져옴)


# 4-3  문자열 처리함수 
# # python = "python is Amazing"
# print(python.lower()) # 소문자로 출력
# print(python.upper()) # 대문자로 출력
# print(python[0].islower()) # 0번째 문자가 소문자인지를 참 거짓으로 리턴후 출력
# print(python[0].isupper()) # 0번째 문자가 대문자인지를 참 거짓으로 리턴후 출력
# print(len(python)) # 문자열 길이를 반환
# print(python.replace("Python","Java")) # 일치하는 문자열을 두번째 인자의 문자열로 대체

# index = python.index("n") # 지정한 인자의 위치를 반환
# print(index)  # 위치 확인
# index = python.index("n",index+1)  # 일치하는 n 문자의 다음번의 인덱스를 반환
# print(index)

# print(python.find("n")) # 인덱스 함수와 비슷하게 사용
# print(python.find("Java")) #  찾는 문자열이 없으면 -1을 리턴  (인덱스 함수와 달리 원하는 값이 없으면 -1을 반환 하는 점이 차이점)
# # print(python.index("Java")) # 인덱스 함수는 찾는 문자열이 없으면 오류를 내면서 프로그램이 종료되나, find()함수는 -1을 반환하고 프로그램은 계속 진행됨.
# print("hi")  # 인덱스 함수를 사용시 이부분은 실행되지 못하지만 find() 함수를 사용시 출력됨
# print(python.count('n')) # n 이라는 글자를 몇번 사용했는지 출력 2



# 4-4 문자열 포멧
# #print("a" + "b")
# #print("a","b")

# #방법1 문자열 처리 규칙을 이용
# print("나는 %d살입니다." % 20)  # d는 정수형
# print("나는 %s을 좋아해요" %"파이썬") #s는 문자열을 
# print("Apple 은 %c로 시작해요" %"A") #c는 문자

# print("나는 %s살입니다." % 20)  # 위의 첫번째 정수형 예제를 문자열로 변경 테스트
# print("나는 %s색과 %s색을 좋아해요" %("파란","빨강"))

# #방법2 #포멧함수를 이용
# print("나는 {}살입니다.".format(20))    
# print("나는{}색과{}색을 좋아해요".format("파란","빨간"))
# print("나는{0}색과{1}색을 좋아해요".format("파란","빨간"))
# print("나는{1}색과{0}색을 좋아해요".format("파란","빨간"))

# #방법3 함수와 함께 지역변수를 활용
# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20, ))
# print("나는 {age}살이며, {color}색이랑 {color2}를 좋아해요".format(color="빨간", age=20,color2="노랑" )) # 문자열처리 응용

# #방법4 (python3.6이상)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")



# 4-5 탈출문자 
# \" \' 는 문장에서 탈출문자로 사용
# print("백문이 불여일견  \n 백견이 불여일타")  # 문장에서 줄바꿈 \n
# print("백문이 불여일견  \"백견이\" 불여일타")  # 문장에서 " 를 그냥 쌍따옴표로 인식  탈출문
# print("C\\user\\PythonWorkspace>")  # 문장에서 경로설정등을 사용할때 \ 뒤에 \를 같이 써서 \를 표현
# print("Red Apple\rPine") # \r : 커서를 맨앞으로 이동
# print("Redd\bApple") # \b : 백스페이스 (한 글자 삭제)
# print("Red\tApple") # \t : 탭 (키보드에서 탭을 치는 것과 똑같은 효과로 출력)

# 4-6 퀴즈 #3 
#  사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#  예) http://naver.comb
#  규칙1 : http:// 부분은 제외 => naver.comb
#  규칙2 : cjdma akssksms (.) 이후 부분은 제외 = > naver
#  규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#             |    |    |  (nav)     (5)            (1)           (!)
# url = "http://naver.com"
# my_str = url.replace("http://","")  # 규칙1 해결
# print(my_str)
# my_str = my_str[:my_str.index(".")] # 규칙2 해결  처음부터 . 의 위치까지를 저장
# print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) +"!"
# # print(password)
# print("{0}의 비밀번호는 {1}입니다.".format(url,password))



# 5-1 #리스트[]
# subway1 = 10
# subway2 = 20
# subway3 = 30
# print(subway1,subway2,subway3)  
# subway = [10,20,30]   # 리스트 선언및 초기화  위와 같이 쓰지 않고 리스트를 사용시 
# print(subway)
# subway=["유재석","조세호","박명수"]
# print(subway)
# subway.append("하하")  # 리스트의 뒤에 추가
# print(subway)
# subway.insert(1,"정형돈")  #리스트의 두번째 인덱스에 추가
# print(subway)
# print(subway.pop())  #리스트의 마지막 인덱스에 있는 것을 꺼내서 반환
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.count("유재석"))  # 유재석의 문자열이 몇개 있는지 반환

# #리스트 정렬
# num_list= [5,2,4,3,1] #무작위로 랜덤으로 입력
# num_list.sort()
# print(num_list)  #1,2,3,4,5 로 정렬됨
# num_list.reverse()
# print(num_list)   # 정렬된 순서를 뒤집기 5,4,3,2,1

# #다양한 자료형을 같이 사용도 가능
# mix_list = ["조세호", 20, True]
# print(mix_list)

# #리스트와 리스트끼리의 확장(합치기)도 가능
# num_list.extend(mix_list)
# print(num_list)




# 5-2 사전 or 사물함의 키 의 구현
# cabinet = {3:"유재석",100:"김태호"}
# print(cabinet[3])
# print(cabinet.get(3))
# print(cabinet[100])
# print(cabinet.get(100))

# # print(cabinet[5])  # 캐비넷에 할당된 키값에 해당되는 데이터가 없기 때문에 오류와 함께 종료
# print(cabinet.get(5)) # 반면 get() 없는경우는 none 으로 반납후 함수는 종료되지 않고, 추가로 진행이 가능

# print(cabinet.get(5,"사용가능")) # get() 함수의 특성을 사용하여 케비넷의 데이터가 비어있는지 확인후 응용가능
# print(cabinet.get(5,"can"))   # 위의 사용가능 문구는 ㅅ_용가능 이라고 나오는 데 아래의 영문데이터는 정상으로 나옴...컴파일러의 버그로 보이는데 차후 확인
# print(3 in cabinet) #true    # in 키워드를 사용하여 true 를 받환 받을 수 있음.
# print(5 in cabinet) #frue    # false 반환


# #목욕탕 케비넷 관리 예제 테스트
# cabinet1 = {"a-3":"유재석", "B-100":"김태호"}
# print(cabinet1["a-3"])
# print(cabinet1["B-100"])

# #새손님
# print(cabinet1)
# cabinet1["a-3"] = "김종국"
# cabinet1["c-20"] = "조세호"
# print(cabinet1)

# #간 손님
# del cabinet1["a-3"]
# print(cabinet1)


# # key 들만 출력
# print(cabinet1.keys())

# # value 들만 출력
# print(cabinet1.values())

# #key, value 쌍으로 출력
# print(cabinet1.items())

# #목욕탕 폐점시
# cabinet1.clear()  # 케비넷 리스트트의 키와 값을 다 지운다. 
# print(cabinet1)



#  5-3  튜플 실습    리스트와는 달리 데이터 요소를 추가할 수 없다.  때문에 리스트 보다 불편하지만, 속도가 빠르다.
# menu = ("돈까스","치즈까스")
# print(menu[0])
# print(menu[1])
# name = "김종국" 
# age = 20
# hobby = "코딩"
# (name, age, hobby) = ("김종국", 20,"코딩")
# print(name, age, hobby)




# 5-4 집합(set)  중복 안됨, 순서 없음
# print("집합 set 예제 테스트")
# #첫번째 예제
# my_set = {1,2,3,3,3}  #중복된 데이터가 들어가 있음.
# print(my_set)  # set 는 중복 데이터를 허용하지 않기 때문에 출력해 보면 중복된 3이 없어지고 1,2,3 만 출력됨

# #집합(set)에 대한 두번째 예제
# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

# #교집합 (java 와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))   # intersecton. 동일하게 교집합 값을 뽑을 수 있다. 

# #합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))   # 합집합 union 을 쓸 수도 있음.

# #차집합 (java 할 수 있지만 python 은 할줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))  # difference  자바에서 파이썬을 할줄 모르는 사람을 뻄

# # python 을 할 줄 아는 사람이 늘어남
# python.add("김태호")    # 값을 늘리거나, ...
# print(python)

# # java를 잊어버렸어요. 
# java.remove("김태호")  #값을 뺄 수 있다. 
# print(java)




# 5-5  자료구조의 변경 예제
# print("자료구조의 변경 예제")
# #자료구조의 변경
# menu = {"커피","우유","주스"}    # 집합(set)에 데이터를 저장을 해 놓고...
# print(menu, type(menu))         # 데이터 확인을 해보면  set 으로 나옴을 확인 할 수 있음. 

# menu = list(menu)              # set 데이터를 list()로 감싸서 변환 할 수 있다. 
# print(menu, type(menu))       #확인해 보면 list 로 바뀐걸 확인 할 수 있다. 

# menu = tuple(menu)             # list 로 바뀐 menu 데이터를 tuple 로 바꿀 수도 있다. 
# print(menu, type(menu))       #확인해 보면 tuple 로 바뀐걸 확인 할 수 있다. 

# menu = set(menu)           # 다시 원래 대로 되돌려봄.
# print(menu, type(menu))




# 5-6 #퀴즈4 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다. 

# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 
# 추첨 프로그램을 작성하시ㅛ.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 를 활용

# (출력예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1 
# 커피 당첨자 : [2,3,4]
# --- 축하합니다. ---

#(활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)   # 리스트의 순서를 무작위로 섞어줌
# print(lst)     
# print(sample(lst,1))   # 리스트중 1개를 추출해줌

#퀴즈 테스트 풀어보았으나 lst1.rmove 에서 리스트로 형변환 하는 부분에서 실패, lis1.remove()
# lst1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(lst1)
# print("퀴즈테스트")
# list_first=sample(lst1,1)
# print(list_first)
# # lst1.remove(list(list_first))
# lst1.remove()
# print(sample(lst1,3))
# -------------여기까지 내가 만들었던 실패작

# users = range(1,21)
# print(users)
# users = list(users)
# shuffle(users)
# print(users)

# winners = sample(users,4) # 4명중에서 1명은 치킨, 1명은 커피
# print ("----당첨자 발표 -----")
# print ("치킨 당첨자 : {0}".format(winners[0]))
# print ("커피당첨자 : {0}".format(winners[1:]))
# print ("축하합니다.")


# 6-1 if 
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요.")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지마세요")
# elif 10<=temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp <10:
#     print("외투를 챙기세요")
# else:
#     print("외투를 챙기세요")
 



# 6-2 For 
# for waiting_no in range(1,6): #0,1,2,3,4
#     print("대기번호 : {0}".format(waiting_no))


# starbucks =["아이언맨","토르", "아이엠 그루트"]    
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))




# 6-3 while
# customer = '토르'
# index = 5
# while index >= 1 :
#     print("{0}, 커피가 준비되었습니다.{1}번남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기되었습니다.")



# 내가 만들어본 while문 테스트
# customer = "아이언맨"
# index = 1
# roof = True
# while roof:
#     print("{0}님 커피가 준비되었습니다.  호출 {1}회 ".format(customer,index))
#     index += 1
#     if index == 1000 : roof = False
#     print("루프가 종료되었습니다.")



# while 예제
# customer "토르"
# person = "Unknow"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(cstom))




# 6-4 continue, break 
# absent = [2,5] # 결석
# no_book = [7]  # 책을 깜빡했음
# for student in range(1,11):  #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))
#         break
#     print("{0} 책을 읽어봐".format(student))




# 6-5 한줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101,102,103,104.
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)


# 학생 이름을 길이로 변환
# students = ["Iron man","Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)


# 학생 이름을 대문자로 변환
# students = ["Iron man","Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)



# 6-6  퀴즈 #5 
# Cocoa 택시회사의 매칭 서비스 루틴 만들기
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
#조건1 : 승객별 운행 소요 시간은 5분~ 50분 사이의 난수로 정해집니다.
#조건2 : 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다. 

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 16분)
# 총 탑승 승객 : 2분

# from random import *

# cnt = 0  #총 탑승 승객수
# for i in range(1,51): # 1~50 이라는 숫자
#     time = randrange(5,51)  # 5분 ~ 50분 소요시간
#     if 5 <= time <=15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분".format(i,time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i,time))
# print("총 탑승 승객 : {0}분".format(cnt))




# 7-1 함수
# from warnings import formatwarning


# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# 7-2 반환값
# def deposit(balance, money): #입금
#     print("입금이 완료되었습니다. 잔액은{0}원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): #출금
#     if balance >= money : #잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): #저녁에 출금
#     commission =100 # 수수료 100원
#     return commission, balance - money - commission


# balance = 0 # 잔액

# balance = deposit(balance, 1000) # 입금
# #balance = withdraw(balance, 2000)
# #balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은{1}원입니다.".format(commission,balance))


# 7-3 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬") # 유재석씨(20세)의 주 사용 언어는 파이썬
# profile("김태호", 25, "자바") # 김태호씨(25세)의 주 사용 언어는 자바

# def profile(name, age=17, main_lang="파이썬"): # 전달값을 따로 받지 않을때 기본으로 사용할 값
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
        
# profile("유재석")
# profile("김태호")


# # 7-4 키워드 인자
# def profile(name, age, main_lang): # 키워드 인자 : name, age, main_lang
#     print(name, age, main_lang)

# # profile("유재석", 20, "파이썬")
# # profile("김태호", 25, "자바")

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")


#7-5 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # 문장 출력 후 줄바꿈 대신 띄어쓰기
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# def profile(name, age, *language): # 언어 정보를 전달하고 싶은 갯수 만큼 전달 가능    
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    
#     # print(type(language)) # tuple
#     for lang in language:
#         print(lang, end=" ") # 언어들을 모두 한 줄에 표시
#     print() # 줄바꿈 목적


# #7-6 전역변수 지역변수 
# gun = 10 # 총 10자루  전역변수

# def checkpoint(soldiers): # 경계근무 나가는 군인 수
#     # gun = 20   # 함수내 지역변수
#     global gun   # 함수네에서 전역변수를 쓸 경우
#     gun = gun - soldiers # 전체 총에서 경계근무 나가는 군인 수만큼 뺀 잔여 총
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun,soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# gun = checkpoint_ret(gun, 2)
# print("남은 총:{0}".format(gun))

# print("전체 총 : {0}".format(gun)) # 10 자루
# checkpoint(2) # 2명이 경계 근무 출발
# print("남은 총 : {0}".format(gun)) # 몇 자루?


# 퀴즈)_ 표준 체중을 구하는 프로그램을 작성하시오
#  * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남자 : 키(m) X 키(m) X 22
# 여자 : 키(m) X 키(m) X 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
#(출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height, gender): # 키 m 단위(실수), 성별 "남자" / "여자"
#     if gender=="남자":
#         return height * height * 22
#     else:
#         return height * height *21

# height = 175 # cm 단위
# gender ="남자" 
# weight = round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))



# 8-1 표준 입출력
# import sys
# print("Python","Java", sep=",",end="?")    # sep 는 "Python"요부분"Java" 부분의 정의, end는 끝부분을 줄바꿈 대신 지정하는 값으로 정의
# print("무엇이 더 재밌을까요?")

# print("Python","Java", file=sys.stdout)   
# print("Python","Java", file=sys.stderr)   # 비주얼 스튜디오 코드에서는 정상적으로 나오는 것으로 보이지만, 일반 상황에서는 에러 로그에 기록됨

#시험성적
# scores = {"수학":0,"영어":50,"코딩":100}
# for subject, scores in scores.items():
#     #print(subject, scores)
#     print(subject.ljust(8), str(scores).rjust(4), sep=":")


# 은행 대기순번표 
# #001,002,003,...
# for num in range(1,21):
#     print("대기번호 :" +str(num).zfill(3))   # .zfill(3) 메소드는 자리공간 3자리를 확보하고 자리에 데이터가 없는 경우 0으로 채운다.


# 사용자 표준 입력과 코딩 입력시 주의사항 
# answer = input("아무값이나 입력하세요:")   # 사용잡 입력을 받게 되면 항상 문자(열)로 입력을 받게 된다는 점 주의, (숫자로 변경 필요시 주의)
# # answer = 10   # 사용자 입력이 아닌 코딩시 입력시에는 int 형으로 입력이 된다는 점에 주의
# print(type(answer))  # 변수의 타입을 확인하고 싶을 때 .type()메소드
# print("입력하신 값은"+answer + "입니다.")



# 8-2 다양한 출력포맷

# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# #양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500)) 
# print("{0: >+10}".format(-500))

# #왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_>10}".format(-500))

# #3자리마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))

# #3자리마다 콤마를 찍어주기, +-부호도 붙이기
# print("{0:+,}".format(100000000000))
# print("{0:+,}".format(-100000000000))

#3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# print("{0:^<+30,}".format(-100000000000)) #(좌측정렬에 30자리공백은 ^표 처리)
# print("{0:*>+30,}".format(-100000000000)) #(우측정렬에 30자리공백은 *표처리)

# #소수점 출력
# print("{0:f}".format(5/3))  # 5/3  3분의5를 소수점으로 출력

# #소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))  


# 8-3 파일 입출력
# 파일을 열고 내용쓰기
# score_file = open("score.txt", "w", encoding="utf8")  # "w" 용도로 열경우는 쓰기 용도로 여는 것임
# print("수학:0", file=score_file)   # print() 사용시 자동으로 줄바꿈이 된다.
# print("영어:50", file=score_file)  
# score_file.close()   # 파일을 열었으면 필히 닫아준다.

# 기존파일을 열고 내용 추가 하기
# score_file = open("score.txt", "a", encoding="utf8")    # "a" 로 여는 것은 append 로 여는 것임 "w"로 열경우 파일이 있으므로 덮어쓰기됨
# score_file.write("과학 : 80")      #
# score_file.write("\n코딩 : 100")   #print() 메소드의 경우 줄바꿈이 들어있으나, write()메소드는 줄바꿈이 기본이 아니므로 명시적으로 \n 줄바꿈 넣어주기
# print("\ntest:50", file=score_file)   #위에서 줄바꿈이 안되었기 때문에 줄바꿈을 넣어주고 테스트 해봄
# print("test:1", file=score_file)      # print()는 줄 바꿈이 되기 때문에 줄바꿈이 실행되어 저장됨
# print("test:2", file=score_file)
# print("test:3", file=score_file)
# score_file.close()     #파일사용후 닫아주기는 꼭 잊지 말자

# 파일을 열고 읽기
# 1 한번에 다 읽어서 보여주는 방법
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())    # 한번에 읽어서 보여주기
# score_file.close

# 한줄씩 읽어서 처리하기 (아래의 경우는 읽어야 하는 양을 알아서 간단하나..)
# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동 / (end="") end옵션을 빼면 줄바꿈을 해서 표기
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 한줄씩 읽어서 처리하나 파일이 총 몇줄인지 모를 경우 while 루푸문을 이용해서 처리
# score_file = open("score.txt","r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     # print(line,)       # 줄바꿈을 하려는 경우 end 사용하지 않음
#     print(line, end="")  # 줄바꿈을 하지 않으려는 경우 end="" 추가
# score_file.close()


# 리스트 형태로 저장해서 출력하기
# score_file = open("score.txt","r", encoding="utf8")
# lines = score_file.readlines()  #  list 형태로 저장    .readline 이 아닌 .readlins 로 메소드를 사용 (모든 라인을 가지고 와서 lines list 에 저장)
# for line in lines:    # lines 리스트에서 한줄씩 가져와서 출력해주기
#     print(line, end="")  #줄바꿈을 하지 않으려는 경우 end
# score_file.close()


# 8-4 picke  피클 라이브러리 (프로그램에서 우리가 사용하는 데이터를 파일 형태로 주고 받는 방식)
# import pickle
# profile_file = open("profile.pickle", "wb")  # w->쓰기형태로 열기 b-> 바이너리로 사용 (피클은 항상 바이너리로 사용)
# profile ={"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 에 있는 정보를 file 에 저장
# profile_file.close()

# pickle 파일 데이터 가져와서 출력하기
# import pickle
# profile_file = open("profile.pickle", "rb")  # 바이너리 데이터 읽기로 열기 rb
# profile = pickle.load(profile_file)  # file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()


# 8-5 with 사용하기
# import pickle
# with open("profile.pickle", "rb") as profile_file:  # profile_file 이라는 변수에 profile.pickle 파일을 바이너리 읽기로 열어서 넣어줌.
#     print(pickle.load(profile_file))                # with 를 사용시 파일을 닫아줄 필요가 없어 좀더 편리하다.

# pickle 을 사용하지 않고 일반 파일을 with 로 쓰고 읽기
# with open("study.txt", "w", encoding="utf8") as study_file: # study_file 변수에 study.txt 파일 열어서 개체를 준비시킴 (파일열고 쓸 준비)
#     study_file.write("파이썬을 열심히 공부하고 있어요.")  # 열린변수 study_file 변수에 데이터 쓰기  (파일을 따로 닫지 않아도 됨)

# 읽기
# with open("study.txt","r", encoding="utf8") as study_file:   # 읽기 모드로 study.txt 파일을 열어서 study_file 에 담기
#     print(study_file.read())             # 담은 데이터를 읽어서 print()  마찬가지로 파일을 따로 닫을 필요가 없어서 달랑 두줄이면 파일처리 가능


# 8-6  퀴즈 파일처리
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
#  - X주차 주간보고-
# 부서 :
# 이름 :
# 업무요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt', '2주차.txt',... 와 같이 만듭니다.
# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0}주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무요약 :")



# 9-1 클래스  
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))


# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


# # 공격 함수
# def attack(name, location, damage):
# 	print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시" , damage) # 마린 공격 명령
# attack(tank_name, "1시" , tank_damage) # 탱크 공격 명령


# 탱크2 새로 추가
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# # 공격 함수
# def attack(name, location, damage):
# 	print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시" , damage) # 마린 공격 명령
# attack(tank_name, "1시" , tank_damage) # 탱크 공격 명령
# attack(tank2_name, "1시" , tank2_damage) # 탱크2 공격 명령


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 멤버변수 name 에 전달값 name 저장
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # 마린1 생성. 전달값으로 name, hp, damage 를 전달
marine2 = Unit("마린", 40, 5) # 마린2 생성
tank = Unit("탱크", 150, 35) # 탱크 생성