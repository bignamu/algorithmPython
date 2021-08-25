from collections import defaultdict

def solution(play_time, adv_time, logs):
    answer = ''
    
    def makesec(play_time):
        multi60 = [60*60,60,1]
        pt = play_time.split(':')
        pt_all = 0
        for t,m in zip(pt,multi60):
            pt_all += int(t)*int(m)
        return pt_all
    def makehms(sec):
        h = sec // 3600
        m = (sec- h*3600) // 60
        s = sec - h*3600 - m*60
        if len(str(h)) == 1:
            h = '0'+ str(h)
        if len(str(m)) == 1:
            m = '0' + str(m)
        if len(str(s)) == 1:
            s = '0' + str(s)
        return f'{h}:{m}:{s}'
        
    playsec = makesec(play_time)
    # print(playsec)
    _dict = defaultdict(int)
    for k in range(playsec):
        _dict[k] = 0
    for l in logs:
        ls = l.split('-')
        start = makesec(ls[0])
        end = makesec(ls[1])
        while start < end:
            _dict[start] += 1
            start += 1

    # print(_dict)
    advsec = makesec(adv_time)
    
    previous = 0
    where = ''
    valsum = 0
    vs = [0]
    for j in _dict.values():
        valsum += j
        vs.append(valsum)
    # print(vs)
    
    val = 0

    for i in range(playsec-advsec+1):
        val = vs[advsec+i] - vs[i]
        if val > previous:
            where = i
            previous = val
        
        
        # print(val,i)
    
    
    if not where:
        return '00:00:00'
    # print(where)
    # print(makehms(where))
    answer = makehms(where)
    return answer


play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

solution(play_time,adv_time,logs)
		