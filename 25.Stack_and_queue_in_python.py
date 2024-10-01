# Stack in python:--->
# The Stack is alinear data structure.
# Stores items in a last - in /first-out (LIFO) or First-In/Last-Out(FILO) manner.

# Stack operations:--------->>>>>>>
# 1. Push=> Inserting an Elements
# 2. Pop=> Deletion An Elements(Last element)
# 3. Peek=> Display tha last Element
# 4. Display=> Display List


# l = []
# while True:
#     c = int(input('''
#             1.Push Elements
#             2. Pop Elemnts
#             3. Peek Elements
#             4. Display Stack
#             5. Exit
#             '''))
    
#     if c == 1:
#         n = input("enter the value:-")
#         l.append(n)
#         print(l)
#     elif c==2:
#         if len(l) ==0:
#             print("Empty Stack")
#         else:
#             p=l.pop()
#             print(p)
#             print(l)
#     elif c==3:
#         if len(l)==0:
#             print("Empty Stack")
#         else:
#             print("Last Stack Value",l[-1])
#     elif c==4:
#         print("Display Stack",l)
#     elif c==5:
#         break
#     else:
#         print("invalid operations")







# ------------- Queue In  python::::::::------------->>>>>>>>>

# The Queue is a lineat data structure.
# Stores items in First In First Out(FIFO) manner.

# Queue Operations:

# 1. Enqueue: Adds an item to the queue.
# 2. Dequeue: Remove an items from the queue.
# 3. front: Get the front iitem from the queue.
# 4. Rear: Get the last item from queue.
    

l = []
while True:
    c = int(input('''
            1. Push Elements
            2. Pop first Elements
            3. Front Elements
            4. last Elements
            5. Display Queue
            6. Exit
            '''))
    
    if c == 1:
        n = input("enter the value:-")
        l.append(n)
        print(l)
    elif c==2:
        if len(l) ==0:
            print("Empty Queue")
        else:
            del l[0]
            
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("First Queue Value",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("Last Queue Value",l[-1])
    elif c==5:
        print("Display Queue",l)
    elif c==6:
        break
    else:
        print("invalid operations")


