#!/usr/bin/python3
"""This module defines a class to manage file storage"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of models in storage"""
        if cls is None:
            return self.__objects
        cls_name = cls.__name__
        new_dict = {}
        for key in self.__objects.keys():
            if key.split('.')[0] == cls_name:
                new_dict[key] = self.__objects[key]
        return new_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
            )

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                    }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                from key, value in temp.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass

        def delete(self, obj=None):
            """deletes the object from the attribute"""
            if obj in None:
                return
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.key():
                del self.__objects[obj_key]

        def close(self):
            """Reload method"""
            self.reload()
