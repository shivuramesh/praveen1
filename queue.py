queue=[]
def enqueue():
        item=int(input("Enter item to queue:"))
        queue.append(item)
        print(item,"inserted to queue")
def dequeue():
    if not dequeue:
        print("Under flow(empty queue)")
    else:
        item=queue.pop()
        print("delete item =",item)
def display():
    print(queue)
while True:
    print("Select the operation 1.enqueue 2.dequeue 3.dispaly 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
       display
    elif choice==4:
        break
    else:
        print("Enter the correct operation:")
            
            
