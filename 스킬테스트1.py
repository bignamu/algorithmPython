def solution(n):
    answer = 0

    
    # def test():
        
    #     t = 100000000
    #     count = 1
    #     while t >3:
    #         t = t//3
    #         count += 1
    #     print(count,t)
        
    dp = [0]*100
    def dpfunc(n):
        if n//3 != 1:
            n%3
    def dfs(n):
        s = ''

        if n//3 == 1:
            s += '1' + str(n%3)
            return s
        
        if n//3 != 1:
            s += dfs(n//3)+str(n%3)
    
        return s
    def goten(n):
        result = 0
        for i in range(len(n)):
            result += int(n[len(n)-1-i])*(3**i)
        return result
        
    rev = dfs(n)[::-1]
    # print(rev)
    # print(goten(rev))
    
    answer = goten(rev)
    print(answer)
    test()
            
    
    return answer

solution(100)

