def factorial(n):
    if n==0 or n==1stack=[]
def push():
    if len(stack)==n:
        print("overflow(stack is full)")
    else:
        item=int(input("Enter item to push"))
        stack.append(item)
        print(stack)
def pop():
    if not stack:
        print("Under flow(empty stack)")
    else:
        item=stack.pop()
        print("popped element=",item)
        print(stack)
n=int(input("Enter the stack limit:"))
while True:
    print("Select the operation 1.posh 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
       break
    else:
        print("Enter the correct operation:")
            
            
:
      return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter an integer:"))
result=factorial(n)
print("The factorial of given integer is:",result)
            
