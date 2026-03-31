"""

문제
요즘 종수는 아두이노를 이용해 "Robots"이라는 게임을 만들었다. 종수는 아두이노 한대를 조정하며, 미친 아두이노를 피해다녀야 한다. 미친 아두이노는 종수의 아두이노를 향해 점점 다가온다. 하지만, 미친 아두이노의 움직임은 예측할 수 있다.

게임은 R×C크기의 보드 위에서 이루어지며, 아래와 같은 5가지 과정이 반복된다.

먼저, 종수가 아두이노를 8가지 방향(수직,수평,대각선)으로 이동시키거나, 그 위치에 그대로 놔둔다.
종수의 아두이노가 미친 아두이노가 있는 칸으로 이동한 경우에는 게임이 끝나게 되며, 종수는 게임을 지게 된다.
미친 아두이노는 8가지 방향 중에서 종수의 아두이노와 가장 가까워 지는 방향으로 한 칸 이동한다. 즉, 종수의 위치를 (r1,s1), 미친 아두이노의 위치를 (r2, s2)라고 했을 때, |r1-r2| + |s1-s2|가 가장 작아지는 방향으로 이동한다.
미친 아두이노가 종수의 아두이노가 있는 칸으로 이동한 경우에는 게임이 끝나게 되고, 종수는 게임을 지게 된다.
2개 또는 그 이상의 미친 아두이노가 같은 칸에 있는 경우에는 큰 폭발이 일어나고, 그 칸에 있는 아두이노는 모두 파괴된다.
종수의 시작 위치, 미친 아두이노의 위치, 종수가 움직이려고 하는 방향이 주어진다. 입력으로 주어진 방향대로 종수가 움직였을 때, 보드의 상태를 구하는 프로그램을 작성하시오. 중간에 게임에서 지게된 경우에는 몇 번째 움직임에서 죽는지를 구한다.

입력
첫째 줄에 보드의 크기 R과 C가 주어진다. (1 ≤ R, C ≤ 100)

다음 R개 줄에는 C개의 문자가 주어지며, 보드의 상태이다. '.'는 빈 칸, 'R'은 미친 아두이노, 'I'는 종수의 위치를 나타낸다.

마지막 줄에는 길이가 100을 넘지않는 문자열이 주어지며, 종수가 움직이려고 하는 방향이다. 5는 그 자리에 그대로 있는 것을 나타내고, 나머지는 아래와 같은 방향을 나타낸다.
"""

R, C = map(int, input().split())

arr = []
crazy = [] # 미친 아두이노
for i in range(R):
    row = list(input())
    for j, ch in enumerate(row):
        if ch == 'I':
            my = (i, j)
        elif ch == 'R':
            crazy.append((i,j))
    arr.append(row)

dir = list(map(int, input()))

move = {
    7: (-1, -1), 8: (-1, 0), 9: (-1, -1),
    4: (1, 0), 5: (0, 0), 6:(0, 1),
    1: (1, -1), 2: (1, 0), 3: (1, 1),
}

def move_robot(r, c, my_r, my_c):
    # r, c : 미친 아두이노 위치
    # my_r, my_c : 종수 아두이노 위치
    if r < my_r:
        dr = 1
    elif r > my_r:
        dr = -1
    else:
        dr = 0

    if c < my_c:
        dc = 1
    elif c > my_c:
        dc = -1
    else:
        dc = 0

    # dr = 0 if r == my_r else (1 if r < my_r else -1)
    # dc = 0 if c == my_c else (1 if c < my_c else -1)

    return r + dr, c + dc
    

ans = 0
dead = False
while not dead:
    dr, dc = move[dir[ans]]
    ans += 1
    #종수 아두이노 이동
    my = (my[0] + dr, my[1] + dc)

    #미친 아두이노 위치에 가면? 끝
    if my in crazy:
        print(f"kraj {ans}")
        dead = True
        break
    
    #미친 아두이노가 종수 아두이노 위치로 가도 끝
    new_crazy = []
    for r, c in crazy:
        new_crazy.append(move_robot(r, c, my[0], my[1]))

    if my in new_crazy:
        print(f"kraj {ans}")
        dead = True
        break

    #2개 또는 그 이상의 미친 아두이노가 같은 칸에 있는 경우 그 칸의 아두이노 파괴
    for i, k in enumerate(new_crazy):
        for j, q in new_crazy[i+1:]:
            if k == new_crazy[j]:
                new_crazy.pop(j)
                new_crazy.pop(i)

    crazy = new_crazy


if not dead:
    for i in range(R):
        for j in range(C):
            if (i, j) == my:
                print('I', end='')
            elif (i, j) in crazy:
                print('R', end='')
            else:
                print('.', end='')
        print()