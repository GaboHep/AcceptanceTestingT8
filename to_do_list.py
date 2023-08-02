class toDo:
  tasks = []

  def __init__(self):
    self.tasks = []

  def addTask(self, task):
    self.tasks.append(task)

  def removeTask(self, taskName):
    for t in self.tasks:
      if t.name == taskName:
        self.tasks.remove(t)

  def clearList(self):
    self.tasks.clear()

  def listTasks(self):
    for t in self.tasks:
      print("- " + t.name + " Status: " + t.status)

  def listDescriptions(self):
    for t in self.tasks:
      print(t.name + "\n" + "-" + t.description)

  def mostTimeConsumed(self):
    taskM = None
    mostM = 0
    for t in self.tasks:
      if t.time > mostM:
        taskM = t
        mostM = t.time
    print("- " + taskM.name)
    return taskM

  def markAsCompleted(self, taskName):
    for t in self.tasks:
      if t.name == taskName:
        t.update_status("Completed")
