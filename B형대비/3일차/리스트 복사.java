import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

class UserSolution {
    final int MAX_MAKE_LIST = 10;
    final int MAX_LENGTH = 200000;
    final int MAX_ADDRESS = 6000;
    final int MAX_CHANGE = 110000;
    int initNumber;     // 원본 배열의 번호
    int[][] initValue;  // 원본 배열 (makeList 당시) 정보를 그대로 저장하는 배열

    int addressNumber;  // 새로운 배열의 번호 (마지막 배열 번호 + 1)
    HashMap<String, Integer> address;  // 배열 이름 -> 배열 번호 mapping

    int changeNumber;  // 현재까지 발생한 "변화 event" 개수 (makeList, copyList, updateElement 모두 포함)

    Pair[] changeLog;  // 현재까지 발생한 "변화 event" 정보
    // makeList         : (-1, 원본 배열 번호)
    // copyList         : (-1, -1) 정보 추가하기. (deepcopy를 의미함)
    // updateElement    : (인덱스, 값) ; 인덱스의 값을 변경했다.
    int[] lastChange;  // lastChange[i] := i번 배열의 마지막 변화 event 번호
    int[] prevChange;  // prevChange[i] := i번 변화의 직전 변화 event 번호

    void init() {
        // 원본 배열 초기화
        initNumber = 0;
        initValue = new int[MAX_MAKE_LIST + 1][MAX_LENGTH + 1];

        // 전체 배열 초기화
        addressNumber = 0;
        address = new HashMap<>();

        // 변화 event 정보 초기화
        changeNumber = 0;
        changeLog = new Pair[MAX_CHANGE + 1];
        lastChange = new int[MAX_ADDRESS + 1];
        prevChange = new int[MAX_CHANGE + 1];
    }
    
    String getName(char[] name) {  // char[] -> String 변환 함수
        String x = "";
        for (int i=0;name[i]!=0;i++){
            x += name[i];
        }
        return x;
    }

    void makeList(char[] _mName, int mLength, int[] mListValue) {
        String mName = getName(_mName);
        System.arraycopy(mListValue, 0, initValue[initNumber], 0, mLength);  // initNumber 위치에 원본 배열에 저장하기
        initNumber++;

        address.put(mName, addressNumber);  // mName 이름의 배열을 생성해줍니다.
        addressNumber++;

        changeLog[changeNumber] = new Pair(-1, initNumber - 1);
        prevChange[changeNumber] = -1;
        lastChange[address.get(mName)] = changeNumber;
        changeNumber++;
    }

    void copyList(char[] _mDest, char[] _mSrc, boolean mCopy) {
        String mDest = getName(_mDest);
        String mSrc = getName(_mSrc);
        if (mCopy) {
            address.put(mDest, addressNumber);
            addressNumber++;

            changeLog[changeNumber] = new Pair(-1, -1);
            prevChange[changeNumber] = lastChange[address.get(mSrc)];
            lastChange[address.get(mDest)] = changeNumber;
            changeNumber++;
        } else {
            address.put(mDest, address.get(mSrc));
        }
    }

    void updateElement(char[] _mName, int mIndex, int mValue) {
        String mName = getName(_mName);
        changeLog[changeNumber] = new Pair(mIndex, mValue);
        prevChange[changeNumber] = lastChange[address.get(mName)];
        lastChange[address.get(mName)] = changeNumber;
        changeNumber++;
    }

    int element(char[] _mName, int mIndex) {
        String mName = getName(_mName);
        int c = lastChange[address.get(mName)];
        while (true) {
            if (prevChange[c] == -1) {
                return initValue[changeLog[c].second][mIndex];
            }
            if (changeLog[c].first == mIndex) {
                return changeLog[c].second;
            }
            c = prevChange[c];
        }
    }

    class Pair {
        int first;
        int second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }
}