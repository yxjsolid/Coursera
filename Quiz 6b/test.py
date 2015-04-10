__author__ = 'xyang'

def q7():
    n = 1000
    numbers = []
    result = []
    for i in range(2, 1000):
        #print i
        numbers.append(i)

    number = numbers.pop(0)
    result.append(number)

    while len(numbers) > 0:
        number = numbers.pop(0)
        drop = 0
        for dev in result:
            if number%dev == 0:
                drop = 1
                break

        if drop == 0:
            result.append(number)

    print len(result)


def q8():

    slow = wumpuses(1000, 0.4)
    fast = wumpuses(1, 0.3)
    year = 1
    while 1:




        print year, slow.cnt, fast.cnt

        slow.start()
        fast.start()

        slow.end()
        fast.end()





        year += 1
        if fast.cnt > slow.cnt:
            break


    pass



class wumpuses():
    def __init__(self, initCnt, deadRate):
        self.cnt = initCnt
        self.deadRate = deadRate


    def start(self):
        self.cnt *=2

    def end(self):
        self.cnt *= 1 - self.deadRate






    pass



if __name__ == "__main__":

    q8()
