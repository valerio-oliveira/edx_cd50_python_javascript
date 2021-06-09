
def regist(f):
    def wrapper1():
        print ("[Registering]")
        f()
        print ("[Registered]")
    return wrapper1

def announce(f):
    def wrapper():
        print ("About to the run function...")
        f()
        print ("Done with the function.")
    return wrapper


@regist
@announce
def hello():
    print("Hello, world!")

hello()