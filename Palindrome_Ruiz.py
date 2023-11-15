import string

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)
        if self.top is None:
            self.top = new
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("stack is empty")
        else:
            popped_element = self.top.data
            print("Popped element is:", popped_element)
            print("----------------")
            self.top = self.top.next
            return popped_element

    def display(self):
        if self.top is None:
            print("Stack is Empty")
            print("------------------")
        else:
            print("Elements of the stack are: ")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print("Top of the stack is:", self.top.data)
            print("------------------")

def is_palindrome(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    sentence = sentence.replace(" ", "")
    
    s = Stack()
    for char in sentence:
        s.push(char)

    reversed_sentence = ""
    while s.top:
        reversed_sentence += s.pop()

    return sentence == reversed_sentence



s = Stack()

while True:
    print("Enter the option below")
    print("1 - Check Palindrome\n2 - Display\n3 - Exit")
    option = int(input())

    if option == 1:
        print("Enter a sentence to check if it's a palindrome:")
        user_input = input()
        if is_palindrome(user_input):
            print("The sentence is a palindrome!")
        else:
            print("The sentence is not a palindrome.")
    elif option == 2:
        print("Display")
        print("----------")
        s.display()
    else:
        break
