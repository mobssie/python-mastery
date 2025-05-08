'''
반복문 (for, while)
'''
'''
a=range(1, 10)
print(list(a))
'''
'''
for i in range(10):
    print("hello")

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)

i=1
while i<=10:
    print(i)
    i=i+1


i=10
while i>=1:
    print(i)
    i=i-1
'''
'''
i=1
while True: # 무한반복
    print(i)
    if i==10:
        break
    i+=1
''' 
''' 
for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:
    print(11)
'''
'''
n=input
for i in range(1, n+1):
    print(i)
'''
# 1부터 N까지 홀수 출력하기
'''
n=int(input())
for i in range(1, n+1):
    if i%2==1:
        print(i)
'''
# 1부터 N까지 합을 구하기
'''
m=int(input())
sum=0
for i in range(1, m+1):
    sum=sum+1
print(sum)
'''
# N의 약수 출력하기
'''
n=int(input())
for i in range(1, n+1):
    if n%i==0:
        print(i, end=' ')
'''
