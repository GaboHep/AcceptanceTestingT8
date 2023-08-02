Feature: Add todo item

  Scenario: Adding a task
   Given the To-Do list is empty
   When the user adds a task "Buy groceries"
   Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
    | Task |
    | Buy groceries |
    | Pay bills |
    When the user lists all tasks
    Then the output should contain

Scenario: Mark a task as completed
  Given the to-do list contains tasks:
  | Task | Status |
  | Buy groceries | Pending |
  When the user marks task "Buy groceries" as completed
  Then the to-do list should show task "Buy groceries" as completed

Scenario: Clear the entire to-do list
  Given the to-do list contains tasks:
  | Task |
  | Buy groceries |
  | Pay bills |
  When the user clears the to-do list
  Then the to-do list should be empty

Scenario: Show most time consuming task
  Given the to-do list contains tasks:
  | Task | Time |
  | Buy groceries | 30 |
  | Pay bills | 40 |
  When the user wants to see wich of the tasks has most time consuming
  Then 1 of the tasks is selected 
  And the name of this task is: Pay bills


Scenario: Removing a task
  Given the to-do list contains tasks:
  | Task |
  | Buy groceries |
  | Pay bills |
  When the user removes the task "Pay bills"
  Then the to-do list should contain:
  | Task |
  | Buy groceries |

