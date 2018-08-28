



def main():

    # Math Module
    import math
    x = 10.232442
    print("Math.floor(): ", math.floor(x))
    print("Math.ceil(): ", math.ceil(x))


    # Random Module
    import random
    print("Random number: ", random.randint(0, 4))
    print("Random value: ", random.random)

    # Import Module1

    print("Imported Module")
    from project.src.Modules.ModuleExample import ModuleXYZ
    print("Add: ", ModuleXYZ.add(9, 1))
    print("Subtract: ", ModuleXYZ.subtract(5, 3))




if __name__ == '__main__':
    main()


'''

Module
- Similar to classes
- Allows developer to group code together

Note
- Modules can have runnable code in them, hence having a main() method becomes very critical
- You can use __main__ to execute specific parts of the code

How ? 
- First we typed in "import .ModuleXYZ.py" which was incorrect
- We right clicked and click on import 
- Fix it up to what is above 


'''