from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    baked_goods = db.relationship('BakedGood', back_populates='bakery')

    serialize_rules = ('-baked_goods.bakery',)

    def __str__(self):
        return f'Bakery: {self.id}, name: {self.name}, created_at: {self.created_at}'


class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    bakery = db.relationship('Bakery', back_populates='baked_goods')

    serialize_rules = ('-bakery.baked_goods',)

    def __str__(self):
        return f'Baked Good: {self.id}, name: {self.name}, price: {self.price}, created_at: {self.created_at}'
