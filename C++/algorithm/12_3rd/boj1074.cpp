/*boj1074 - Z
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 
예를 들어, 
2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.



N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.



N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
*/


// 2**N x 2**N 배열
// r행 c열 
// N = 2, 3행 1열이면
// 0 0 0 0
// 0 0 0 0 
// 0 0 0 0
// 0 0 0 0
// 2 ** (2 - 1) x 2 ** (2 - 1) = 4 번째는 지나고
// (1 + 2)행 1열 == 5번째

// 2 ** (N - 1) x 2 ** (N - 1) 번째에
// (1 + 2 ** (N - 1))행  번째?
// 분할로 일단 나눠서 N - n번인지 파악하기
// 분할을 계속 재귀적으로 나누기 반으로 나누고 몇사분면인지 체크하고 반으로 나누고 몇 사분면인지 체크하고 반복




#include <iostream>
#include <cmath> // 거듭제곱 표현 pow함수 사용

using namespace std;

long long cnt = 0;

void halfhalf(int N, int r, int c) {
    // 종료조건은 N이 1x1배열이되면 끝
    if (N == 0) {
        cout << cnt;
        return;
    }
    
    // int half = (int)pow(2, N); 이렇게 표현하기
    // int half = (2 ** N) % 2; 이렇게 하면 에러남
    // 또는 비트연산자 1 << N 사용 하기 2의 N제곱 = 정수 1을 왼쪽으로 N번 비트 이동

    int half = 1 << (N - 1);

    if (r < half && c < half) {
        // 좌 상
        halfhalf(N - 1, r, c);
    }

    else if (r < half && c >= half) {
        // 우 상
        cnt += half * half;
        halfhalf(N - 1, r, c - half);
    }

    else if (r >= half && c < half) {
        //좌 하
        cnt += half * half * 2;
        halfhalf(N - 1, r - half, c);
    }

    else if (r >= half && c >= half) {
        // 우 하
        cnt += half * half * 3;
        halfhalf(N - 1, r - half, c - half);
    }
}





int main() {
    int N, r, c;
    cin >> N >> r >> c;
    // 2, 3, 1 이면 정답이 11이라는데 0행 0열부터 시작하는거였음
    


    halfhalf(N, r, c);

    return 0;
}