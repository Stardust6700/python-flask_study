#자료형(숫자형, 문자열, boolean)

#숫자형

print(5), print(-10), print(3.14)
	#정수 뿐 아니라 음수, 실수도 출력 가능

print(5+3), print(2*8), print(3*(3+1))
	#연산도 처리하여 출력

#문자형

print('풍선'), print("나비")
	#따옴표나 큰따옴표로 문자열을 출력 가능

print('ㅋㅋㅋ'), print('ㅋ'*3)
	#초성을 출력하거나 연산도 가능

#boolean

print(5 < 10), print(5 > 10)
	#True 또는 False로 출력 가능
	
print(True), print(False)
	#True 또는 False를 바로 출력 가능
	
print(not True), print(not (5 > 10))
	#부정하여 출력이 가능하며, 연산값도 부정하여 출력 가능


#변수

animal = "강아지"
name = "티나"
age = 7
is_adult = age >= 7

print("우리 " + animal + "의 이름은 " + name )
print("티나의 나이는 " +str(age)+ "살이에요")
print(name+"는 어른인가요?" ,is_adult,)

	#변수는 값을 저장하는 어떤 공간
	#+ 변수 이름 +로 입력이 가능
	#정수형이나 boolean 변수는 입력 시 str()을 필요로 함
	#+ 대신 , 를 통해 입력이 가능하며, ,를 사용하면
	#정수형이나 boolean 변수에 str을 쓸 필요가 없어지며
	#자동으로 공백이 하나 들어가게 됨

#주석

	# 프로그램 코드 내에는 작성이 되어있지만, 실행 시 출력이 되지않게 함
	# 문장에 앞에 #을 사용하거나 여러 문장의 앞뒤에 '를 3개씩 작성하여 주석처리 가능함
	# 여러 문장을 지정 후 ctrl + / 키를 이용해서 한 번에 주석처리 가능함
