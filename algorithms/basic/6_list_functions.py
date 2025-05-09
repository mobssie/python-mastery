'''
리스트와 내장함수 예제
'''
import random as r

# 빈 리스트 생성 (두 가지 방식)
a = []        # 첫 번째 방식
print(a)
b = list()    # 두 번째 방식
print(b)

# 리스트 기본 생성 및 사용
a = [1, 2]
print(a[0])   # 첫 번째 요소 출력

# 1부터 10까지 리스트 생성
b = list(range(1, 11))
print(b)

# 리스트 합치기
c = a + b
print(c)

# 리스트에 값 추가 (append)
a.append(10)
print(a)

# 3번 인덱스에 7 삽입 (insert)
a.insert(3, 7)
print(a)

# 리스트에서 마지막 값 제거 (pop)
c.pop()
print(c)

# 지정된 인덱스 값 제거 (pop)
c.pop(1)
print(c)

# 지정된 값 제거 (remove)
c.remove(1)
print(c)

# 특정 값의 인덱스 찾기 (index)
print(c.index(5))

# 리스트의 값 합, 최대값, 최소값
c = list(range(1, 11))
print(c)
print(sum(c))  # 합계
print(max(c))  # 최대값
print(min(c))  # 최소값
print(min(5, 7)) # 두 수 중 최소값

# 리스트 섞기 (shuffle) - 무작위 정렬
r.shuffle(c)
print(c)

# 리스트 정렬 (오름차순/내림차순)
c.sort(reverse=True)
print(c)
c.sort()
print(c)

# 리스트 전체 삭제 (clear)
c.clear()
print(c)

# 리스트 슬라이싱 예제
a = [23, 45, 51, 24, 43]
print(a[:3])   # 인덱스 0부터 2까지 (3 미포함)
print(a[1:4])  # 인덱스 1부터 3까지 (4 미포함)
print(len(a))  # 리스트 길이

# 리스트 값 순차적으로 출력
for i in range(len(a)):
    print(a[i], end=' ')
print()

# 리스트 값 중 홀수만 출력
for x in a:
    if x % 2 == 1:
        print(x, end=' ')
print()

# enumerate 사용 (인덱스와 값 동시 출력)
for m in enumerate(a):
    print('enumerate::', m, m[0], m[1])

# 튜플 생성 (리스트와 다르게 값 변경 불가)
b = (1, 2, 3, 4, 5)
print(b[0])
# b[0] = 7  # 오류 발생 (튜플은 값 변경 불가)

# enumerate에서 인덱스와 값 분리하여 출력
for index, value in enumerate(a):
    print(index, value)
print()

# all() - 모든 값이 조건을 만족할 때 (모두 60보다 작으면)
if all(60 > x for x in a):
    print("YES")
else:
    print("NO")

# any() - 하나라도 조건을 만족할 때 (하나라도 15보다 작으면)
if any(15 > x for x in a):
    print("YES")
else:
    print("NO")
