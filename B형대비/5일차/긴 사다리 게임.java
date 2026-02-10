import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.TreeMap;
import java.util.StringTokenizer;

class Node {
    int idx;
    Node prev;
    Node next;
    Node(int idx) {
        this.idx = idx;
    }
}
class UserSolution
{

    static final int N = 100;
    static final int MAX_NUM_NODE = 400210;
    static final int LAST_START_NODE = N;
    static final int FIRST_END_NODE = MAX_NUM_NODE - N - 5;

    static Node[] node = new Node[MAX_NUM_NODE];    // 교점들의 이중 연결 리스트
    static int nodeCnt = 0;
    static TreeMap<Integer, Node> nodeMap[] = new TreeMap[N + 1];   // nodeMap[x] := x번 세로줄의 정점들의 y 좌표를 들고 있는 TreeMap

    public static void link(Node front, Node back) {    // 두 정점을 서로 연결해주기
        front.next = back;
        back.prev = front;
    }

    public static void init() {
        for (int i = 0; i < MAX_NUM_NODE; i++) {
            node[i] = new Node(i);
        }
        for (int i = 1; i <= N; i++) {
            nodeMap[i] = new TreeMap<>();
            
            nodeMap[i].put(0, node[i]);     // i 번 세로줄에 i 번 참가자를 놓는다.

            nodeMap[i].put(1000000000, node[FIRST_END_NODE + i - 1]);   // i 번 세로줄의 도착점을 추가한다.
            link(node[i], node[FIRST_END_NODE + i - 1]);
        }
        nodeCnt = N + 1;
    }

    public static void add(int mX, int mY) {  // (mX, mY)와 (mX + 1, mY)을 잇는 가로줄 추가하기, O(Log N)
        Node nowLeft = node[nodeCnt++];
        Node nowRight = node[nodeCnt++];

        Node prevLeft = nodeMap[mX].floorEntry(mY).getValue();          // mX 번 세로 줄에서 mY 직전 정점 찾기
        Node prevRight = nodeMap[mX + 1].floorEntry(mY).getValue();     // (mX + 1) 번 세로 줄에서 mY 직전 정점 찾기

        Node nextLeft = prevLeft.next;      // mX 번 세로 줄에서 mY 직후 정점 찾기
        Node nextRight = prevRight.next;    // (mX + 1) 번 세로 줄에서 mY 직후 정점 찾기

        // 순서 재조정 하기
        link(prevLeft, nowRight);
        link(nowRight, nextRight);

        link(prevRight, nowLeft);
        link(nowLeft, nextLeft);

        nodeMap[mX].put(mY, nowLeft);
        nodeMap[mX + 1].put(mY, nowRight);
    }

    public static void remove(int mX, int mY) {  // (mX, mY)와 (mX + 1, mY)을 잇는 가로줄 제거하기, O(Log N)
        Node nowLeft = nodeMap[mX].get(mY);         // mX번 세로 줄에서 mY 위치 정점 찾기
        Node nowRight = nodeMap[mX + 1].get(mY);    // (mX + 1)번 세로 줄에서 mY 위치 정점 찾기

        Node prevLeft = nowRight.prev;
        Node prevRight = nowLeft.prev;

        Node nextLeft = nowLeft.next;
        Node nextRight = nowRight.next;

        // 순서 재조정 하기
        link(prevLeft, nextLeft);
        link(prevRight, nextRight);

        nodeMap[mX].remove(mY);
        nodeMap[mX + 1].remove(mY);
    }

    public static int numberOfCross(int mID) {  // mID번 참가자가 지나게 되는 가로줄의 개수 구하기, O(5000)
        int ret = -1;
        Node now = node[mID];   // mID 번 세로줄에서 출발하기
        while (now.idx < node[FIRST_END_NODE].idx) {    // 마지막 줄에 도착할 때까지 다음으로 이동하기
            ret++;
            now = now.next;
        }
        return ret;
    }

    public static int participant(int mX, int mY) {  // (mX, mY)에 도착하는 참가자 찾기, O(5000)
        Node now = nodeMap[mX].floorEntry(mY).getValue();  // mX 번 세로 줄에서 mY 직전 정점 찾기
 
        while (now.idx > node[LAST_START_NODE].idx) // 최상단에 도착할 때까지 이전으로 돌아가기
            now = now.prev;
        return now.idx;
    }
}