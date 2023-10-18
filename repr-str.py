
class Foo:
    def __init__(self, num, s):
        self.num = num
        self.s = s
    def __str__(self):
        return f"[s: {self.s} num: {self.num}]"


a = [ Foo(1,"one"), Foo(2, "two") ]

# output: show-list-with-str [<__main__.Foo object at 0x10287e208>, <__main__.Foo object at 0x10287e0c8>]
print(f"show-list-with-str {str(a)}") 


b = { "1" : Foo(1, 'one'),  "2" : Foo(2, 'two') }

# output: show-map-with-str {'1': <__main__.Foo object at 0x10287e088>, '2': <__main__.Foo object at 0x10287e148>}
print(f"show-map-with-str {str(b)}")


class Bar: 
    def __init__(self, num, s):
        self.num = num
        self.s = s
    def __repr__(self):
        return f"[s: {self.s} num: {self.num}]"


a = [ Bar(1,"one"), Bar(2, "two"), Foo(3, "foo") ]

# output: show-list-with-repr-and-one-__str__ [[s: one num: 1], [s: two num: 2], <__main__.Foo object at 0x1028cde88>] 
print(f"show-list-with-repr-and-one-__str__ {a}")

b = { "1" : Bar(1, 'one'),  "2" : Bar(2, 'two') }
# output: show-map-with-str {'1': [s: one num: 1], '2': [s: two num: 2]} 
print(f"show-map-with-str {str(b)}")


# https://stackoverflow.com/questions/44595218/python-repr-for-all-member-variables
def repr_helper(obj):
    return "{}({!r})".format(type(obj).__name__, obj.__dict__)  

class Big:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # if you want to show all members of an object, upon call to repr - something like this
    def __repr__(self):
        return repr_helper(self)  

c = Big(a, b)

# big: Big({'a': [[s: one num: 1], [s: two num: 2], <__main__.Foo object at 0x10509c3c8>], 'b': {'1': [s: one num: 1], '2': [s: two num: 2]}})
print(f"big: {c}")





