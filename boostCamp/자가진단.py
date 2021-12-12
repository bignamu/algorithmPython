
def answer(s):
    result = sorted(list(s),reverse=True)
    
    return ''.join(result)



print(answer('hello'))




''' 2. 문자열 s 가 주어졌을 때, s 가 팰린드롬(palindrome) 인지 검사하고 맞으면 1, 틀리면 -1 를 반환하는 함수를 구현하여라. 

(팰린드롬은 문자열의 순서를 반대로 뒤집어도 동일한 문자열이 완성되는 형태의 문자열을 의미한다.)​

​​

제한사항

​- 문자열 s 의 길이는 1 이상 10,000 이하 입니다.

​​

입출력 예시

s

result

"abcd"

-1

"abba"

1

"a"

1 '''