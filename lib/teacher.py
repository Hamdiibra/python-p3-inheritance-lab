#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self,first_name,last_name,knowledge=None):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = knowledge if knowledge else ["Math","Science","History","Literature"]

    def teach(self):
        if self.knowledge:
            random_index = random.randint(0,len(self.knowledge) -1)
            return self.knowledge[random_index]
        else:
            return "No knowledge to teach"