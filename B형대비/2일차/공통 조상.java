import java.util.*;

public class Solution {
    static int ans, N, M, A, B;
    static Node[] nodes;                            // node[i] := i 번 정점의 자식 정점들
    static ArrayList<Integer> ancestorA, ancestorB;

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int T;

        T = sc.nextInt();
        for (int t = 1; t < T + 1; t++) {
            N = sc.nextInt();
            M = sc.nextInt();
            A = sc.nextInt();
            B = sc.nextInt();
            nodes = new Node[N + 1];
            ancestorA = new ArrayList<>();
            ancestorB = new ArrayList<>();

            for (int i = 0; i < N + 1; i++) {
                nodes[i] = new Node();
            }
            for (int i = 0; i < M; i++) {
                int p, c;
                p = sc.nextInt();
                c = sc.nextInt();
                nodes[p].children.add(c);
                nodes[c].parents = p;
            }

            // A 와 B 의 조상 찾기
            traverse(A, ancestorA);
            traverse(B, ancestorB);

            for (int i = 0; i < N; i++) {
                if (!ancestorA.get(i).equals(ancestorB.get(i))) break;
                ans = ancestorA.get(i);
            }

            System.out.printf("#%d %d %d\n", t, ans, dfs(ans));
        }
    }

    public static int dfs(int idx) {  // idx 를 root로 갖는 subtree 의 크기를 계산하는 함수
        int res = 1;
        for (int child : nodes[idx].children) {
            res += dfs(child);
        }
        return res;
    }

    public static void traverse(int idx, ArrayList<Integer> ancestor) {
        int parent = nodes[idx].parents;
        if (parent != 0) {  // 부모 노드가 존재한다면
            traverse(parent, ancestor);  // 조상을 더 찾으라고 재귀 호출 수행
        }
        ancestor.add(idx);
    }


    static public class Node {
        List<Integer> children;
        int parents;

        Node() {
            this.children = new ArrayList<>();
            this.parents = 0;
        }
    }
}