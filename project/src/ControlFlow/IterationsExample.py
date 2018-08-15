def main():

    # Using For In
    print("For In Iteration")
    list1 = ["Bring", "It", "On", "Biatch"]
    for i in list1:
        print(i)


    # Using For In Range
    print("\nFor in Range")
    for i in range(len(list1)):
        print(i)

    # Using enumerate
    print("\nEnumerate Example")
    for i,x in enumerate(list1):
        print("Index:", i , "     Value:", x)



if __name__ == '__main__':
    main()