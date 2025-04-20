import json

class Task:
    def __init__(self, id, title, description="", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"[{status}] {self.id}. {self.title} - {self.description}"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['title'], data['description'], data['completed'])
