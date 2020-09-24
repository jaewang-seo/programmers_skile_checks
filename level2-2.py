def solution(numbers):
    import itertools
    number = list(numbers)

    a = []
    for i in range(1, len(numbers)+1):
        a+=list(map(''.join,itertools.permutations(number,i)))
    a = list(set(map(int, a)))
    a.sort()

    count = 0

    for i in a:
        if i < 2:
            pass
        elif i == 2:
            count += 1
        else:
            for j in range(2,i):
                if i % j == 0:
                    break;
                elif j == i-1 :
                    count +=1
    return count