import collections

def main():

    list1 = [1,4,6,7,3,8,9]

    # Instantiate a Deque
    deque1 = collections.deque(list1)

    # Append
    deque1.append(100)
    print("Append: ", deque1)

    # AppendLeft
    deque1.appendleft(500)
    print("\nAppendLeft: ", deque1)

    # Pop
    print("\npop: ", deque1.pop())
    print("Deque after pop: ", deque1)

    # PopLeft
    print("\npopLeft: ", deque1.popleft())
    print("Deque after popLeft: ", deque1)

    # Copy
    deque2 = deque1.copy()
    print("\ndeque2: ", deque2)

    deque2.pop()
    print("Deque2 afer pop: ", deque2)
    print("Deque1 after popping Deque2: ", deque1)
    print(".copy is a DEEP COPY ... NOT  a shallow")


    # Count
    print("\ncount occurence of 3: ", deque1.count(3))

    # Index
    print("index of 7: ", deque1.index(7, 0, deque1.__len__()))
    #print("index of 100: ", deque1.index(100))      # This will throw an Error


    # Insert
    deque1.insert(3, 300)
    print("\ninsert 300 in index 3: ", deque1)

    # Remove
    deque1.remove(300)
    print("\nremove 300: ", deque1)

    # Rotate
    print("\nBefore rotate: ", deque1)
    deque1.rotate(3)
    print('rotate by 3: ', deque1)
    deque1.rotate(2)
    print('rotate by 2: ', deque1)

    # Extend
    deque1.extend([10,20,30])
    print("extend: ", deque1)

    # Clear
    deque1.clear()
    print("clear: ", deque1)

    pass


if __name__ == '__main__':
    main()


'''
Deque

What ? 
- Also known as a DOUBLE ENDED Queue
- Elements can be removed from the front or back ...(Left of Right)

How ?
- Can be implemented using the module collections

'''