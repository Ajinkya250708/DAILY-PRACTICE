stack = []

def push():
    a = input("Enter value: ")
    stack.append(a)

def pop():
    if stack==[]:
        print("Stack is empty!")
        
    else:
        print("Deleted item is:", stack.pop())

def display():
    print(stack[::-1])

while True:
    print("1.Push 2.Pop 3.Display 4.Exit")
    ch = input("Choice: ")
    if ch=='1':
        push()
    elif ch=='2':
        pop()
    elif ch=='3':
        display()
    else:
        break
