### Sammlung an Tricks und Kniffen ###

def unpack_collection(): # Fund: Herr Dering

    def add(num,num2): 
        print(num+num2)

    add(*[100,2])
    add(*["Elder","Berries"])



def seperate_in_print(): # Fund: Herr Dering
    print(*"text", sep="\t")


def multi_input():
    inputs = [input().split(" ")]
    for word in inputs:
        print(word)

# def ternary_bool():
#     x,y = ("Wahr", "Falsch"),0
#     print((x[0],x[1])[y])

def ternary_bool_revised():
    truth_tuple, number = ("Wahr", "Falsch"), 0
    print(truth_tuple[0] if number == 0 else truth_tuple[1])

ternary_bool_revised()

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
