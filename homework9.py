#여러 입력값을 활용하는 함수 문제
#1 *args 를 활용하여 전달된 숫자들의 평균을 계산하는 함수를 작성하세요.

def calculate_average(*args):
    score = 0

    for num in args:
        score += num

    return score/len(args)



numbers1 = 10, 20, 30, 40, 50
print(calculate_average(*numbers1))  # 출력: 30.0

numbers2 = 2, 4, 6, 8, 10
print(calculate_average(*numbers2))  # 출력: 6.0

#2. *args 로 전달된 문자열들을 이어붙인 하나의 문자열을 반환하는 함수를 작성하세요
def concatenate_strings(*args):
    
    return "".join(args)

    
        

strings1 = "Hello", " ", "world", "!"
print(concatenate_strings(*strings1))  # 출력: Hello world!

strings2 = "Python", " is", " fun"
print(concatenate_strings(*strings2))  # 출력: Python is fun

#3. *args 로 전달된 숫자들 중에서 최댓값을 찾아서 반환하는 함수를 작성하세요.

def find_maximum(*args):
    
    return max(args)

numbers1 = 5, 12, 9, 20, 3
print(find_maximum(*numbers1))  # 출력: 20

numbers2 = -8, 0, 10, -3
print(find_maximum(*numbers2))  # 출력: 10

#4. *args 로 전달된 숫자들을 모두 곱한 값을 반환하는 함수를 작성하세요.
def calculate_product(*args):
    score = 1
    for n in args:
        score *= n

    return score

numbers1 = 2, 3, 4, 5
print(calculate_product(*numbers1))  # 출력: 120

numbers2 = -2, 4, -3
print(calculate_product(*numbers2))  # 출력: 24

#5. *args 로 전달된 문자열들 중에서 가장 긴 문자열을 찾아서 반환하는 함수를 작성하세요.

#def find_longest_string(*args):
    

#strings1 = "apple", "banana", "cherry", "date"
#print(find_longest_string(*strings1))  # 출력: banana

#strings2 = "dog", "cat", "elephant"
#print(find_longest_string(*strings2))  # 출력: elephant

#6. *args 로 전달된 숫자들을 제곱한 후의 값을 가지고 있는 리스트를 반환하는 함수를 작성하세요
def calculate_squared_values(*args):
    result = []
    for num in args:
        result.append((num)*(num))

    return result
        

numbers1 = 1, 2, 3, 4, 5
print(calculate_squared_values(*numbers1))  # 출력: [1, 4, 9, 16, 25]

numbers2 = -3, 0, 2
print(calculate_squared_values(*numbers2))  # 출력: [9, 0, 4]

#7. *args 로 전달된 숫자들을 오름차순으로 정렬한 리스트를 반환하는 함수를 작성하세요.
def sort_numbers_ascending(*args):
        
	return sorted(args)

numbers1 = 5, 2, 9, 1, 7
print(sort_numbers_ascending(*numbers1))  # 출력: [1, 2, 5, 7, 9]

numbers2 = -3, 8, 0, -1
print(sort_numbers_ascending(*numbers2))  # 출력: [-3, -1, 0, 8]

#8. *args 로 전달된 값들 중에서 홀수만 필터링하여 리스트로 반환하는 함수를 작성하세요.
def filter_odd_numbers(*args):

    result =  [num for num in args if num % 2 == 1]
    
    return result

numbers1 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(filter_odd_numbers(*numbers1))  # 출력: [1, 3, 5, 7, 9]

numbers2 = -4, -3, -2, -1, 0, 1, 2, 3, 4
print(filter_odd_numbers(*numbers2))  # 출력: [-3, -1, 1, 3]

#키워드 매개변수

#1. 두 수를 받아서 더한 값을 반환하는 함수를 작성하세요. 함수는 num1과 num2라는 키워드 매개변수를 받아들이며, 결과를 반환합니다.
def add_numbers(**kwargs):

    result = sum(kwargs.values())

    return result

result = add_numbers(num1=5, num2=3)
print(result)  # 출력 결과: 8

#2. 문자열과 반복 횟수를 입력받아, 해당 문자열을 주어진 횟수만큼 반복하여 반환하는 함수를 작성하세요. 함수는 text와 repeats라는 키워드 매개변수를 받아들이며, 결과를 반환합니다.
def repeat_text(**kwargs):
	
    result = kwargs.get("text")*kwargs.get("repeats")
    

    return result

result = repeat_text(text='Hello', repeats=3)
print(result)  # 출력 결과: HelloHelloHello

#3.리스트를 입력받아 짝수만 필터링하여 반환하는 함수를 작성하세요. 함수는 numbers라는 키워드 매개변수를 받아들이며, 짝수만을 담은 리스트를 반환합니다.
def filter_even_numbers(**kwargs):
    result = []
        
    for num  in kwargs.get("numbers"):
        if num % 2 == 0:
            result.append(num)

    return result

result = filter_even_numbers(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)  # 출력 결과: [2, 4, 6, 8, 10]

#4. 원의 반지름을 입력받아 원의 넓이를 계산하는 함수를 작성하세요. 함수는 radius라는 키워드 매개변수를 받아들이며, 원의 넓이를 반환합니다.
def calculate_circle_area(**kwargs):
    pi = 3.14
    
    result = kwargs.get("radius")

    return result*result*pi

result = calculate_circle_area(radius=5)
print(result)  # 출력 결과: 78.5

#5. 사각형의 가로와 세로 길이를 입력받아 넓이를 계산하는 함수를 작성하세요. 함수는 width와 height라는 키워드 매개변수를 받아들이며, 넓이를 반환합니다.
def calculate_rectangle_area(**kwargs):
	
    result = kwargs.get("width")*kwargs.get("height")

    return result

result = calculate_rectangle_area(width=6, height=4)
print(result)  # 출력 결과: 24

#6. 이메일 주소와 메시지를 입력받아 이메일을 전송하는 함수를 작성하세요. 함수는 email와 message라는 키워드 매개변수를 받아들이며, 전송 성공 여부를 반환합니다.
#def send_email(**kwargs):
	
    #result = kwargs.get("email"),kwargs.get("message")

    

#result = send_email(email='example@example.com', message='Hello there!')
#print(result)  # 출력 결과: True

#7. 사용자의 정보를 입력받아 딕셔너리 형태로 반환하는 함수를 작성하세요. 함수는 name, age, city라는 키워드 매개변수를 받아들이며, 사용자 정보를 딕셔너리로 구성하여 반환합니다.
def get_user_info(**kwargs):
	
    result = kwargs

    return result

result = get_user_info(name='Alice', age=30, city='New York')
print(result)  # 출력 결과: {'name': 'Alice', 'age': 30, 'city': 'New York'}

#8. 리스트와 찾으려는 요소를 입력받아, 해당 요소가 리스트에 있는지 여부를 반환하는 함수를 작성하세요. 함수는 my_list와 target라는 키워드 매개변수를 받아들이며, 요소의 존재 여부를 불리언 값으로 반환합니다.
def check_element_in_list(**kwargs):
    result = kwargs.get("my_List")
        
    if "result" in "target":
        return "True"
        
result = check_element_in_list(my_list=[1, 2, 3, 4, 5], target=3)
print(result)  # 출력 결과: True