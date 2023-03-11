#!/usr/bin/python3

"""Module implements all common functionality amongst classes"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """class implements all common functionality"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if (kwargs.get("created_at") and type(self.created_at) is str):
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    "%Y-%m-%d %H:%M:%S")
            else:
                self.created_at = datetime.utcnow()

            if (kwargs.get("updated_at") and type(self.created_at) is str):
                self.updated_at = datetime.strptime(kwargs["created_at"],
                                                    "%Y-%m-%d %H:%M:%S")
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
        attr = {}
        attr["__class__"] = self.__class__.__name__
        for key, value in dict(self.__dict__).items():
            if key == "created_at":
                attr[key] = value.strftime("%Y-%m-%d %H:%M:%S")
            elif key == "updated_at":
                attr[key] = value.strftime("%Y-%m-%d %H:%M:%S")
            else:
                attr[key] = value
        return attr

    def __str__(self):
        """Returns string representation of object"""
        return f"[[{self.__class__.__name__}] ({self.id}) {self.to_dict()}]"

    def create(self):
        """set object in all objects dictionary"""
        models.storage.create(self)

    def save(self):
        """Persists object in storage"""
        models.storage.create(self)
        models.storage.save()

    def delete(self):
        """deletes object from storage"""
        models.storage.delete(self)
