''' swea 4864 문자열비교
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.


ABC

ZZZZZABCZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.


ABC

ZZZZAZBCZZZZZ

문자열이 일치하지 않으므로 0을 출력.
'''

T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()


    for i in range(len(str2)):
        correct = 0
        for j in range(len(str1)):
            if i+j < len(str2):
                if str2[i+j] == str1[j]:
                    correct += 1

        if correct == len(str1):
            print(f"#{t} {1}")
            break



    if correct != len(str1):
        print(f"#{t} {0}")