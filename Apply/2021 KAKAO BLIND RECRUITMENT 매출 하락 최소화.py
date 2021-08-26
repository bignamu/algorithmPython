
from collections import defaultdict

def solution(sales, links):

    teams = defaultdict(list)
    
    for a, b in links:
    
        teams[a].append((b,sales[b-1]))

    for a in teams.keys():
        teams[a].append((a,sales[a-1]))


    teams_val = list(teams.values())
    teams_key = list(teams.keys())
    for i in range(len(teams)):
        end = i
        while end < len(teams):
            
            end += 1
            if end == len(teams):
                break
            
            test = set(teams_val[i]) & set(teams_val[end])
            print(test,teams_key[i],teams_key[end])
            
        
    
    def dfs(start):

        if promising():
            print('ok')
        
    def promising():
        return True
    
    
    dfs(1)
    
    
    

        
    print(teams)
        
        
    
    
    
    answer = 0
    return answer



sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]	
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]

solution(sales,links)