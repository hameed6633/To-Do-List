class Task:
    def __init__(self, id, title, description=""):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False
    def mark_complete(self):
        self.completed = True
    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"[{status}] {self.id}.{self.title} -  {self.description}"

