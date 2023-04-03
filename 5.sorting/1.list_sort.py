# when sort is applied it takes two parameters, one is key another is reverse

def find_len(l):
    return len(l)


l = ['my', 'name', 'is', 'gowrav']

l.sort(key=find_len)


# print(l)

# sorting user defined objects

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def fun_a(p):
    return p.a


"""
 here the three objects of Point are created and are sorted using the attribute 'a' , even when the attribute
 a is same in the object, sorting will maintain its order of the original points
 Ex:  [Point(1, 15), Point(20, 5), Point(1, 29)]
 Output: 1 15
         1 29
         20 5
 Even though the first object and the third object , python maintains its original state and returns 1,15 in the 
 first place as it is present first
"""

l = [Point(1, 15), Point(20, 5), Point(1, 29)]

l.sort(key=fun_a)

# for i in l:
#     print(i.a, i.b)

"""
    Instead of explicitly sorting by defining the key , we used the magic method __lt__ which is less than 
    it compares all the first numbers with the remaining elements
"""


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.a < other.a


l = [Point(1, 15), Point(20, 5), Point(8, 29)]

l.sort()

# for i in l:
#     print(i.a, i.b)

"""
    In this method if the first elements then we are checking with the second element that is present and 
    returning the sorting based on that
"""


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a == other.a:
            return self.b < other.b
        return self.a < other.a


l = [Point(1, 15), Point(20, 5), Point(1, 7)]

l.sort()

for i in l:
    print(i.a, i.b)
