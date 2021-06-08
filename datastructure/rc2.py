def fun(a):
    if a>0:
        print(f"called {a}")
        fun(a-1)
    
fun(3)