from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


# Larpworks Models
class User(UserMixin, db.Model):
    """
    Create a User table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    phone = db.Column(db.String(20))
    user_name = db.Column(db.String(200))
    birth_month = db.Column(db.String(20), index=True)
    birth_day = db.Column(db.Integer, index=True)
    birth_year = db.Column(db.Integer, index=True)
    join_date = db.Column(db.Date, index=True)
    experience_points = db.Column(db.Integer)  # Refers to proprietary character build points
    game_points = db.Column(db.Integer)  # Refers to proprietary redeemable game points
    emergency_contact_name = db.Column(db.String(60))
    emergency_contact_number = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    user_role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    user_character = db.relationship('UserCharacter', backref='user')
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class UserRole(UserMixin, db.Model):
    """
    Create a Player Character table - all characters assigned to user
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(200))
    role = db.Column(db.String(200), index=True)
    user = db.Relationship('User', backref='user_role')


class UserCharacter(UserMixin, db.Model):
    """
    Create a User Character table - all characters assigned to user
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'user_characters'

    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(60), index=True)
    user_name = db.Column(db.String(60), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    character = db.Column('Character', backref='user_character')


class Character(UserMixin, db.Model):
    """
    Create a Player Character table - all characters assigned to user
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(60), index=True)
    player_name = db.Column(db.String(60), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class PlayerCharacter(UserMixin, db.Model):
    """
    Create a Player Character table - all characters assigned to user
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'player_character'

    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(60), index=True)
    player_name = db.Column(db.String(60), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class PlayerCharacter(UserMixin, db.Model):
    """
    Create a Player Character table - all characters assigned to user
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'player_character'

    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(60), index=True)
    player_name = db.Column(db.String(60), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class PlayerCharacter(UserMixin, db.Model):
    """
    Create a Player Character table - all characters assigned to user
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'player_character'

    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(60), index=True)
    player_name = db.Column(db.String(60), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))