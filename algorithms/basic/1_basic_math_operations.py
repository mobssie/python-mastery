a=1
_A=4
print(a, _A)
'''
a, b=input("숫자를 입력하세요: ").split()
print(a+b)
'''
'''
a, b=input("숫자를 입력하세요: ").split()
a=int(a)
b=int(b)
print(a+b)
'''
# 사용자로부터 두 개의 숫자를 입력받아 a, b 변수에 정수(int)로 저장
a, b = map(int, input("숫자를 입력하세요 : ").split())

# 두 숫자의 합 출력
print(a + b)  # 덧셈

# 두 숫자의 차 출력
print(a - b)  # 뺄셈

# 두 숫자의 곱 출력
print(a * b)  # 곱셈

# 두 숫자의 나눗셈 (소수점까지 결과 출력)
print(a / b)  # 나눗셈 (실수)

# 두 숫자의 몫 연산 (소수점 없이 정수로 나옴)
print(a // b)  # 몫 연산 (정수)

# 두 숫자의 나머지 연산 (정수)
print(a % b)  # 나머지 (modulus)

# 두 숫자의 거듭제곱 연산 (a를 b번 곱함)
print(a ** b)  # 거듭제곱 (exponentiation)

a = 4.3   # 실수 (float)
b = 5     # 정수 (int)
c = a + b # 실수 (float)
print(c)         # 출력: 9.3
print(type(c))   # 출력: <class 'float'>