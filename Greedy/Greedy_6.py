def solution(routes):
    
    routes.sort(key = lambda x:x[0])
    
    """     for san in range(0,len(routes)):
        routes[san][0] += 30000
        routes[san][1] += 30000 """
    
    print(routes)
    
    

    x = routes[0][0]
    y = routes[0][1]
    cam = 0
    setcam = 0
    print(x,y)

    for i in routes:
        if [x,y] == i[0]:
            continue
        if y >= i[0] and setcam == 0:
            cam += 1
            setcam = 1
        elif y < i[0]:
            cam += 1
            setcam = 0
        x = i[0]
        y = i[1]



    print(cam)
    answer = cam
    return answer



routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]

solution(routes)