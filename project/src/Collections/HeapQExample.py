import heapq

def main():

    list1 = [6,1,7,3,9,5,8,2,4]

    # Heapify - Convert an iterable to a heap data structure
    heapq.heapify(list1)

    # Print HeapQ
    print("HeapQ1: ", list(list1))

    # Insert Elements
    heapq.heappush(list1, 100)
    print("\nInsert 100 into heap: ", list1)
    print("**Notice that list1 has added the value 100 ")

    # Remove and Pop smallest elements
    print("\nPopping from heap: ", heapq.heappop(list1))
    print("Heap After pop: ", list1)
    print("Noticed it popped from the left ...not right")


    # PushPop  - combines push and pop operations in one statement for better efficiency
    print("\npushPop: ", heapq.heappushpop(list1, 99))
    print("Heap After pushpop: ", list1)

    # HeadReplace - Pops element first ...then pushes element. The larger value than pushed element is returned
    print("\nHeadReplace: ", heapq.heapreplace(list1, 1))
    print("Heap After pushpop: ", list1)


    # Return the k largest elements from the iterable
    print("The largest 3 numbers in the list: ", heapq.nlargest(3, list1))

    # Return the k smallest element from the interable
    print("The smallest 3 numbers in the list: ", heapq.nsmallest(3, list1))

    pass



if __name__ == '__main__':
    main()


'''
HeapQ

What? 
- Collection data structure to implement a priority Queue
- REMEMBER HEAP ONLY CARES ABOUT THE TOP ELEMENT ...which is a[0] ... everything else can be random order

Why ? 
- Maintains the priority of the heap
- Whenever an element is popped, it pops the smallest of the Heap Element


'''