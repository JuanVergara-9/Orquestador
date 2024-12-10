from .extension import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.JSON, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)