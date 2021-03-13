class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

a=Node(1)
b=Node(2)
c=Node(3)

a.next_node=b
b.next_node=c

print(a.data)
print(b.data)
print(c.data)

print("a.next_node.data",a.next_node.data)
print("b.next_node.data",b.next_node.data)

print("a.get_data()",a.get_data())
print("a.get_next()()",a.get_next())


# a.get_data
# a.get_data

# class Xyi:
#     def __init__(self, data):
#         self.data=data
#         self.jopa="Jopa"
#     def say(self):
#         return (self.data,self.jopa)
# z=Xyi("bbbb")
# z.say()






