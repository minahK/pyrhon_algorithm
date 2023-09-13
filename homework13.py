#예외처리
#1. 문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생합니다. 예외처리를 통해 에러가 발생하는 PER은 0으로 출력하세요.
per = ["10.31", "", "8.00"]

#for i in per:
#    print(float(i))

#try:
#    print(float(i))
#except ValueError as b:
#    print(b)
# 출력:
# 10.31
# 0
# 8.
#정답이안나옵니다.

#2. 어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생합니다. try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리해보세요.
try:
    print(3/0)
except ZeroDivisionError:
    print("0으로 나누면 안돼요")
