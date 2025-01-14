class Task:
    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus
