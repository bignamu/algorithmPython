def solution(routes):
    
    routes.sort(key = lambda x:x[1])
    
    print(routes)
    
    

    x = routes[0][0]
    y = routes[0][1]
    cam = 0
    coRoutes = routes[:]



    for i in routes:
        if [x,y] == i:

            continue
        if y >= i[0] and y <= i[1]:
            coRoutes.remove(i)
        if y <i[0] and y < i[1]:
            x = i[0]
            y = i[1]



    print(len(coRoutes))
    print(routes)
    answer = len(coRoutes)
    return answer



routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]

solution(routes)

# 프로그래머스 답

""" 
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer """