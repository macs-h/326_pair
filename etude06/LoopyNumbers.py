# E6 - Loopy Numbers
#
# @author Max Huang
# @author Sam Paterson
# @since 17 August 2018
# @version 1

import sys

def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def perfect():
    # limit = 15
    count = 0
    c = 0
    for e in range (2, 500):
        c+=1
        if (c % 10 == 0):
            print(c)
        if count >= 15:
            print("BREAK")
            break
        if checkPrime(e):
            if checkPrime(pow(2,e)-1):
                print(pow(2, e-1)*(pow(2,e)-1))
                count+=1
        # if checkPrime(p):
        #     print(p)

# MAIN
if __name__ == "__main__":
    # input = int(sys.argv[1])
    # print(checkPrime(input))
    perfect()
