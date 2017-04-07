from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


# Project Cyaniel Models

character_attributes = db.Table('character_attributes',
                                db.Column('character_id', db.Integer, db.ForeignKey('characters.id')),
                                db.Column('attribute_id', db.Integer, db.ForeignKey('attributes.id')),
                                db.Column('value', db.Integer),
                                db.Column('last_modified', db.DateTime)
                                )


user_roles = db.Table("user_roles",
                      db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                      db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
                      )

"""
A requirement for an AdvancementListAttribute to be visible/valid in an advancement list.
"""
advancement_list_requirements = db.Table('advancement_list_requirements',
                                         db.Column('advancement_list_attribute_id', db.Integer,
                                                   db.ForeignKey('advancement_list_attributes.id')),
                                         db.Column('attribute_requirement_id', db.Integer,
                                                   db.ForeignKey('attributes.id'))
                                         )


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
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    birth_month = db.Column(db.String(20), index=True)
    birth_day = db.Column(db.Integer, index=True)
    birth_year = db.Column(db.Integer, index=True)
    join_date = db.Column(db.DateTime, index=True)
    experience_points = db.Column(db.Integer)  # Refers to proprietary character build points
    game_points = db.Column(db.Integer)  # Refers to proprietary redeemable game points
    emergency_contact_name = db.Column(db.String(60))
    emergency_contact_number = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    last_update = db.Column(db.DateTime)
    is_admin = db.Column(db.Boolean, default=False)
    roles = db.relationship("Role", secondary=user_roles)

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


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class ExperienceLog(db.Model):
    """
    Create a log table to track player experience updates
    """

    __tablename__ = 'experience_logs'

    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character = db.relationship("Character")
    amount = db.Column(db.Integer)
    award_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Experience: {}>'.format(self.name)


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class Character(db.Model):
    """
    Create a Player Character table - all characters assigned to user
    """

    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(60), index=True)
    create_date = db.Column(db.DateTime)
    last_update = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    attributes = db.relationship("Attribute", secondary=character_attributes)

    def __repr__(self):
        return '<Character: {}>'.format(self.name)


class Attribute(db.Model):
    """
    Create a master index of all character related attributes (skills, etc...)
    """

    __tablename__ = 'attributes'

    id = db.Column(db.Integer, primary_key=True)
    attribute_name = db.Column(db.String(200), unique=True)
    description = db.Column(db.String(200))
    last_update = db.Column(db.DateTime)
    attribute_type_id = db.Column(db.Integer, db.ForeignKey('attribute_types.id'))
    attribute_type = db.relationship("AttributeType")

    def __repr__(self):
        return '<Attribute: {}>'.format(self.name)


class AttributeType(db.Model):
    __tablename__ = 'attribute_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    last_update = db.Column(db.DateTime)

    def __repr__(self):
        return '<Attribute Type: {}>'.format(self.name)


class Inventory(db.Model):
    """
    Create an Inventory table where items are tied to each character
    """

    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, index=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character = db.relationship("Character")
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item = db.relationship("Item")

    def __repr__(self):
        return '<Inventory: {}>'.format(self.name)


class Items(db.Model):
    """
    Create and Inventory table as an index for all in-game items and materials
    """

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(200), index=True, unique=True)
    description = db.Column(db.Text(200))
    item_attr = db.Column(db.Text(200))
    last_update = db.Column(db.DateTime)

    def __repr__(self):
        return '<Item: {}>'.format(self.name)


class CharacterNotes(db.Model):
    """
    Create a table to house mostly clob-like fields of character notes
    """

    __tablename__ = 'character_notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.Text(500))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character = db.relationship("Character")

    def __repr__(self):
        return '<Character Note: {}>'.format(self.name)


class AdvancementList(db.Model):
    """
    A type of list for character generation / character advancement options.
    """

    __tablename__ = 'advancement_lists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    is_chargen_only = db.Column(db.Boolean, default=False)
    is_staff_only = db.Column(db.Boolean, default=False)
    options = db.relationship('AdvancementListAttribute')

    def __repr(self):
        return "<Advancement List: {}>".format(self.name)


class AdvancementListAttribute(db.Model):
    """
    A possible option for an advancement list, assuming all AdvancementListRequirements are met.
    """

    __tablename__ = 'advancement_list_attributes'

    id = db.Column(db.Integer, primary_key=True)
    advancement_list_id = db.Column(db.Integer, db.ForeignKey("advancement_lists.id"))
    advancement_list = db.relationship('AdvancementList')
    attribute_id = db.Column(db.Integer, db.ForeignKey('attributes.id'))
    attribute = db.relationship("Attribute")
    is_staff_only = db.Column(db.Boolean, default=False)
    is_free_with_requirements = db.Column(db.Boolean, default=False)
    requirements = db.relationship('Attribute', secondary=advancement_list_requirements)

    def __repr__(self):
        return "<Advancement List Attribute: {}>".format(self.attribute.name)

