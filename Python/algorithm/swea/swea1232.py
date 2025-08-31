'''swea1232 사칙연산
사칙연산으로 구성되어 있는 식은 이진 트리로 표현할 수 있다. 
아래는 식 “(9/(6-4))*3”을 이진 트리로 표현한 것이다.
            *
        /       3
    9     -
        6   4
임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의 결과에 해당 연산자를 적용한다.

사칙연산 “+, -, *, /”와 양의 정수로만 구성된 임의의 이진 트리가 주어질 때, 
이를 계산한 결과를 출력하는 프로그램을 작성하라.

계산 중간 과정에서의 연산은 모두 실수 연산으로 한다.


총 10개의 테스트 케이스가 주어진다. (총 테스트 케이스의 개수는 입력으로 주어지지 않는다)

각 테스트 케이스의 첫 줄에는 정점의 개수 N(1≤N≤1000)이 주어진다. 
그다음 N 줄에 걸쳐 각 정점의 정보가 주어진다.

정점이 정수면 정점 번호와 양의 정수가 주어지고, 
정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호가 차례대로 주어진다.

정점 번호는 1부터 N까지의 정수로 구분된고 루트 정점의 번호는 항상 1이다.

위의 예시에서, 숫자 4가 7번 정점에 해당하면 “7 4”으로 주어지고, 
연산자 ‘/’가 2번 정점에 해당하면 두 자식이 각각 숫자 9인 4번 정점과 연산자 ‘-’인 5번 정점이므로 “2 / 4 5”로 주어진다.
'''

T = 10
for t in range(1, T+1):
    N = int(input()) #정점의 개수
    tree = [0] * (N + 1)
    operator = []
    for i in range(N):
        info = input().split()
        if info[1] in '-+*/':
            tree[i+1] = info[1]
            operator.append(info)
        else:
            tree[i+1] = float(info[1])
    # print(operator)
    # print(tree)

    #정점이 정수면 정점 번호화 양의 정수 주어짐

    #정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식 정점 번호 주어짐
    
    #operator 예시
    #[['1', '/', '2', '3'], ['2', '-', '4', '5'], ['3', '-', '6', '7']] 이런식으로 저장
    for i in range(len(operator)-1, -1, -1):
        if operator[i][1] == '-':
            tree[int(operator[i][0])] = tree[int(operator[i][2])] - tree[int(operator[i][3])]
        
        elif operator[i][1] == '+':
            tree[int(operator[i][0])] = tree[int(operator[i][2])] + tree[int(operator[i][3])]
        
        elif operator[i][1] == '*':
            tree[int(operator[i][0])] = tree[int(operator[i][2])] * tree[int(operator[i][3])]
        
        elif operator[i][1] == '/':
            tree[int(operator[i][0])] = tree[int(operator[i][2])] / tree[int(operator[i][3])]
        
    print(f"#{t} {int(tree[1])}")