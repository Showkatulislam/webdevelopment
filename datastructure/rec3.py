def fun(a):
    if a>0:
        print(f"calling before fun: {a}")
        fun(a-1)
        print(f"calling after fun: {a}")
fun(4)