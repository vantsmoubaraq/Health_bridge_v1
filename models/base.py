#!/usr/bin/python3

"""Module implements all common functionality amongst classes"""

import uuid
from datetime import datetime


class Base:
    """class implements all common functionality"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("updated_at"):
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%d %H:%M:%S")
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("created_at"):
                self.updated_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%d %H:%M:%S")
            else:
                self.updated_at = datetime.utcnow()
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns dictionary representation of object"""
        return self.__dict__


    def __str__(self):
        """Returns string representation of object"""
        return f"[[{self.__class__}] ({self.id}) {self.to_dict}]"
