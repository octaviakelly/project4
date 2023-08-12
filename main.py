def myfibfunc():


    usernum=(input("Enter your chosen n where n is the nth number in the Fibonacci sequence, or enter QUIT: "))
    def fibfunc(usernum):
        num1 = 0
        num2 = 1
        num3 = 0
        val = 0

        for i in range(2, usernum + 1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            val = num3
            yield (val)

    if usernum=="QUIT":
        return
    else:
        usernum=int(usernum)
        x = [0, 1]
        y = list(fibfunc(usernum-1))
        z = x + y
        a = len(z)
        for i in range(a-1):
            print(str(z[i]) + ",", end="")
        print(z[-1])

myfibfunc()