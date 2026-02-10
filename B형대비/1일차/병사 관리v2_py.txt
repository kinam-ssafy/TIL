MIN_ID = 1
MAX_ID = 100000
MIN_TEAM = 1
MAX_TEAM = 5
MIN_SCORE = 1
MAX_SCORE = 5

class Node:
    def __init__(self):
        self.id = 0
        self.team = 0
        self.prev = None
        self.next = None

class List:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

    @classmethod
    def link(cls, front, back):
        front.next = back
        back.prev = front

    @classmethod
    def erase(cls, node):
        cls.link(node.prev, node.next)

    def initialize(self):
        self.link(self.head, self.tail)

    def insert(self, node):
        self.link(self.tail.prev, node)
        self.link(node, self.tail)

    def isEmpty(self):
        return self.head.next == self.tail

    def splice(self, lst):
        if lst.isEmpty():
            return

        self.link(self.tail.prev, lst.head.next)
        self.link(lst.tail.prev, self.tail)
        lst.initialize()

def init():
    global soldier, soldierGroup

    soldier = [Node() for _ in range(MAX_ID + 1)]
    soldierGroup = [[List() for _ in range(MAX_SCORE + 1)] for _ in range(MAX_TEAM + 1)]

    for i in range(MIN_TEAM, MAX_TEAM + 1):
        for j in range(MIN_SCORE, MAX_SCORE + 1):
            soldierGroup[i][j].initialize()

def hire(mID, mTeam, mScore):
    soldier[mID].id = mID
    soldier[mID].team = mTeam
    soldierGroup[mTeam][mScore].insert(soldier[mID])

def fire(mID):
    List.erase(soldier[mID])

def updateSoldier(mID, mScore):
    List.erase(soldier[mID])
    soldierGroup[soldier[mID].team][mScore].insert(soldier[mID])

def updateTeam(mTeam, mChangeScore):
    if mChangeScore > 0:
        for i in range(MAX_SCORE - 1, MIN_SCORE - 1, -1):
            newScore = i + mChangeScore
            if newScore > MAX_SCORE:
                newScore = MAX_SCORE
            soldierGroup[mTeam][newScore].splice(soldierGroup[mTeam][i])
    elif mChangeScore < 0:
        for i in range(MIN_SCORE + 1, MAX_SCORE + 1):
            newScore = i + mChangeScore
            if newScore < MIN_SCORE:
                newScore = MIN_SCORE
            soldierGroup[mTeam][newScore].splice(soldierGroup[mTeam][i])

def bestSoldier(mTeam):
    maxScoreGroup = List()
    for i in range(MAX_SCORE, MIN_SCORE - 1, -1):
        if not soldierGroup[mTeam][i].isEmpty():
            maxScoreGroup = soldierGroup[mTeam][i]
            break

    maxId = MIN_ID - 1
    maxScoreSoldier = maxScoreGroup.head.next
    while maxScoreSoldier != maxScoreGroup.tail:
        if maxId < maxScoreSoldier.id:
            maxId = maxScoreSoldier.id
        maxScoreSoldier = maxScoreSoldier.next

    return maxId