#EVERY DAY USE TO DO LIST
def to_do_list():
    task_list=[]
    print("----WELCOME TO LIST YOUR TASKS----")
    no_of_tasks=int(input("Enter the number of tasks to do:"))
    for i in range(1,no_of_tasks+1):
        task=input(f"Enter your task number {i} :")
        task_list.append(task)
    print(f"TODAY'S ASSIGNED TASKS ARE: \n{task_list}")
    while True:
        print("Enter the required operation to perform :")
        operations=int(input("1.ADD A TASK\n2.UPDATE YOUR LIST\n3.DELETE FROM LIST\n4.VIEW YOUR TASKS\n5.Exit\n"))
        if operations==1:
            add=input("Enter your task :")
            task_list.append(add)
            print(f"SUCCESSFULLY YOU ADDED {add} INTO THE LIST\n")
        elif operations==2:
            up_val=input("Enter the task to be updated :")
            index=task_list.index(up_val)
            new_val=input("Enter the new task :")
            task_list[index]=new_val
            print(f"SUCCESSFULLY YOU UPDATED YOUR TASK TO {new_val}")
        elif operations==3:
            del_val=input("Enter the task to be deleted :")
            if del_val in task_list:
                index=task_list.index(del_val)
                del task_list[index]
                print(f"SUCCESSFULLY DELETED YOUR TASK {del_val}")
            else:
                print("Invalid task")
        elif operations==4:
            print(f"TOTAL TASKS:\n{task_list}")
        elif operations==5:
            print("CLOSING YOUR TASKS")
            break
        else:
            print("Invalid command")   
to_do_list() 