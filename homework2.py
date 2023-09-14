# 1. 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장하고 출력하세요. (순위 정보는 저장하지 않습니다.)

movie_rank = [ "범죄도시" , "닥터스트레인지" , "인어공주 "]
print(movie_rank)
#  2. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있어요. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하고 출력하세요.

movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1 ,"슈퍼맨")
print(movie_rank)

# 3. movie_rank2 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하세요.

movie_rank2 = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank2[2]
del movie_rank2[2]
print(movie_rank2)

# 4. lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어 출력하세요.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 5. 다음 리스트에 저장된 데이터의 개수를 화면에 구하세요.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 6. price 변수에는 날짜와 종가 정보가 저장돼 있습니다. 날짜 정보를 제외하고 가격 정보만을 출력하세요. (힌트 : 슬라이싱 활용!!
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 7. 내장 함수를 사용하여 리스트의 내용을 역 방향으로 출력하세요.
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)

# 8.다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하여 출력하세요.\
ticker = "btc_krw"
print(ticker.upper())

# 9. 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하여 출력하세요.
ticker = "BTC_KRW"
print(ticker.lower())

# 10. 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠 출력하세요.
a = "hello world"
print(a.split())

# 11. 다음과 같은 문자열이 있을 때 “,”을 기준으로 문자열을 나눠 출력하세요.
b = "hello,world"
print(b.split(","))

# 12. 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
print(date.split("-"))

# 13. 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "
print(data.rstrip())

# 14. interest 리스트에는 아래의 데이터가 바인딩되어 있습니다.join() 함수를 사용해서 interest 리스트를 아래와 같이 화면에 출력하세요.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

# 15. 리스트에 있는 값을 오름차순으로 정렬하세요
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# 16. 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "철수" 
age1 = 10
name2 = "철희"
age2 = 13
print("이름 :{0} 나이 :{1}" .format(name1,age1))
print("이름 :{0} 나이 :{1}" .format(name2,age2))

# 17. 16번 문제를 f-문자열 포매팅(f(’’)) 을 사용해서 다시 출력하세요
print(f" 이름: {name1} 나이:{age1}")
print(f" 이름: {name2} 나이:{age2}")

# 18 . 삼성전자의 상장주식수가 다음과 같습니다. 콤마(,)를 제거한 후 이를 정수 타입으로 변환해보세요. (힌트: replace() 사용)
samsung = "5,969,782,550"
#모르겠는 이유 : replace라는 게 문자열 바꾸기라고 배웠는데 문자열을 저렇게 바꾸는 방법을 모르겠습니다

# 19. 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 f-문자열 포매팅(f(’’))을 사용해서 다음과 같이 출력해보세요
name = "민수"
math = 92
english = 87
print( f"나의 이름은{name}입니다. 나의 수학 점수는 {math}점이고 영어 점수는 {english}점 입니다.")

# 20. 변수에 다음과 같은 문자열이 있습니다.  해당 문자열에 문자 (t,T)의 개수를 출력하세요
longT = "Tom, the talented tenor, traveled to Tokyo to taste traditional takoyaki, the tasty treat that thrilled his taste buds."
print(longT.count('t') + longT.count('T'))

# 1. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
print(string.replace("a","A"))

# 2. 아래 문자열의 좌우 공백을 제거해보세요.
data = "  조이   "
print(data.strip())

# 3. 아래의 문자열을 시계방향으로 90도 돌려서 출력하세요.
sample = "abcde"
print(sample[0])
print(sample[1])
print(sample[2])
print(sample[3])
print(sample[4])

# 4. 주어진 문자열에서 모음(a, e, i, o, u)의 개수를 세는 함수를 작성하세요.
text = "Python programming is fun and educational"
print(text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u'))

# 5. 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하세요
a = 12
b = 23
print( "{0} + {1} = 35 " .format(a , b))

# 6. 문자열 my_string, overwrite_string과 정수 s가 주어집니다. 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 출력하세요
# 1
my_string = "He11oWor1d"
overwrite_string = "lloWorl"
s = 2

print(my_string[:2]+ overwrite_string[:])

# 2
my_string = "Program29b8UYP"
overwrite_string = "merS123"
s = 7

print(my_string[:7] + overwrite_string [:])

# 7. 문자들이 담겨있는 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 출력하세요
array = ["I", "am", "happy"]
print(array[0] + array[1] + array[2])

# 8. 음이 아닌 정수인 (number, number2)가 주어졌을 때, 9로 나눈 나머지를 출력하세요.
number = 123
number2 = 78720646226947352489

# 9. 아래에 my_list와 my_list2라는 두 개의 리스트가 있습니다. 이 두 리스트를 활용하여 입출력 예시와 같이 출력하세요. (my_list와 my_list2를 활용해야 하며, 문자열 슬라이싱은 사용할 수 없습니다. 예를 들어 my_list[5] + my_list[4]와 같은 방법은 사용할 수 없습니다.)
my_list = ['a', 'r', 'g', 'n', 'o', 'c']
my_list2 = ['t', 'u', 'l', 'a', 't', 'i', 'o', 'n', 's']

