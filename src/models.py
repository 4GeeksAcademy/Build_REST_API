from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

#table of users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(250), nullable=True)
    lastname = db.Column(db.String(250), nullable=True)
    username = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.laststname,
            "usarname": self.usarname,
            "email": self.email
            # do not serialize the password, its a security breach
        }

#table of planets
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.String(250), nullable=True)
    climate = db.Column(db.String(120), nullable=True)
    population = db.Column(db.String(120), nullable=True)
    orbital_period = db.Column(db.String(120), nullable=True)
    rotation_period = db.Column(db.String(120), nullable=True)
    diameter = db.Column(db.String(3), nullable=True)
    terrain = db.Column(db.String(120), nullable=True)
    url = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
            "terrain": self.terrain,
            "url": self.url
        }

#table of characters 
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.String(250), nullable=True)
    gender = db.Column(db.String(120), nullable=True)
    hair_color = db.Column(db.String(120), nullable=True)
    eye_color = db.Column(db.String(120), nullable=True)
    birth_year = db.Column(db.String(120), nullable=True)
    height = db.Column(db.String(3), nullable=True)
    skin_color = db.Column(db.String(120), nullable=True)
    url = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Character %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "climate": self.climate,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "height": self.height,
            "skin_color": self.skin_color,
            "url": self.url
        }

#table of favorites
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
    character_id = db.Column(db.Integer, ForeignKey("character.id"), nullable=False)
    planet_id = db.Column(db.Integer, ForeignKey("planet.id"), nullable=False)
    def __repr__(self):
        return '<Favorite %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }