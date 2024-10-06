from datetime import datetime

class Task:
    task_count = 0

    def __init__(self, description):
        self.id = self.set_id()
        self.decription = description
        self.status = "todo"
        self.createdAt = datetime.now().strftime("%m %d %Y")
        self.updatedAt = datetime.now().strftime("%m %d %Y")

    def get_id(self) -> int:
        return self.id
    
    def get_description(self) -> str:
        return self.decription
    
    def get_status(self) -> str:
        return self.status
    
    def get_created_str(self) -> str:
        return self.createdAt
    
    def get_updated_str(self) -> str:
        return self.updatedAt      
    
    def set_id(self) -> int:
        self.task_count += 1
        return self.task_count
    
    def set_description(self, descr) -> str:
        self.decription = descr
        self.updatedAt = datetime.now().strftime("%m %d %Y")
        return self.decription
    
    def set_status(self, stat) -> str:
        self.status = stat
        self.updatedAt = datetime.now().strftime("%m %d %Y")
        return self.status
    
    def to_Dict(self) -> dict:
        return {'id': self.get_id(), 'description': self.get_description(), 'status': self.get_status(), 'createdAt': self.get_created_str(), 'updatedAt': self.get_updated_str()}