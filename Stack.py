# Stack implementation using Array.

def push(ele):
    stack.append(ele)
    print("Ele pushed :", ele)

def pop():
    stack[-1] = "NA"
    stack.remove("NA")
    print("Top ele popped :")

def disp():
    c = 0
    print("--")
    for ele in reversed(stack):
        if c == 0:
            print(ele, end=" <- Top\n")
            c += 1
        else:
            print(ele, end="\n")
        print("--")

stack = []
choice = 1

while (choice != 4):

    choice = int(input("1: Push element, 2: Pop element, 3: Display 4: Exit := "))
    if choice == 1:
        n = int(input("Enter element to push on to stack : "))
        push(n)
    elif choice == 2:
        if len(stack) != 0:
            pop()
        else:
            print("Stack is empty")
    elif choice == 3:
        if len(stack) != 0:
            disp()
        else:
            print("Stack is empty")
    elif choice > 4:
        print("Wrong choice !")