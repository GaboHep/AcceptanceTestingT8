from behave import *
from to_do_list import toDo
from task import Task

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
  # Set the to-do list as an empty list
  global to_do_list
  to_do_list = toDo()


# Step 2: When the user adds a task "Buy groceriesbal"
@when('the user adds a task "{task_name}"')
def step_impl1(context, task_name):
  # Add the task to the to-do list
  global to_do_list
  to_do_list.addTask(Task(task_name, "", 1, ""))


# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should contain "{task_name}"')
def step_impl2(context, task_name):
  # Check if the task is in the to-do list
  global to_do_list
  global task_names
  task_names = []
  for task in to_do_list.tasks:
    task_names.append(task.name)
  print(task_names, task_name)
  assert task_name in task_names, f'Task "{task_name}" not found in the to-do list'


#Step 1:
@given('the to-do list contains tasks')
def step_given_todo_list(context):
    global to_do_list
    global task_list
    to_do_list = toDo()
    task_list = [row['Task'] for row in context.table]
    try:
      times = [int(row['Time']) for row in context.table]
    except:
      times = [0 for i in range(len(task_list))]
    for task,time in zip(task_list, times):
      to_do_list.addTask(Task(task,"",time,""))
  
#Step 2:
@when('the user lists all tasks')
def step_when_list_all_tasks(context):
    #global to_do_list
    #to_do_list.listTasks()
  pass
    #pass  # No action needed as we are simulating the request to list tasks.

#Step 3:
@then('the output should contain')
def step_then_verify_output(context ):
    global to_do_list
    global task_list
    #expected_output = context.stdout_mock.getvalue()
    for task in to_do_list.tasks:
        assert task.name in task_list


@when(u'the user marks task "Buy groceries" as completed')
def step_impl(context):
  global to_do_list
  to_do_list.markAsCompleted("Buy groceries")
  
  


@then(u'the to-do list should show task "Buy groceries" as completed')
def step_impl(context):
  global to_do_list
  for task in to_do_list.tasks:
    if task =="Buy groceries":
      assert task.status == "Completed"

@when(u'the user clears the to-do list')
def step_impl(context):
  global to_do_list
  to_do_list.clearList()


@then(u'the to-do list should be empty')
def step_impl(context):
  global to_do_list
  assert len(to_do_list.tasks) == 0j

@when(u'the user wants to see wich of the tasks has most time consuming')
def step_impl(context):
  global to_do_list
  global M_task
  M_task = to_do_list.mostTimeConsumed()
  

  
@then(u'1 of the tasks is selected')
def step_impl(context):
  pass


@then(u'the name of this task is: Pay bills')
def step_impl(context):
  global M_task
  assert M_task.name == "Pay bills"


@when(u'the user removes the task "Pay bills"')
def step_impl(context):
  global to_do_list
  to_do_list.removeTask("Pay bills")


@then(u'the to-do list should contain')
def step_impl(context):
  global to_do_list
  tasks_names = map(lambda task: task.name, to_do_list.tasks)
  assert "Pay bills" not in task_names
    