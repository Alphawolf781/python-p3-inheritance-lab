#!/usr/bin/env python

from user import User


knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]
import random

class Teacher(User):
    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        if not self.knowledge:
            return "No knowledge to teach"
        

        random_index = random.randint(0, len(self.knowledge) -1)
        return self.knowledge[random_index]
    