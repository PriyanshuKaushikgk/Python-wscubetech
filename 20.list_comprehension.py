<<<<<<< HEAD
#  list compehension is an elegant way to define and create lists based on existing lists.
# list comprehension is generally more compact and faster than normal functions and loops for creating list.

# syntax of list comprehension
# [expression for item in list]


l = []
for a in range(1,101):
    l.append(a)
print(l)

print()

n = [m for m in range(1,101)]
print(n)  # USE same vairable like m in m.

n = [m for m in range(1,101) if m%2==0]
print(n)

s = 'hello'
d = [g for g in s]
=======
#  list compehension is an elegant way to define and create lists based on existing lists.
# list comprehension is generally more compact and faster than normal functions and loops for creating list.

# syntax of list comprehension
# [expression for item in list]


l = []
for a in range(1,101):
    l.append(a)
print(l)

print()

n = [m for m in range(1,101)]
print(n)  # USE same vairable like m in m.

n = [m for m in range(1,101) if m%2==0]
print(n)

s = 'hello'
d = [g for g in s]
>>>>>>> 560dd38c076599402728a14c966acec587d4e178
print(d)