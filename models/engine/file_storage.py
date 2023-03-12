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

    def delete(self, obj_id):
        """deletes instance"""
        if obj_id in self.__objects:
            del self.__objects[obj_id]
            self.save()
        else:
            pass

    def update(self, obj_id, **kwargs):
        """updates instance attributes"""
        try:
            if obj_id in self.__objects and kwargs:
                obj = self.__objects[obj_id]
                obj_dict = obj.to_dict()
                obj_dict.update(**kwargs)
                obj = eval(obj_dict["__class__"])(**obj_dict)
                self.create(obj)
                self.save()
        except Exception:
            pass
