class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description

    def __repr__(self):
        return f"Task(title='{self.title}', description='{self.description}')"
