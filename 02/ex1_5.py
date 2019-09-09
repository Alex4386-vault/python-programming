'''
    String 
'''

a = 27
b = 419
hell_o = 'Hello'

try:
    print(a + b + hell_o)
except TypeError:
    print("헬-로 타입에러: 자바스크립트랑 헷갈리셨나요? 휴먼?")

# 그러면 당연히 string 으로 캐스팅 하거나
print(str(a+b)+hell_o)

# 콤마 쓰거나
print(a+b, hell_o, sep='')
