# 인덱스 바꾸기
def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    my_string[num1],my_string[num2] = my_string[num2],my_string[num1]
    # return answer.join(my_string)
print(solution("i love you",3,6))