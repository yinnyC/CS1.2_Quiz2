# Write a function called reverse_string()
# that takes in a single string argument
# and reverses the string using a stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty:
            return self.items.pop()
        else:
            return "The Stack is Empty"

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items)


def reverse_string(a_str):
    """ This function reverse a string with stack """
    a_stack = Stack()
    for character in a_str:  # Push string into a stack
        a_stack.push(character)
    result = []
    while a_stack.is_empty():
        result.append(a_stack.pop())
    return "".join(result)


# Testing
a = "tac"
print(reverse_string(a))
