#!/usr/bin/python3

"""Module implements JSON filestorage engine"""

from models.base_model import BaseModel
from models.patients import Patient
from models.drugs import Drug
from models.payments import Payment
from datetime import datetime
import json

classes = {"Patient": Patient, "Drug": Drug, "Payment": Payment}

class FileStorage:
    """Class implements JSON filestorage engine"""
    __objects = {}
    __file = "file.json"

    def all(self):
        """returns all objects"""
        all_objects = {}
        for key, value in  self.__objects.items():
            all_objects[key] = value.to_dict()
        return all_objects


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

    def save(self):
        """Persists object to JSON storage"""
        all_objects = []
        for key, value in self.__objects.items():
            all_objects.append(value.to_dict())
        
        with open(self.__file, "w") as f:
            json.dump(all_objects, f)

    def reload(self):
        all_objects = []

        with open(self.__file, "r") as f:
            all_objects = json.load(f)

        for obj in all_objects:
            key = obj["__class__"] + "." + obj["id"]
            value = eval(obj["__class__"])(**obj)
            self.__objects[key] = value
        return self.__objects
