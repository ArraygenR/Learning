"""
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
"""

# Python program to illustrate
# closures
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction  # Note we are returning function WITHOUT parenthesis


if __name__ == '__main__':
    myFunction = outerFunction('Coming from outerFunction, but this parameter is remembered by innerFunction')
    myFunction()
