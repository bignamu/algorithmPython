def solution(phoneBook):

    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1,p2)
        if p2.startswith(p1):
            return False
    return True


li = ["12","123","1235","567","88"]

solution(li)