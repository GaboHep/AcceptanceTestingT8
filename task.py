class Task:

  def __init__(self, n, s, t,d):
    self.name=n
    self.status=s
    self.time = t
    self.description = d
    
  def update_status(self, s):
    self.status = s

  def addDesc(self,d):
    self.description = d

