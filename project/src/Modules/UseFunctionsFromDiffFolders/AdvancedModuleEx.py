from project.src.Modules.ModuleExample.ModuleXYZ import *

def main():

    # Using add(x,y) from the ModuleExample
    # Notice this is in completely different module
    print("Add: ", add(5,4))




if __name__ == '__main__':
    main()


'''
Note 

- By Default, you CANNOT import files from a different python "FOLDER" (FOLDER ...NOT PACKAGE)

Packages
- Carry the __init__.py. This REQUIRED  tof be used as part of a package
- If you remove this file - Python will no longer look for sub modules in that directory
    -> ANY IMPORTS from this file will fail
    
    
Note
- The __init__.py file is needed for Python 2.X but no longer required for 3.3 and Above    
    

'''