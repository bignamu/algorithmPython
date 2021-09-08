class Trie:
    def __init__(self):
        self.child = dict() # 문자를 key로하고 value로 노드를 가진다
        self.count = 0
    
    def insert(self,str): # 단어를 입력하기 위함
        curr = self # curret를 self로 함, insert는 root에서 시작하기 때문에
        for ch in str:
            curr.count += 1
            if ch not in curr.child:
                curr.child[ch] = Trie()
            
            curr = curr.child[ch]
        curr.count += 1
    
    def search(self,str):
        curr = self
        for ch in str:
            if ch =='?':
                return curr.count
            if ch not in curr.child:
                return 0
            curr = curr.child[ch]
        return curr.count



def solution(words, queries):
    answer = []
    TrieRoot = [Trie() for _ in range(10001)]
    ReTrieRoot = [Trie() for _ in range(10001)]
    
    for str in words:
        TrieRoot[len(str)].insert(str)
        ReTrieRoot[len(str)].insert(str[::-1])
    
    for str in queries:
        if str[0] != '?':
            answer.append(TrieRoot[len(str)].search(str))
        else:
            answer.append(ReTrieRoot[len(str)].search(str[::-1]))

        
    return answer




words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
queries = ["fro??", "????o", "fr???", "fro???", "pro?","?????"]
#	[3, 2, 4, 1, 0]

print(solution(words,queries))