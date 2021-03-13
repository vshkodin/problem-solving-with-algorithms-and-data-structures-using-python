class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

a=Node(1)
b=Node(2)
c=Node(3)

a.next_node=b
b.next_node=c
b.previous_node=a
c.previous_node=b

print(a.data)
print(b.data)
print(c.data)

print(b.previous_node.data)