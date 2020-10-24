"""
A decorator takes in a function, adds some functionality and returns it.
"""

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

@make_pretty
def dec_ordinary():
    print("I am ordinary")

ordinary()
print("-"*10)
p = make_pretty(ordinary)
p()
print("-"*10)
dec_ordinary()