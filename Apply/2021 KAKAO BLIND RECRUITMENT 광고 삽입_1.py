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
        sec = sec % 3600
        m = sec // 60
        s = sec % 60
        if len(str(h)) == 1:
            h = '0'+ str(h)
        if len(str(m)) == 1:
            m = '0' + str(m)
        if len(str(s)) == 1:
            s = '0' + str(s)
        return f'{h}:{m}:{s}'
    
    play_sec = makesec(play_time)
    adv_sec = makesec(adv_time)
    all_time = [0 for _ in range(play_sec+1)]
    
    log_start = []
    log_end = []

    for log in logs:
        log = log.split('-')
        start = makesec(log[0])
        end = makesec(log[1])
        log_start.append(start)
        log_end.append(end)
    
    for ls in log_start:
        all_time[ls] += 1
    
    for le in log_end:
        all_time[le] += -1

    for i in range(1,len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
    
    for i in range(1,len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
    
    most_view = 0
    max_time = 0

    
    for i in range(adv_sec - 1, play_sec):
        if  i >= adv_sec:
            previous = most_view
            most_view = max(most_view,all_time[i]-all_time[i-adv_sec])
            if previous != most_view:
                max_time = i - adv_sec + 1
        else:
            most_view = max(max_time,all_time[i])
        
        
    
    # print(max_time,makehms(max_time))
    

    answer = makehms(max_time)

    
        
        
        
    

    return answer



play_time = "02:03:55"	
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time,adv_time,logs))
		