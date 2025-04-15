from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from .app import db




class Guest(db.Model, SerializerMixin):
    __tablename__ = "guests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    # add relationship

    appearances = db.relationship ('Appearance' , backref = 'guest', cascade = "all, delete")
    


    # add serialization rules

    episodes = association_proxy('appearances', 'episode')
    serialize_rules = ('-appearances.guest',)

    def __repr__(self):
        return f"<Guest {self.name}>"



class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.String)

    # add relationship

    appearances = db.relationship ("Appearance" , backref = 'episode', cascade = "all,delete")

    # add serialization rules

    guests = association_proxy('appearances', 'guest')
    serialize_rules = ('-appearances.episode',)

    def __repr__(self):
        return f"<Episode {self.number}, {self.date}>"
    
class Appearance(db.Model, SerializerMixin):
    __tablename__ = "appearances"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    # add relationships

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable= False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable= False)

    # add serialization rules

    serialize_rules = ('-guests.appearances', '-episode.appearances')


    # add validation
    @validates('rating')
    def validate_price(self, key, value):
        if value < 1 or value > 5:
            raise ValueError("Rating should be between 1 and 5")
        return value
        
    def __repr__(self):
        return f"<Appeareance ${self.rating}>"
