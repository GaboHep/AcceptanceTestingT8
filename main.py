from task import Task
from to_do_list import toDo

lista = toDo()  

def get_new_task_from_user():
  name = input("enter task name: ")
  time = int(input("enter time (minutes): "))
  description = input("enter description: ")
  return name, time, description

def show_menu():
  option = int(input("1. Show task list\n2. Add task\n3. Remove task\n4. List tasks descriptions\n5. Clear list\n6. Show most time consuming task\n7. Mark a task as completed\n8. Close program\nInsert your choice: "))
  print("--------------------------------------------")
  if option == 1:
    lista.listTasks()
    print("--------------------------------------------")
  if option == 2: 
    n,t,d = get_new_task_from_user()
    tarea = Task(n,"pending",t,d)
    lista.addTask(tarea)
    print ("task added!")
    print("--------------------------------------------")
  if option == 3:
    task = input("Enter the task name you want to remove:")
    lista.removeTask(task)
  if option == 4:
    lista.listDescriptions()
  if option == 5:
    lista.clearList()
  if option == 6:
    lista.mostTimeConsumed()
  if option == 7:
    task = input("Insert the name of the task to mark: ")
    lista.markAsCompleted(task)
  if option == 8:
    return -1
  


while True:
  show_menu()
  
  
  