import re

def hello(name="World"):
    if not isinstance(name, str): #verificamos si name es una cadena  
        return "Hello, World!"
     
    stringwithOutWhiteSpace = name.strip() #remueve espacios al final e inicio del string 

    if re.match(r"^[A-Za-zÀ-ÿ\s]+$", stringwithOutWhiteSpace):  
        newName = stringwithOutWhiteSpace
    else:
        newName = "World"

    return f"Hello, {newName}!"
