""" Model handles database commucation and maping of table to objects """
from . import db

class Person(db.Model):
    id = db.Column(db.Interge(), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """ Convert person object into dict """
        data = {
            "id": self.id,
            "name": self.name
        }
        return data
    
    def from_dict(self, data):
        """ Convert person dict to obj """
        if data:
            if "name" in data:
                setattr(self, "name", data["name"])
                db.session.add(self)
                db.session.commit()
        
            
