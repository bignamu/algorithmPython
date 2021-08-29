

def solution(a):
    answer = []
    
    def find_a(test):
        while test[-1] == 'a' or test[0] == 'a':
            if test[-1] == 'a':
                test = test[:-1]
            elif test[0] == 'a':
                test = test[1:]
        return test
    def find_b(test):
        if not 'a' in test:
            return False
        leftb = test.split('a')[0]
        rightb = test.split('a')[-1]

        wantb = min(leftb,rightb)
        test = test[len(wantb):]
        test = test[:-len(wantb)]
        return test
    
    for test in a:
        
        while test:
            test = find_a(test)
            # print(test,'find a')
            test = find_b(test)
            # print(test)
            if not test:
                answer.append(False)
                break
            elif test == 'a':
                answer.append(True)
                break
    print(answer)    
    return answer




a = ["abab","bbaa","bababa","bbbabababbbaa","bbbababb","bbabbabbbb"]	
#[true,false,false,true]
solution(a)