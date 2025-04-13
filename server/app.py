#!/usr/bin/env python3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource

import os
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'lateshow.db')}")


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.json.compact = False

    db.init_app(app)
    migrate.init_app(app, db)

    from server.models import Guest, Episode, Appearance


    #Homepage
    @app.route("/")
    def index():
        return "<h1>Code challenge</h1>"
    

    #GET /episodes
    @app.route('/episodes', methods = ['GET'])
    def get_episodes():
        episodes = Episode.query.all()
        return jsonify([episode.to_dict()for episode in episodes]), 200
    
    #GET /episodes/:id
    @app.route('/episodes/<int:id>', methods = ['GET'])
    def get_episode(id):
        episode = Episode.query.get(id)
        if not episode:
            return jsonify({'error': "Episode not found"}),404
        return jsonify(episode.to_dict(rules=('-appearances.episode',))),200
    
    #GET /guests
    @app.route('/guests', methods =['GET'])
    def get_guests():
        guests = Guest.query.all()
        return jsonify([guest.to_dict(only=("id", "name", "occupation"))for guest in guests]), 200
    

    #POST /appearances
    @app.route('/appearances', methods = ['POST'])
    def make_appearance():
        data = request.get_json()

        try:
            appearance = Appearance(
               rating = data['rating'],
               guest_id = data['guest_id'],
               episode_id = data['episode_id']

            )
            db.session.add(appearance)
            db.session.commit()

            return jsonify(appearance.to_dict()), 201
        
        except ValueError:
            db.session.rollback()
            return jsonify ({"errors": ["validation errors"]}), 400
        
        except Exception as e:
            db.session.rollback()
            return jsonify({"error" : str(e)}), 400
        
        
    return app











