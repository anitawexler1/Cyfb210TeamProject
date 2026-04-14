class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped = self.items.pop()
        return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.items[-1]

    def is_empty(self):
        return not bool(self.items)

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Stack: {self.items}"

#Example usage
#stack = Stack()
#stack.push('A')
#print(stack)
#stack.push('B')
#print(stack)
#stack.push('C')
#print(stack)
#print("Top of stack:", stack.peek())
#print("Popped", stack.pop())
#print("Stack after pop:", stack)
#print("Is empty:", stack.is_empty())
#print("Size:", stack.size())
