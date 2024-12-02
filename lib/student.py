#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.knowledge = []
    
    def learn(self,subject):
        self.knowledge.append(subject)
        print(f"{self.first_name} has learned {subject}")