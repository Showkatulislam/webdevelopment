def home(f):
    def index():
        print("About function..")
        f()
        print("done function")
    return index


@home
def hello():
    print("hello,world")

hello()