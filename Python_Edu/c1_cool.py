### Sammlung an Tricks und Kniffen ###


def multi_input():
    inputs = [input().split(" ")]
    for word in inputs:
        print(word)

def ternary_bool():
    x,y = ("Wahr", "Falsch"),0
    print((x[0],x[1])[y])

def fast_swap():
    x = 4
    y = 2
    x,y = y,x
    print(x,y)

def revert_string():
    print("Very Cool"[::-1])

def assignment_in_expression():
    if x:=2 == 2:
        print(x)

def comparison_chaining():
    x = 0
    if 1 < x > -1:
        print(x)

def fast_sqrt(x):
    return x ** .5