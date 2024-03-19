from typing import Self

from app.tasks.repositories import TaskRepository


class TaskUseCases:
    def __init__(self: Self, task_repo=TaskRepository()):
        self.task_repo = task_repo
