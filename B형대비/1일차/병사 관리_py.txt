class Node:
    def __init__(self, id=0, v=0, nxt=None):
        self.id = id
        self.v = v
        self.nxt = nxt

def getNewNode(id, nxt=None):
    global node, cnt

    ret = node[cnt]
    cnt += 1
    ret.id = id
    ret.nxt = nxt
    ret.v = version[id] + 1
    version[id] += 1
    return ret

class Team:
    def __init__(self):
        self.head = [None for _ in range(6)]
        self.tail = [None for _ in range(6)]

t = [Team() for _ in range(6)]

def init():
    global node, cnt, version, num

    node = [Node() for _ in range(500055)]
    version = [0 for _ in range(100055)]
    num = [0 for _ in range(100055)]

    cnt = 0
    for i in range(1, 6):
        for j in range(1, 6):
            t[i].tail[j] = t[i].head[j] = getNewNode(0)

def hire(mID, mTeam, mScore):
    newNode = getNewNode(mID)
    t[mTeam].tail[mScore].nxt = newNode
    t[mTeam].tail[mScore] = newNode
    num[mID] = mTeam

def fire(mID):
    version[mID] = -1

def updateSoldier(mID, mScore):
    hire(mID, num[mID], mScore)

def updateTeam(mTeam, mChangeScore):
    if mChangeScore < 0:
        for j in range(1, 6):
            k = j + mChangeScore
            if k < 1:
                k = 1
            if k > 5:
                k = 5
            # j -> k
            if j == k:
                continue

            if t[mTeam].head[j].nxt == None:
                continue

            t[mTeam].tail[k].nxt = t[mTeam].head[j].nxt
            t[mTeam].tail[k] = t[mTeam].tail[j]
            t[mTeam].head[j].nxt = None
            t[mTeam].tail[j] = t[mTeam].head[j]
    if mChangeScore > 0:
        for j in range(5, 0, -1):
            k = j + mChangeScore
            if k < 1:
                k = 1
            if k > 5:
                k = 5
            # j -> k
            if j == k:
                continue

            if t[mTeam].head[j].nxt == None:
                continue

            t[mTeam].tail[k].nxt = t[mTeam].head[j].nxt
            t[mTeam].tail[k] = t[mTeam].tail[j]
            t[mTeam].head[j].nxt = None
            t[mTeam].tail[j] = t[mTeam].head[j]

def bestSoldier(mTeam):
    for j in range(5, 0, -1):
        node = t[mTeam].head[j].nxt
        if node == None:
            continue

        ans = 0
        while node:
            if node.v == version[node.id]:
                ans = node.id if ans < node.id else ans
            node = node.nxt
        if ans != 0:
            return ans

    return 0