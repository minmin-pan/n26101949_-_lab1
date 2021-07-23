import random


class Nine_Coins:
    # constructor
    def __init__(self, num):
        self.num = num

        # decimal num to binary num
        binary = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 1
        while num != 0:
            binary[len(binary)-i] += (num % 2)
            num //= 2
            i += 1
        self.binary = binary
        b = ''
        for k in binary:
            b += str(k)
        self.b = b

        # change binary code to head or tail
        h_t = ''
        for j in self.binary:
            if j == 0:
                h_t += 'H'
            else:
                h_t += 'T'
        self.h_t = h_t

    def __repr__(self):
        return f'Nine_Coins: {self.h_t}'

    def __str__(self):
        return f'binary: {self.b} and decimal: {self.num}'

    def toss(self):
        # change binary num by random
        for i in range(len(self.binary)):
            self.binary[i] = random.randint(0, 1)
        b = ''
        for j in self.binary:
            b += str(j)
        self.b = b

        # change the random binary num to head or tail
        h_t = ''
        for k in self.binary:
            if k == 0:
                h_t += 'H'
            else:
                h_t += 'T'
        self.h_t = h_t

        # change the random binary num  to decimal num
        num = 0
        a = 8
        for m in self.binary:
            if m == 1:
                num += 2**a
            a -= 1
        self.num = num
