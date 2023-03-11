#!/usr/bin/python3

"""Module implements JSON filestorage engine"""

from models.base_model import BaseModel
from models.patients import Patient
from models.drugs import Drug
from models.payments import Payment
from datetime import datetime
import json


class FileStorage:
    """Class implements JSON filestorage engine"""
    self.__objects = {}
    self.__file = file.json

    classes = {"Patient": Patient, "Drug": Drug, "Payment": Payment)

    def get_all(self):
        """returns all objects"""
        return self.__objects

    def create(self, obj):
        """adds object to objects dictionary"""
        class_name = obj.__class__.__name__ 
        if class_name  in classes:
            key = class_name + "." + obj.id
            self.__objects[key] = obj

    def delete(self, obj):
        """deletes instance"""
        class_name = obj.__class__.__name__
        if class_name  in classes:
            key = class_name + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
            else:
                pass
        else:
            pass

    def update(self, obj, **kwargs):
        """updates instance attributes"""
        try:
            key = self.__class__.__name__ + "." + self.id
            if key in self.__objects and kwargs:
                for attr, value in kwargs.items():
                    if attr != "__class__":
                        if kwargs.get("created_at"):
                            obj["created_at"] = datetime.strptime(kwargs["created_at"],"%Y-%m-%d %H:%M:%S")
                        elif kwargs.get("updated_at"):
                            obj["updated_at"] = datetime.strptime(kwargs["updated_at"],"%Y-%m-%d %H:%M:%S")
                        else:
                            setattr(obj, attr, value)
        except Exception:
            pass

    def get(self, obj_id):
        """gets single object by id"""
        if obj_id in self.__objects:
            return self.__objects[obj_id]

    def save(self, obj):
        """Persists object to JSON storage"""
        class_name = obj.__class__.__name__
        if class_name  in classes:
            key = class_name + "." + obj.id
            if key in self.__objects
                obj_dict = obj.to_dict()
                with open(self.__file, "w") as f:
                    json.dump(obj_dict, f)


