def solution(s):
    answer = ""

    s = s.lower()
    s_split = s.split(" ")

    for i in s_split:

        i = i.capitalize()
        answer += i + " "

    return answer[:-1]