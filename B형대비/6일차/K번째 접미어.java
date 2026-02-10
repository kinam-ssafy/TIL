import java.util.*;

class Trie {
    char alphabet;      // 이 정점으로 이동하는 알파벳
    boolean isWordEnd;  // 이 정점에서 끝나는 문자열이 존재하는 지 표현
    int cnt;            // 이 정점을 root로 하는 subtree에 포함된 문자열 개수

    Map<Character, Trie> children = new HashMap<Character, Trie>(); // 각 문자에 대해 이동하는 다른 정점을 기억하는 HashMap

    Trie(char alphabet) {
        this.alphabet = alphabet;
        this.cnt = 0;
    }

    Trie() {
    }
}

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            Trie head = new Trie();
            K = sc.nextInt();
            String words = sc.next();   // 새로운 단어
            int len = words.length();

            if (K > len) {
                print("none", test_case);
                continue;
            }

            for (int i = 0; i < len; i++) { // i 번째 문자에서 시작하는 접미열을 Trie에 반영
                Trie indexTrie = head;

                for (int j = i; j < len; j++) { // j 번째 문자로 이동하기
                    char alphabet = words.charAt(j);

                    if (!indexTrie.children.containsKey(alphabet)) {    // 새로운 문자라면 정점 추가하기
                        Trie newTrie = new Trie(alphabet);
                        indexTrie.children.put(alphabet, newTrie);
                    }
                    indexTrie = indexTrie.children.get(alphabet);
                    indexTrie.cnt++;    // 하위 문자열 개수 증가
                }

                indexTrie.isWordEnd = true;
            }
            results = new char[len];
            dfs(head, 0, test_case);
        }
    }

    static char[] results;  // 이동하는 경로 위에 놓인 문자
    static int K;

    // trie := 현재 방문 중인 정점
    // depth := 현재 깊이
    // test_case := 테스트 케이스 번호
    public static void dfs(Trie trie, int depth, int test_case) {
        if (K == 0) return;
        
        if (trie.isWordEnd) {   // 해당 정점에서 끝나는 단어가 있다면
            K--;
            if (K == 0) {   // 원하는 문자열에 도달했다면,
                String result = "";
                for (int i = 0; i < depth; i++) {
                    result += results[i];
                }
                print(result, test_case);
                return;
            }
        }

        for (char i = 'a'; i <= 'z'; i++) { // 낮은 알파벳부터 하나씩 이동한다.
            if (trie.children.containsKey(i)) { // 해당 알파벳으로 이동할 수 있다면,
                Trie child = trie.children.get(i);
                if (child.cnt < K){ // 해당 정점으로 이동하더라도 K 개의 문자열보다 적은 개수의 문자열이 있다면,
                    K -= child.cnt; // 빠르게 해당 개수만큼 skip 한다.
                    continue;
                }

                results[depth] = i;
                dfs(child, depth + 1, test_case);
                results[depth] = '_';
            }
        }
    }

    //결과 출력
    public static void print(String str, int test_case) {
        System.out.println("#" + test_case + " " + str);
    }
}