from task import Task

class TaskManager:
    def __init__(self):
        self.taskList = []

    def addTask(self, task):
        self.taskList.append(task)

    def removeTask(self, taskName):
        self.taskList = [task for task in self.taskList if task.getName() != taskName]

    def updateTask(self, taskName, updatedTask):
        for idx, task in enumerate(self.taskList):
            if task.getName() == taskName:
                self.taskList[idx] = updatedTask
                break

    def getTasks(self, filterStatus=None):
        if filterStatus:
            return [task for task in self.taskList if task.getStatus() == filterStatus]
        return self.taskList
