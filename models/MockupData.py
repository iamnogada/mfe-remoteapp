from pydantic import BaseModel
import json

class Todo(BaseModel):
    def __init__(self, id: int, todo: str, categoryId: int, completed: bool):
        id: int
        todo: str
        categoryId: int
        completed: bool

Todos = []
Categories =[]
with open('data/todos.json') as f:
    data = json.load(f)
    Todos = data['todos']
    Categories = data['categories']