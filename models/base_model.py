#!/usr/bin/python3
"""BaseModel class"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """BaseModel class representing common functionalities."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        
        models.storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime and save to storage."""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict
