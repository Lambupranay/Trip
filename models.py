from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class VisitInterest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    willing_to_come_to_zoo = db.Column(db.Boolean, default=False)
    willing_to_come_to_charminar = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<VisitInterest {self.name}>'
