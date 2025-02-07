def greet():
    """
    simple function printing hello
    :return: None
    """
    print("Hello!")
    return 0
greet()
x= greet()
print(x)

def greet_improved(name):
    """
    More complex greet that takes a name as param
    :param name: The name of the person to greet
    :return: None
    """
    print("Hello", name)
greet_improved("John")
greet_improved("Jane")

def custom_op(x= 0,y=0):
    """
    Custom op: 10x + y
    :param x: the frist number
    :param y: the second number
    :return: number, 10x +y
    """
    result= 10*x +y
    return result
print(custom_op(5,8))
x= custom_op(5, 9) #arguments by position
print(f"the result of cutom_op is: {x}")
x= custom_op(y=9, x=5) #arguments by name
print(f"the result of cutom_op is: {x}")
print(custom_op(5)) #using default value for y
print(custom_op()) #default values for both
print(custom_op(y=9)) #default balue for x

def bond_intro(name):
    print("the name is:", name)
def bond_name(first="Helena", last="Amado"):
    return f"{last}, {first},{last}"

print(bond_name("Helena", "Amado"))
bond_intro(bond_name("Helena", "Amado"))
bond_intro(bond_name())
