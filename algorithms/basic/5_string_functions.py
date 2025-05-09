'''
문자열과 내장함수
'''
msg="It is Time"
print(msg.upper()) # msg 원본데이터는 그대로 있음
print(msg.lower())
tmp=msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))
print(msg[:2])
print(msg[3:5])
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=' ')
print()
for x in msg:
    print(x, end=' ')

print()

# 대문자만 찾아서 출력
for x in msg:
    if x.isupper():
        print(x, end=' ')
print()


# 소문자만 찾아서 출력
for x in msg:
    if x.islower():
        print(x, end=' ')
print()

# 알파벳만 찾아서 출력
for x in msg:
    if x.isalpha():
        print(x, end=' ')
print()

# 아스키넘버
tmp='AZaz'
for x in tmp:
    print(ord(x))
print()

num=65
print(chr(num))