def fun(a):
    if a>0:
        fun(a-1)
        print(f"called {a}")
    
fun(3)